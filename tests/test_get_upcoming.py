import pytest

from pylaunches import PyLaunches, PyLaunchesError
from pylaunches.const import HEADERS
from tests.common import fixture


@pytest.mark.asyncio
async def test_launch_upcoming(aresponses):
    response = fixture("upcoming.json", False)
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.3.0/launches/upcoming/",
        "get",
        aresponses.Response(text=response, headers=HEADERS),
    )

    async with PyLaunches() as client:
        launches = await client.launch_upcoming()
        first = launches[0]
        assert first["name"] == "Example | Example-01"


@pytest.mark.asyncio
async def test_launch_upcoming_exceptions(aresponses):
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.3.0/launches/upcoming/",
        "get",
        aresponses.Response(text="{}", headers=HEADERS),
    )
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.3.0/launches/upcoming/",
        "get",
        aresponses.Response(text="{}", headers=HEADERS, status=500),
    )

    async with PyLaunches() as client:
        with pytest.raises(PyLaunchesError, match="No launch data"):
            await client.launch_upcoming()

    async with PyLaunches() as client:
        with pytest.raises(PyLaunchesError):
            await client.launch_upcoming()


@pytest.mark.asyncio
async def test_launch_upcoming_params(aresponses):
    response = fixture("upcoming.json", False)
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.3.0/launches/upcoming/?limit=1",
        "get",
        aresponses.Response(text=response, headers=HEADERS),
        match_querystring=True,
    )

    async with PyLaunches() as client:
        launches = await client.launch_upcoming(filters={"limit": "1"})
        assert launches
