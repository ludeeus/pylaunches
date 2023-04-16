import aiohttp
import pytest

from pylaunches import PyLaunches, PyLaunchesException, PyLaunchesNoData
from pylaunches.const import HEADERS
from tests.common import fixture


@pytest.mark.asyncio
async def test_upcoming_launches(aresponses):
    response = fixture("upcoming.json", False)
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/launch/upcoming/",
        "get",
        aresponses.Response(text=response, headers=HEADERS),
    )

    async with PyLaunches() as client:
        launches = await client.upcoming_launches()
        first = launches[0]
        assert first.name == "Example | Example-01"
        assert isinstance(first.raw_data_contents, dict)


@pytest.mark.asyncio
async def test_upcoming_launches_exceptions(aresponses):
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/launch/upcoming/",
        "get",
        aresponses.Response(text="{}", headers=HEADERS),
    )
    aresponses.add(
        "ll.thespacedevs.com",
        "/2.2.0/launch/upcoming/",
        "get",
        aresponses.Response(text="{}", headers=HEADERS, status=500),
    )

    async with PyLaunches() as client:
        with pytest.raises(PyLaunchesNoData):
            await client.upcoming_launches()

    async with PyLaunches() as client:
        with pytest.raises(PyLaunchesException):
            await client.upcoming_launches()
