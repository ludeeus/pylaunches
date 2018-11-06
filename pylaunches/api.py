"""
A python packages to get information form upcoming space launches.

This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
from .common import BASE_URL, LOGGER
from .error import LaunchesError


class Launches():
    """A class to get launch information."""

    def __init__(self, loop):
        """Initialize the class."""
        self.loop = loop
        self._launches = []

    async def get_launches(self):
        """Get launch information."""
        from .common import CommonFunctions
        common = CommonFunctions(self.loop)
        all_launches = []
        launches = {}
        data = await common.api_call(BASE_URL)
        if data is None:
            LOGGER.error('Error getting launch information')
            return
        for launch in data['launches']:
            lid = launch['id']
            launches[lid] = {}
            try:
                launches[lid]['start'] = launch['windowstart']
            except LaunchesError as error:
                launches[lid]['start'] = None
                LOGGER.error('Error getting launch information, %s', error)
            try:
                launches[lid]['wsstamp'] = launch['wsstamp']
            except LaunchesError as error:
                launches[lid]['namwsstampe'] = None
                LOGGER.error('Error getting launch information, %s', error)
            try:
                launches[lid]['name'] = launch['name']
            except LaunchesError as error:
                launches[lid]['name'] = None
                LOGGER.error('Error getting launch information, %s', error)
            try:
                launches[lid]['agency'] = (launch['location']['pads'][0]
                                           ['agencies'][0]['name'])
            except LaunchesError as error:
                launches[lid]['agency'] = None
                LOGGER.error('Error getting launch information, %s', error)
            try:
                launches[lid]['agency_country_code'] = (launch['location']
                                                        ['countryCode'])
            except LaunchesError as error:
                launches[lid]['agency_country_code'] = None
                LOGGER.error('Error getting launch information, %s', error)
            try:
                launches[lid]['stream'] = launch['vidURLs'][0]
            except LaunchesError as error:
                launches[lid]['stream'] = None
                LOGGER.error('Error getting launch information, %s', error)
            all_launches.append(launches[lid])
        self._launches = await common.sort_data(all_launches, 'start')

    @property
    def launches(self):
        """Return the launches."""
        return self._launches
