import json
from pathlib import Path
from typing import Any


def fixture(filename: str, asjson: bool = True) -> Any:
    """Load a fixture."""
    path = Path(__file__).parent / "fixtures" / filename
    content = path.read_text(encoding="utf-8")
    return json.loads(content) if asjson else content
