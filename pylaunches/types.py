"""Type definitions for the PyLaunches package."""

from __future__ import annotations

from typing import Generic, TypeVar, TypedDict

_T = TypeVar("_T")


class IdName(TypedDict):
    """Launch Library ID Name Type data object."""

    id: int
    name: str


class LauncherConfigurationFamily(IdName):
    """Launcher Configuration Family data object."""


class RocketConfiguration(IdName):
    """Rocket Configuration data object."""

    family: LauncherConfigurationFamily
    full_name: str
    launch_library_id: int
    url: str
    variant: str


class Rocket(TypedDict):
    """Launch Library Rocket Type data object."""

    configuration: RocketConfiguration
    id: str


class LaunchPadLocation(IdName):
    """Launch data object."""

    country_code: str
    map_image: str
    total_landing_count: int
    total_launch_count: int
    url: str


class LaunchServiceProvider(IdName):
    """Launch Library ID Name Type data object."""

    type: str
    url: str


class LaunchMissionOrbit(IdName):
    """Launch data object."""

    abbrev: str


class LaunchPad(IdName):
    """Launch data object."""

    agencies: list[dict]
    info_url: str
    latitude: float
    location: LaunchPadLocation
    longitude: float
    map_image: str
    map_url: str
    total_launch_count: int
    url: str
    wiki_url: str


class LaunchMission(IdName):
    """Launch data object."""

    description: str
    launch_library_id: int
    orbit: LaunchMissionOrbit
    type: str


class Launch(IdName):
    """Launch data object."""

    failreason: str
    hashtag: str
    image: str
    infographic: str
    inhold: bool
    launch_designator: str
    launch_library_id: int
    launch_service_provider: LaunchServiceProvider
    mission: LaunchMission
    net: str
    pad: LaunchPad
    probability: int
    program: list[dict]
    rocket: Rocket
    slug: str
    status: IdName
    tbddate: bool
    tbdtime: bool
    url: str
    webcast_live: bool
    window_end: str
    window_start: str


class Event(IdName):
    """Launch Library Event."""

    date: str
    description: str
    feature_image: str
    launches: list[Launch]
    location: str
    slug: str
    type: IdName


class StarshipLiveStream(TypedDict):
    """Live Stream data object."""

    description: str
    image: str
    title: str
    url: str


class StarshipRoadClosure(TypedDict):
    """Road closure data object."""

    id: str
    status: IdName
    title: str
    window_end: str
    window_start: str


class StarshipVehicle(TypedDict):
    """Vehicle data object."""

    details: str
    first_launch_date: str
    flight_proven: bool
    flights: int
    id: str
    image_url: str
    last_launch_date: str
    launcher_config: RocketConfiguration
    serial_number: str
    status: str
    url: str


class StarshipEvents(TypedDict):
    """Starship launches and events data object."""

    events: list[Event]
    launches: list[Launch]


class PyLaunchesResponse(Generic[_T], TypedDict):
    """Base class for all responses."""

    count: str
    next: str
    previous: str
    results: _T


class StarshipResponse(PyLaunchesResponse[None]):
    """Starship response data object."""

    live_streams: list[StarshipLiveStream]
    previous: StarshipEvents
    road_closures: list[StarshipRoadClosure]
    upcoming: StarshipEvents
    vehicles: list[StarshipVehicle]
