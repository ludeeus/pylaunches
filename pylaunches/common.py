"""Common attributes and functions."""

from asyncio import CancelledError, TimeoutError
from typing import Mapping, Optional

from aiohttp import ClientSession, ClientTimeout

from .const import HEADERS
from .exceptions import PyLaunchesError


async def call_api(
    session: ClientSession,
    endpoint: str,
    token: Optional[str],
    params: Optional[Mapping[str, str]],
) -> dict:
    """Call the API."""
    headers = HEADERS
    if token is not None:
        headers["Token"] = token
    try:
        response = await session.get(
            endpoint,
            headers=headers,
            timeout=ClientTimeout(total=20),
            params=params,
        )
        if response.status != 200:
            raise PyLaunchesError(f"Unexpected statuscode {response.status}")
        return await response.json()
    except (CancelledError, PyLaunchesError) as exception:
        raise PyLaunchesError(exception)
    except TimeoutError:
        raise PyLaunchesError(f"Timeout while fetching data from {endpoint}")
