import pytest
from pylaunches import PyLaunches
from pylaunches.const import DEFAULT_API_VERSION


@pytest.mark.asyncio
async def test_default_api_version():
    """Test default api version."""
    async with PyLaunches() as client:
        assert client._base_url == f"https://ll.thespacedevs.com/{DEFAULT_API_VERSION}"

@pytest.mark.asyncio
async def test_custom_api_version():
    """Test custom api version."""
    async with PyLaunches(api_version="0.1.0") as client:
        assert client._base_url == "https://ll.thespacedevs.com/0.1.0"