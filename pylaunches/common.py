"""Common attributes and functions."""
import logging

import aiohttp
import async_timeout

from .error import LaunchesError

LOGGER = logging.getLogger(__name__)
BASE_URL = 'https://launchlibrary.net/1.4/launch/next/1'
HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}


class CommonFunctions():
    """A class for common functions."""

    def __init__(self, loop):
        """Initialize the class."""
        self.loop = loop

    async def api_call(self, endpoint):
        """Call the API."""
        data = None
        try:
            async with async_timeout.timeout(5, loop=self.loop):
                async with aiohttp.ClientSession() as session:
                    response = await session.get(endpoint, headers=HEADERS)
                    data = await response.json()
        except LaunchesError as error:
            LOGGER.error('Error connecting to Ruter, %s', error)
        return data

    async def sort_data(self, data, sort_key, reverse=False):
        """Sort dataset."""
        sorted_data = []
        lines = sorted(data, key=lambda k: k[sort_key], reverse=reverse)
        for line in lines:
            sorted_data.append(line)
        return sorted_data
