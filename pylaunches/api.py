"""
A python packages to get information form upcoming space launches.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""

from __future__ import annotations
from typing import Mapping

from aiohttp import ClientSession

from .common import call_api
from .const import BASE_URL, DEFAULT_API_VERSION, DEV_BASE_URL
from .exceptions import PyLaunchesError
from .types import Launch, StarshipResponse, PyLaunchesResponse


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
        filters: Mapping[str, str] | None = None,
    ) -> list[Launch]:
        """Get upcoming launch information."""
        response: PyLaunchesResponse[list[Launch]] = await call_api(
            self.session,
            f"{self._base_url}/launch/upcoming/",
            self.token,
            params=filters,
        )
        if not (results := response.get("results")):
            raise PyLaunchesError("No launch data")
        return results

    async def dashboard_starship(
        self,
        *,
        filters: Mapping[str, str] | None = None,
    ) -> StarshipResponse:
        """Get upcoming launch information for starship."""
        response: StarshipResponse = await call_api(
            self.session,
            f"{self._base_url}/dashboard/starship/",
            self.token,
            params=filters,
        )
        if not response.get("previous", {}).get("launches"):
            raise PyLaunchesError("No starship data.")
        return response
