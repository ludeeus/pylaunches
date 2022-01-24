from typing import Any, Dict


class PyLaunchesData:
    def __init__(self, data: dict) -> None:
        self._data = data or {}

    @property
    def raw_data_contents(self) -> Dict[str, Any]:
        return self._data
