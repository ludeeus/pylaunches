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

    def __init__(self, loop, session):
        """Initialize the class."""
        self.loop = loop
        self.session = session

    async def api_call(self, endpoint):
        """Call the API."""
        data = None
        if self.session is None:
            self.session = aiohttp.ClientSession()
        try:
            async with async_timeout.timeout(5, loop=self.loop):
                response = await self.session.get(endpoint, headers=HEADERS)
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

    async def iso(self, source):
        """Convert to timestamp."""
        from datetime import datetime
        unix_timestamp = int(source)
        return datetime.fromtimestamp(unix_timestamp).isoformat()
