import aiohttp
import pytest

from pylaunches import PyLaunches, PyLaunchesException, PyLaunchesNoData
from pylaunches.const import HEADERS
from tests.common import fixture


@pytest.mark.asyncio
async def test_starship_events(aresponses):
    response = fixture("starship.json", False)
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/dashboard/starship/",
        "get",
        aresponses.Response(text=response, headers=HEADERS),
    )

    async with PyLaunches() as client:
        starship = await client.starship_events()
        upcoming_launch = starship.upcoming.launches[0]
        assert upcoming_launch.name == "Example | Example-01"
        upcoming_event = starship.upcoming.events[0]
        assert upcoming_event.name == "Example | Example-01"
        previous_launch = starship.previous.launches[0]
        assert previous_launch.name == "Example | Example-01"
        previous_event = starship.upcoming.events[0]
        assert previous_event.name == "Example | Example-01"
        live_stream = starship.live_streams[0]
        assert live_stream.title == "24/7 Livestream"
        road_closure = starship.road_closures[0]
        assert road_closure.title == "Primary Date"
        vehicle = starship.vehicles[0]
        assert vehicle.serial_number == "BN1"


@pytest.mark.asyncio
async def test_starship_events_exceptions(aresponses):
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/dashboard/starship/",
        "get",
        aresponses.Response(text="{}", headers=HEADERS),
    )
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/dashboard/starship/",
        "get",
        aresponses.Response(text="{}", headers=HEADERS, status=500),
    )

    async with PyLaunches() as client:
        with pytest.raises(PyLaunchesNoData):
            await client.starship_events()

    async with PyLaunches() as client:
        with pytest.raises(PyLaunchesException):
            await client.starship_events()


@pytest.mark.asyncio
async def test_starship_params(aresponses):
    response = fixture("starship.json", False)
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/dashboard/starship/?limit=1",
        "get",
        aresponses.Response(text=response, headers=HEADERS),
        match_querystring=True,
    )

    async with PyLaunches() as client:
        launches = await client.starship_events(filters={"limit": "1"})
        assert launches