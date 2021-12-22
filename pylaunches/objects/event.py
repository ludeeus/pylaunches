from pylaunches.objects.data import PyLaunchesData
from pylaunches.objects.launch import Launch


class EventType(PyLaunchesData):
    """Event type data object."""

    @property
    def id(self) -> str:
        return self._data.get("id")

    @property
    def name(self) -> str:
        return self._data.get("name")


class Event(PyLaunchesData):
    """Event data object."""

    @property
    def id(self) -> str:
        return self._data.get("id")

    @property
    def url(self) -> str:
        return self._data.get("url")

    @property
    def slug(self) -> str:
        return self._data.get("slug")

    @property
    def name(self) -> str:
        return self._data.get("name")

    @property
    def type(self) -> EventType:
        return EventType(self._data.get("type", {}))

    @property
    def description(self) -> str:
        return self._data.get("description")

    @property
    def location(self) -> str:
        return self._data.get("location")

    @property
    def news_url(self) -> str:
        return self._data.get("news_url")

    @property
    def video_url(self) -> str:
        return self._data.get("video_url")

    @property
    def feature_image(self) -> str:
        return self._data.get("feature_image")

    @property
    def date(self) -> str:
        return self._data.get("date")

    @property
    def launches(self) -> Launch:
        return [Launch(x) for x in self._data.get("launches", [])]
