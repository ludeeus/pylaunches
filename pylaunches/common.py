"""Common attributes and functions."""
from asyncio import CancelledError, TimeoutError, get_event_loop
from typing import Optional

import async_timeout
from aiohttp import ClientSession

from pylaunches.const import HEADERS
from pylaunches.exceptions import PyLaunchesException


async def call_api(
    session: ClientSession, endpoint: str, token: Optional[str]
) -> dict or None:
    """Call the API."""
    headers = HEADERS
    if token is not None:
        headers["Token"] = token
    try:
        async with async_timeout.timeout(20, loop=get_event_loop()):
            response = await session.get(endpoint, headers=headers)
            if response.status != 200:
                raise PyLaunchesException(f"Unexpected statuscode {response.status}")
            return await response.json()
    except (CancelledError, TimeoutError, PyLaunchesException) as exception:
        raise PyLaunchesException(exception)
