"""
A python packages to get information form upcoming space launches.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""

from __future__ import annotations
from typing import List, Mapping, Optional

from aiohttp import ClientSession

from .common import call_api
from .const import BASE_URL, DEFAULT_API_VERSION, DEV_BASE_URL
from .exceptions import PyLaunchesNoData
from .objects.launch import Launch, LaunchResponse
from .objects.starship import StarshipResponse


class PyLaunches:
    """A class to get launch information."""

    _close_session = False

    def __init__(
        self,
        session: ClientSession | None = None,
        token: str = None,
        *,
        api_version: str = DEFAULT_API_VERSION,
        dev: bool = False,
    ) -> None:
        """Initialize the class."""
        self.session = session
        self.token = token
        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

        self._base_url = f"{DEV_BASE_URL if dev else BASE_URL}/{api_version}"

    async def __aenter__(self) -> PyLaunches:
        """Async enter."""
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit."""
        await self._close()

    async def _close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def upcoming_launches(
        self,
        *,
        filters: Optional[Mapping[str, str]] = None,
    ) -> List[Launch] or None:
        """Get upcoming launch information."""
        response = LaunchResponse(
            await call_api(
                self.session,
                f"{self._base_url}/launch/upcoming/",
                self.token,
                params=filters or None,
            )
        )
        if not response.results:
            raise PyLaunchesNoData("No launch data")
        return response.results

    async def starship_events(
        self,
        *,
        filters: Optional[Mapping[str, str]] = None,
    ) -> StarshipResponse or None:
        """Get upcoming launch information for starship."""
        response = StarshipResponse(
            await call_api(
                self.session,
                f"{self._base_url}/dashboard/starship/",
                self.token,
                params=filters or None,
            )
        )
        if not response.previous.launches:
            raise PyLaunchesNoData("No starship data.")
        return response
