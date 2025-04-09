import pytest
from pylaunches import PyLaunches
from pylaunches.const import API_VERSION, BASE_URL, DEV_BASE_URL


@pytest.mark.asyncio
async def test_default_api_version():
    """Test default URL."""
    async with PyLaunches() as client:
        assert client._base_url == f"{BASE_URL}/{API_VERSION}"


@pytest.mark.asyncio
async def test_dev_url():
    """Test dev URL."""
    async with PyLaunches(dev=True) as client:
        assert client._base_url == f"{DEV_BASE_URL}/{API_VERSION}"
