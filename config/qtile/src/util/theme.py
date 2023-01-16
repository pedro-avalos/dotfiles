"""Provides theming settings."""

from typing import Optional

import toml

from . import paths


def load_theme(theme_name: str) -> dict:
    """Creates a dictionary out of the theme's toml file.

    theme_name: The name of the theme, without the `.toml` file extension.
    """

    theme: dict = dict()
    if theme_name:
        theme_path = paths.theme_dir / f"{theme_name}.toml"
        assert theme_path.exists()
        with open(theme_path, "r") as f:
            theme = toml.load(f)

    return theme


class WallpaperTheme:
    """Wallpaper-related theming."""

    def __init__(self, theme: Optional[dict] = None) -> None:
        self.wallpaper: Optional[str] = None
        self.mode: Optional[str] = None

        if theme and "path" in theme:
            for s in ["wallpaper", "mode"]:
                setattr(self, s, theme["wallpaper"][s])


class FontsTheme:
    """Font-related theming."""

    def __init__(self, theme: Optional[dict] = None) -> None:
        self.default: str = "sans"
        self.symbols: str = "sans"

        if theme and "fonts" in theme:
            for s in ["default", "symbols"]:
                if s in theme["layouts"]:
                    setattr(self, s, theme["fonts"][s])


class LayoutsTheme:
    """Layouts-related theming."""

    def __init__(self, theme: Optional[dict] = None) -> None:
        self.default: dict = dict()
        self.columns: dict = dict()
        self.floating: dict = dict()

        if theme and "layouts" in theme:
            for s in ["default", "columns", "floating"]:
                if s in theme["layouts"]:
                    setattr(self, s, theme["layouts"][s])


class WidgetsTheme:
    """Widgets-related theming."""

    def __init__(self, theme: Optional[dict] = None) -> None:
        self.default: dict = dict()
        self.battery: dict = dict()
        self.calendar: dict = dict()
        self.clock: dict = dict()
        self.launcher: dict = dict()
        self.windowname: dict = dict()
        self.quickexit: dict = dict()
        self.volume: dict = dict()
        self.current_layout_icon: dict = dict()
        self.groupbox: dict = dict()
        self.current_screen: dict = dict()

        if theme and "widgets" in theme:
            for s in [
                "default",
                "battery",
                "calendar",
                "clock",
                "launcher",
                "windowname",
                "quickexit",
                "volume",
                "current_layout_icon",
                "groupbox",
                "current_screen",
            ]:
                if s in theme["widgets"]:
                    setattr(self, s, theme["widgets"][s])
