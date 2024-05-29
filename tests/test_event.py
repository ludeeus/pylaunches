import pytest

from pylaunches import PyLaunches, PyLaunchesError
from pylaunches.const import HEADERS
from tests.common import fixture


@pytest.mark.asyncio
async def test_event(aresponses):
    response = fixture("event.json", False)
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/event/",
        "get",
        aresponses.Response(text=response, headers=HEADERS),
    )

    async with PyLaunches() as client:
        events = await client.event()
        first = events[0]
        assert first["name"] == "string"


@pytest.mark.asyncio
async def test_event_exceptions(aresponses):
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/event/",
        "get",
        aresponses.Response(text="{}", headers=HEADERS),
    )
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/event/",
        "get",
        aresponses.Response(text="{}", headers=HEADERS, status=500),
    )

    async with PyLaunches() as client:
        with pytest.raises(PyLaunchesError, match="No event data"):
            await client.event()

    async with PyLaunches() as client:
        with pytest.raises(PyLaunchesError):
            await client.event()


@pytest.mark.asyncio
async def test_event_params(aresponses):
    response = fixture("event.json", False)
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/event/?limit=1",
        "get",
        aresponses.Response(text=response, headers=HEADERS),
        match_querystring=True,
    )

    async with PyLaunches() as client:
        launches = await client.event(filters={"limit": "1"})
        assert launches
