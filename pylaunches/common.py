"""Common attributes and functions."""
from asyncio import CancelledError, TimeoutError
from typing import Optional

from aiohttp import ClientSession, ClientTimeout

from pylaunches.const import HEADERS
from pylaunches.exceptions import PyLaunchesException


async def call_api(
    session: ClientSession,
    endpoint: str,
    token: Optional[str],
) -> dict or None:
    """Call the API."""
    headers = HEADERS
    if token is not None:
        headers["Token"] = token
    try:
        response = await session.get(
            endpoint,
            headers=headers,
            timeout=ClientTimeout(total=20),
        )
        if response.status != 200:
            raise PyLaunchesException(f"Unexpected statuscode {response.status}")
        return await response.json()
    except (CancelledError, PyLaunchesException) as exception:
        raise PyLaunchesException(exception)
    except TimeoutError:
        raise PyLaunchesException(f"Timeout while fetching data from {endpoint}")
