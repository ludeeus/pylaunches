# pylaunches [![Build Status](https://travis-ci.com/ludeeus/pylaunches.svg?branch=master)](https://travis-ci.com/ludeeus/pylaunches) [![PyPI version](https://badge.fury.io/py/pylaunches.svg)](https://badge.fury.io/py/pylaunches)

_A python packages to get information form upcoming space launches._

## Install

```bash
pip install pylaunches
```

### Example usage

```python
"""Example usage of pylaunches."""
import asyncio
import aiohttp
from pylaunches.api import Launches

async def test_pylaunches():
    """Example usage of pylaunches."""
    custom_session = aiohttp.ClientSession()
    data = Launches(LOOP, custom_session)
    await data.get_launches()

    print("Launches:", data.launches)

LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(test_pylaunches())
```

This package is using the [launchlibrary.net API][launchlibrary] to get the information.

[launchlibrary]: http://launchlibrary.net/