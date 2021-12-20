from typing import List

from pylaunches.objects.data import PyLaunchesData


class LaunchServiceProvider(PyLaunchesData):
    """Launch data object."""

    @property
    def id(self) -> int:
        return self._data.get("id")

    @property
    def url(self) -> str:
        return self._data.get("url")

    @property
    def name(self) -> str:
        return self._data.get("name")

    @property
    def type(self) -> str:
        return self._data.get("type")


class RocketConfiguration(PyLaunchesData):
    """Launch data object."""

    @property
    def id(self) -> int:
        return self._data.get("id")

    @property
    def launch_library_id(self) -> int:
        return self._data.get("launch_library_id")

    @property
    def url(self) -> str:
        return self._data.get("url")

    @property
    def name(self) -> str:
        return self._data.get("name")

    @property
    def family(self) -> str:
        return self._data.get("family")

    @property
    def full_name(self) -> str:
        return self._data.get("full_name")

    @property
    def variant(self) -> str:
        return self._data.get("variant")


class Rocket(PyLaunchesData):
    """Launch data object."""

    @property
    def id(self) -> int:
        return self._data.get("id")

    @property
    def configuration(self) -> RocketConfiguration:
        return RocketConfiguration(self._data.get("configuration", {}))


class LaunchMissionOrbit(PyLaunchesData):
    """Launch data object."""

    @property
    def id(self) -> int:
        return self._data.get("id")

    @property
    def name(self) -> str:
        return self._data.get("name")

    @property
    def abbrev(self) -> str:
        return self._data.get("abbrev")


class LaunchMission(PyLaunchesData):
    """Launch data object."""

    @property
    def id(self) -> int:
        return self._data.get("id")

    @property
    def launch_library_id(self) -> int:
        return self._data.get("launch_library_id")

    @property
    def name(self) -> str:
        return self._data.get("name")

    @property
    def description(self) -> str:
        return self._data.get("description")

    @property
    def launch_designator(self) -> str:
        return self._data.get("launch_designator")

    @property
    def type(self) -> str:
        return self._data.get("type")

    @property
    def orbit(self) -> LaunchMissionOrbit:
        return LaunchMissionOrbit(self._data.get("orbit", {}))


class LaunchStatus(PyLaunchesData):
    """Launch data object."""

    @property
    def id(self) -> int:
        return self._data.get("id")

    @property
    def name(self) -> str:
        return self._data.get("name")


class LaunchPadLocation(PyLaunchesData):
    """Launch data object."""

    @property
    def id(self) -> int:
        return self._data.get("id")

    @property
    def url(self) -> str:
        return self._data.get("url")

    @property
    def name(self) -> str:
        return self._data.get("name")

    @property
    def country_code(self) -> str:
        return self._data.get("country_code")

    @property
    def map_image(self) -> str:
        return self._data.get("map_image")

    @property
    def total_launch_count(self) -> int:
        return self._data.get("total_launch_count")

    @property
    def total_landing_count(self) -> int:
        return self._data.get("total_landing_count")


class LaunchPad(PyLaunchesData):
    """Launch data object."""

    @property
    def id(self) -> int:
        return self._data.get("id")

    @property
    def url(self) -> str:
        return self._data.get("url")

    @property
    def agency_id(self) -> int:
        return self._data.get("agency_id")

    @property
    def name(self) -> str:
        return self._data.get("name")

    @property
    def info_url(self) -> str:
        return self._data.get("info_url")

    @property
    def wiki_url(self) -> str:
        return self._data.get("wiki_url")

    @property
    def map_url(self) -> str:
        return self._data.get("map_url")

    @property
    def latitude(self) -> str:
        return self._data.get("latitude")

    @property
    def longitude(self) -> str:
        return self._data.get("longitude")

    @property
    def location(self) -> LaunchPadLocation:
        return LaunchPadLocation(self._data.get("location", {}))

    @property
    def map_image(self) -> str:
        return self._data.get("map_image")

    @property
    def total_launch_count(self) -> int:
        return self._data.get("total_launch_count")


class Launch(PyLaunchesData):
    """Launch data object."""

    @property
    def id(self) -> str:
        return self._data.get("id")

    @property
    def url(self) -> str:
        return self._data.get("url")

    @property
    def launch_library_id(self) -> int:
        return self._data.get("launch_library_id")

    @property
    def slug(self) -> str:
        return self._data.get("slug")

    @property
    def name(self) -> str:
        return self._data.get("name")

    @property
    def status(self) -> str:
        return LaunchStatus(self._data.get("status", {}))

    @property
    def net(self) -> str:
        return self._data.get("net")

    @property
    def window_end(self) -> str:
        return self._data.get("window_end")

    @property
    def window_start(self) -> str:
        return self._data.get("window_start")

    @property
    def inhold(self) -> bool:
        return self._data.get("inhold")

    @property
    def tbdtime(self) -> bool:
        return self._data.get("tbdtime")

    @property
    def tbddate(self) -> bool:
        return self._data.get("tbddate")

    @property
    def probability(self) -> int:
        return self._data.get("probability")

    @property
    def holdreason(self) -> str:
        return self._data.get("holdreason")

    @property
    def failreason(self) -> str:
        return self._data.get("failreason")

    @property
    def hashtag(self) -> str:
        return self._data.get("hashtag")

    @property
    def launch_service_provider(self) -> LaunchServiceProvider:
        return LaunchServiceProvider(self._data.get("launch_service_provider", {}))

    @property
    def rocket(self) -> Rocket:
        return Rocket(self._data.get("rocket", {}))

    @property
    def mission(self) -> LaunchMission:
        return LaunchMission(self._data.get("mission", {}))

    @property
    def pad(self) -> LaunchPad:
        return LaunchPad(self._data.get("pad", {}))

    @property
    def webcast_live(self) -> bool:
        return self._data.get("webcast_live")

    @property
    def image(self) -> str:
        return self._data.get("image")

    @property
    def infographic(self) -> str:
        return self._data.get("infographic")

    @property
    def program(self) -> List[dict]:
        return self._data.get("program", [])


class LaunchResponse(PyLaunchesData):
    @property
    def id(self) -> int:
        return self._data.get("id")

    @property
    def next(self) -> str:
        return self._data.get("next")

    @property
    def previous(self) -> str:
        return self._data.get("previous")

    @property
    def results(self) -> List[Launch]:
        return [Launch(x) for x in self._data.get("results", [])]
