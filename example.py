"""Example usage of pylaunches."""

import asyncio
import logging
import os


from pylaunches import PyLaunches, PyLaunchesException

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)

log = logging.getLogger(__name__)


async def example():
    """Example usage of pylaunches."""
    async with PyLaunches(token=os.environ.get("LAUNCH_TOKEN"), dev=True) as client:
        try:
            launches = await client.upcoming_launches()
            for launch in launches:
                log.info(launch.name)
        except PyLaunchesException as exception:
            log.exception(exception)


asyncio.run(example())
