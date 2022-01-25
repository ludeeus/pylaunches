from typing import Dict, List

from pylaunches.objects.data import PyLaunchesData
from pylaunches.objects.event import Event
from pylaunches.objects.launch import Launch, RocketConfiguration


class LiveStream(PyLaunchesData):
    """Live Stream data object."""

    @property
    def title(self) -> str:
        return self._data.get("title")

    @property
    def description(self) -> str:
        return self._data.get("description")

    @property
    def image(self) -> str:
        return self._data.get("image")

    @property
    def url(self) -> str:
        return self._data.get("url")


class RoadClosureStatus(PyLaunchesData):
    """Road closure status data object."""

    @property
    def id(self) -> str:
        return self._data.get("id")

    @property
    def name(self) -> str:
        return self._data.get("name")


class RoadClosure(PyLaunchesData):
    """Road closure data object."""

    @property
    def id(self) -> str:
        return self._data.get("id")

    @property
    def title(self) -> str:
        return self._data.get("title")

    @property
    def status(self) -> RoadClosureStatus:
        return RoadClosureStatus(self._data.get("status", {}))

    @property
    def window_start(self) -> str:
        return self._data.get("window_start")

    @property
    def window_end(self) -> str:
        return self._data.get("window_end")


class Vehicle(PyLaunchesData):
    """Vehicle data object."""

    @property
    def id(self) -> str:
        return self._data.get("id")

    @property
    def url(self) -> str:
        return self._data.get("url")

    @property
    def flight_proven(self) -> bool:
        return self._data.get("flight_proven")

    @property
    def serial_number(self) -> str:
        return self._data.get("serial_number")

    @property
    def status(self) -> str:
        return self._data.get("status")

    @property
    def details(self) -> str:
        return self._data.get("details")

    @property
    def launcher_config(self) -> RocketConfiguration:
        return RocketConfiguration(self._data.get("launcher_config", {}))

    @property
    def image_url(self) -> str:
        return self._data.get("image_url")

    @property
    def flights(self) -> int:
        return self._data.get("flights")

    @property
    def last_launch_date(self) -> str:
        return self._data.get("last_launch_date")

    @property
    def first_launch_date(self) -> str:
        return self._data.get("first_launch_date")


class StarshipEvents(PyLaunchesData):
    """Starship launches and events data object."""

    @property
    def launches(self) -> List[Launch]:
        return [Launch(x) for x in self._data.get("launches", [])]

    @property
    def events(self) -> List[Event]:
        return [Event(x) for x in self._data.get("events", [])]


class StarshipResponse(PyLaunchesData):
    @property
    def upcoming(self) -> StarshipEvents:
        return StarshipEvents(self._data.get("upcoming", {}))

    @property
    def previous(self) -> StarshipEvents:
        return StarshipEvents(self._data.get("previous", {}))

    @property
    def live_streams(self) -> List[LiveStream]:
        return [LiveStream(x) for x in self._data.get("live_streams", [])]

    @property
    def road_closures(self) -> List[RoadClosure]:
        return [RoadClosure(x) for x in self._data.get("road_closures", [])]

    @property
    def vehicles(self) -> List[Vehicle]:
        return [Vehicle(x) for x in self._data.get("vehicles", [])]
