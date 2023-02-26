"""Provides what the default apps are, and functions related to them."""

from typing import Optional

from libqtile import qtile

from . import compositor


class Apps:
    """Holds app names and app-related functions."""

    def __init__(self, settings: dict) -> None:
        assert "apps" in settings
        assert "common" in settings["apps"]
        assert compositor.name in settings["apps"]
        self.settings: dict = {
            **settings["apps"]["common"],
            **settings["apps"][compositor.name],
        }

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

    def __getitem__(self, key: str) -> Optional[str]:
        val = self.settings.get(key)
        return None if val is None else val
