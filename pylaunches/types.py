"""Type definitions for the PyLaunches package."""

from __future__ import annotations

from typing import Generic, Literal, TypeVar, TypedDict

_T = TypeVar("_T")


class IdNameObject(TypedDict):
    """Launch Library ID Name Type data object."""

    id: int
    name: str


class IdNameObjectWithResponseMode(IdNameObject):
    """Launch Library ID Name Type data object with response mode."""

    response_mode: Literal["list"] | Literal["normal"] | Literal["detailed"]


class License(IdNameObject):
    """Launch Library Image Type data object."""

    priority: int
    link: str


class Country(IdNameObject):
    """Launch Library Country data object."""

    alpha_2_code: str
    alpha_3_code: str
    nationality_name: str
    nationality_name_composed: str


class LaunchStatus(IdNameObject):
    """Launch Library Status Type data object."""

    abbrev: str
    description: str


class Image(IdNameObject):
    """Launch Library Image Type data object."""

    image_url: str
    thumbnail_url: str
    credit: str
    license: License
    single_use: bool


class RocketConfiguration(IdNameObjectWithResponseMode):
    """Rocket Configuration data object."""

    url: str
    full_name: str
    variant: str
    families: list[IdNameObjectWithResponseMode]


class CelestialBody(IdNameObjectWithResponseMode):
    """Celestial body data object."""

    type: IdNameObject
    diameter: float
    mass: float
    gravity: float
    length_of_day: str
    atmosphere: bool
    image: Image | None
    description: str
    wiki_url: str
    total_attempted_launches: int
    successful_launches: int
    failed_launches: int
    total_attempted_landings: int
    successful_landings: int
    failed_landings: int


class Rocket(TypedDict):
    """Launch Library Rocket Type data object."""

    configuration: RocketConfiguration
    id: str


class LaunchPadLocation(IdNameObjectWithResponseMode):
    """Launch Library Launch Pad Location data object."""

    url: str
    celestial_body: CelestialBody
    active: bool
    country: Country
    description: str
    image: Image | None
    map_image: str
    longitude: float
    latitude: float
    timezone_name: str
    total_launch_count: int
    total_landing_count: int


class LaunchServiceProvider(IdNameObjectWithResponseMode):
    """Launch Library ID Name Type data object."""

    type: IdNameObject
    url: str
    abbrev: str


class LaunchMissionOrbit(IdNameObject):
    """Launch data object."""

    abbrev: str
    celestial_body: IdNameObjectWithResponseMode


class LaunchPad(IdNameObject):
    """Launch data object."""

    url: str
    active: bool
    image: Image | None
    description: str | None
    info_url: str | None
    wiki_url: str
    map_url: str
    latitude: float
    longitude: float
    country: Country
    map_image: str
    total_launch_count: int
    orbital_launch_attempt_count: int
    fastest_turnaround: str
    location: LaunchPadLocation


class LaunchMission(IdNameObject):
    """Launch data object."""

    type: str
    description: str
    image: Image | None
    orbit: LaunchMissionOrbit


class Launch(IdNameObjectWithResponseMode):
    """Launch data object."""

    url: str
    slug: str
    launch_designator: str | None
    status: LaunchStatus
    last_updated: str
    net: str
    window_end: str
    window_start: str
    image: Image | None
    failreason: str | None
    hashtag: str | None
    launch_service_provider: LaunchServiceProvider
    rocket: Rocket
    mission: LaunchMission | None
    pad: LaunchPad
    webcast_live: bool
    program: list[dict]
    orbital_launch_attempt_count: int | None
    location_launch_attempt_count: int | None
    pad_launch_attempt_count: int | None
    agency_launch_attempt_count: int | None
    orbital_launch_attempt_count_year: int | None
    location_launch_attempt_count_year: int | None
    pad_launch_attempt_count_year: int | None
    agency_launch_attempt_count_year: int | None
    probability: int | None
    weather_concerns: str | None


class Event(IdNameObjectWithResponseMode):
    """Launch Library Event."""

    url: str
    image: Image | None
    date: str
    slug: str
    type: IdNameObject
    description: str
    webcast_live: bool
    location: str
    date_precision: str | None
    duration: str | None
    updates: list[dict]
    last_updated: str
    info_urls: list[str]
    vid_urls: list[dict]


class StarshipLiveStream(TypedDict):
    """Live Stream data object."""

    description: str
    image: str
    title: str
    url: str


class StarshipRoadClosure(TypedDict):
    """Road closure data object."""

    id: str
    status: IdNameObject
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
    previous: StarshipEvents  # type: ignore
    road_closures: list[StarshipRoadClosure]
    upcoming: StarshipEvents
    vehicles: list[StarshipVehicle]
