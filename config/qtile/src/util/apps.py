"""Provides what the default apps are, and functions related to them."""

from libqtile import qtile


class Apps:
    """Holds app-related functions"""

    def __init__(self, settings: dict) -> None:
        assert "apps" in settings
        assert qtile.core.name in settings["apps"]
        self.settings: dict = settings["apps"][qtile.core.name]

    def kill_window(self) -> None:
        """Kills the focused window."""

        qtile.cmd_spawn(self.settings["KILL_WINDOW"])

    def open_browser(self) -> None:
        qtile.cmd_spawn(self.settings["BROWSER"])

    def open_calendar(self) -> None:
        qtile.cmd_spawn(self.settings["CALENDAR"])

    def open_launcher(self) -> None:
        qtile.cmd_spawn(self.settings["LAUNCHER"])

    def open_volume_control(self) -> None:
        qtile.cmd_spawn(self.settings["VOLUME_CONTROL"])

    def open_app(self, appname: str) -> None:
        if appname in self.settings:
            qtile.cmd_spawn(self.settings[appname])

    def get_app(self, appname: str) -> None:
        """Retrieves specific name of app."""

        if appname in self.settings:
            return self.settings[appname]
