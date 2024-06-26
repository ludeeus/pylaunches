import pytest

from pylaunches import PyLaunches, PyLaunchesError
from pylaunches.const import HEADERS
from tests.common import fixture


@pytest.mark.asyncio
async def test_event_upcoming(aresponses):
    response = fixture("event.json", False)
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/event/upcoming/",
        "get",
        aresponses.Response(text=response, headers=HEADERS),
    )

    async with PyLaunches() as client:
        events = await client.event_upcoming()
        first = events[0]
        assert first["name"] == "string"


@pytest.mark.asyncio
async def test_event_upcoming_exceptions(aresponses):
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/event/upcoming/",
        "get",
        aresponses.Response(text="{}", headers=HEADERS),
    )
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/event/upcoming/",
        "get",
        aresponses.Response(text="{}", headers=HEADERS, status=500),
    )

    async with PyLaunches() as client:
        with pytest.raises(PyLaunchesError, match="No event data"):
            await client.event_upcoming()

    async with PyLaunches() as client:
        with pytest.raises(PyLaunchesError):
            await client.event_upcoming()


@pytest.mark.asyncio
async def test_event_upcoming_params(aresponses):
    response = fixture("event.json", False)
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/event/upcoming/?limit=1",
        "get",
        aresponses.Response(text=response, headers=HEADERS),
        match_querystring=True,
    )

    async with PyLaunches() as client:
        launches = await client.event_upcoming(filters={"limit": "1"})
        assert launches
