import pytest
from pylaunches import PyLaunches
from pylaunches.const import BASE_URL, DEFAULT_API_VERSION, DEV_BASE_URL


@pytest.mark.asyncio
async def test_default_api_version():
    """Test default api version."""
    async with PyLaunches() as client:
        assert client._base_url == f"{BASE_URL}/{DEFAULT_API_VERSION}"


@pytest.mark.asyncio
async def test_custom_api_version():
    """Test custom api version."""
    async with PyLaunches(api_version="0.1.0") as client:
        assert client._base_url == f"{BASE_URL}/0.1.0"


@pytest.mark.asyncio
async def test_dev_url():
    """Test custom api version."""
    async with PyLaunches(dev=True) as client:
        assert client._base_url == f"{DEV_BASE_URL}/{DEFAULT_API_VERSION}"
