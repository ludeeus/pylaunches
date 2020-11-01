"""
A python packages to get information form upcoming space launches.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
from typing import List

from aiohttp import ClientSession

from pylaunches.common import call_api
from pylaunches.const import BASE_URL
from pylaunches.exceptions import PyLaunchesNoData
from pylaunches.objects.launch import Launch, LaunchResponse


class PyLaunches:
    """A class to get launch information."""

    _close_session = False

    def __init__(self, session: ClientSession or None = None) -> None:
        """Initialize the class."""
        self.session = session
        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

    async def __aenter__(self) -> None:
        """Async enter."""
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit."""
        await self._close()

    async def _close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def upcoming_launches(self) -> List[Launch] or None:
        """Get upcoming launch information."""
        response = LaunchResponse(
            await call_api(self.session, f"{BASE_URL}/launch/upcoming/")
        )
        if not response.results:
            raise PyLaunchesNoData("No data")
        return response.results
