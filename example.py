"""Example usage of pylaunches."""

import asyncio
import logging
import os


from pylaunches import PyLaunches, PyLaunchesError

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
            events = await client.event_upcoming(filters={"limit": 1, "program": "1"})
            for event in events:
                log.info("%s", event["name"])
        except PyLaunchesError as exception:
            log.exception(exception)


asyncio.run(example())
