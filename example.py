"""Example usage of pylaunches."""
import asyncio

from pylaunches import PyLaunches, PyLaunchesException


async def example():
    """Example usage of pylaunches."""
    async with PyLaunches() as api:
        try:
            launches = await api.upcoming_launches(params={"limit": "1"})
            for launch in launches:
                print(launch.name)
        except PyLaunchesException as exception:
            print(":(", exception)


asyncio.get_event_loop().run_until_complete(example())
