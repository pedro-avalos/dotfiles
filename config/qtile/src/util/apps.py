"""Provides what the default apps are, and functions related to them."""

from typing import Optional

from libqtile import qtile


class Apps:
    """Holds app-related functions"""

    def __init__(self, settings: dict) -> None:
        assert "apps" in settings
        compositor: str = "x11" if qtile is None else qtile.core.name
        assert compositor in settings["apps"]
        self.settings: dict = settings["apps"][compositor]

    def kill_window(self) -> None:
        """Kills the focused window."""

        if qtile is not None:
            qtile.cmd_spawn(self.settings.get("KILL_WINDOW"))

    def open_browser(self) -> None:
        """Opens default web browser."""

        if qtile is not None:
            qtile.cmd_spawn(self.settings.get("BROWSER"))

    def open_calendar(self) -> None:
        """Opens default calendar app."""

        if qtile is not None:
            qtile.cmd_spawn(self.settings.get("CALENDAR"))

    def open_launcher(self) -> None:
        """Opens default launcher."""

        if qtile is not None:
            qtile.cmd_spawn(self.settings.get("LAUNCHER"))

    def open_volume_control(self) -> None:
        """Opens default volume control app."""

        if qtile is not None:
            qtile.cmd_spawn(self.settings.get("VOLUME_CONTROL"))

    def open_app(self, name: str) -> None:
        """Opens default app for a given name."""

        if qtile is not None and name in self.settings:
            qtile.cmd_spawn(self.settings.get(name))

    def get_app(self, name: str) -> Optional[str]:
        """Retrieves specific name of app."""

        return self.settings.get(name)
