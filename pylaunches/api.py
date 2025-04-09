"""
A python packages to get information form upcoming space launches.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""

from __future__ import annotations
from asyncio import CancelledError
from logging import getLogger, Logger
from typing import Mapping

from aiohttp import ClientSession, ClientTimeout

from .const import API_VERSION, BASE_URL, DEV_BASE_URL, HEADERS
from .exceptions import PyLaunchesError
from .types import Event, Launch, StarshipResponse, PyLaunchesResponse

LOGGER: Logger = getLogger(__package__)


class PyLaunches:
    """A class to get launch information."""

    _close_session = False

    def __init__(
        self,
        session: ClientSession | None = None,
        token: str = None,
        *,
        dev: bool = False,
    ) -> None:
        """Initialize the class."""
        self.session = session
        self.token = token
        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

        self._base_url = f"{DEV_BASE_URL if dev else BASE_URL}/{API_VERSION}"

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

    async def _call_api(
        self,
        endpoint: str,
        params: Mapping[str, str] | None = None,
    ) -> dict:
        """Call the API."""
        headers = HEADERS
        timeout = ClientTimeout(total=20)
        if (token := self.token) is not None:
            headers["Authorization"] = f"Token {token}"
        try:
            response = await self.session.get(
                endpoint,
                headers=headers,
                timeout=timeout,
                params=params,
            )
            if response.status != 200:
                raise PyLaunchesError(f"Unexpected statuscode {response.status}")
            return await response.json()
        except (CancelledError, PyLaunchesError) as exception:
            raise PyLaunchesError(exception) from exception
        except TimeoutError as exception:
            raise PyLaunchesError(
                f"Timeout of {timeout.total} reached while fetching data from {endpoint}"
            ) from exception

    async def launch_upcoming(
        self,
        *,
        filters: Mapping[str, str] | None = None,
    ) -> list[Launch]:
        """Get upcoming launch information."""
        response: PyLaunchesResponse[list[Launch]] = await self._call_api(
            f"{self._base_url}/launch/upcoming/",
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
        response: StarshipResponse = await self._call_api(
            f"{self._base_url}/dashboard/starship/",
            params=filters,
        )
        if not response.get("previous", {}).get("launches"):
            raise PyLaunchesError("No starship data.")
        return response

    async def event(
        self,
        *,
        filters: Mapping[str, str] | None = None,
    ) -> list[Event]:
        """Get events."""
        response: PyLaunchesResponse[list[Event]] = await self._call_api(
            f"{self._base_url}/event/",
            params=filters,
        )
        if not (results := response.get("results")):
            raise PyLaunchesError("No event data")
        return results

    async def event_previous(
        self,
        *,
        filters: Mapping[str, str] | None = None,
    ) -> list[Event]:
        """Get previous events."""
        response: PyLaunchesResponse[list[Event]] = await self._call_api(
            f"{self._base_url}/event/previous/",
            params=filters,
        )
        if not (results := response.get("results")):
            raise PyLaunchesError("No event data")
        return results

    async def event_upcoming(
        self,
        *,
        filters: Mapping[str, str] | None = None,
    ) -> list[Event]:
        """Get upcoming events."""
        response: PyLaunchesResponse[list[Event]] = await self._call_api(
            f"{self._base_url}/event/upcoming/",
            params=filters,
        )
        if not (results := response.get("results")):
            raise PyLaunchesError("No event data")
        return results
