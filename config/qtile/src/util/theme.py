"""Provides theming settings."""

from typing import Optional
from pathlib import Path
import toml

from . import paths


__THEME_TOML: Optional[dict] = None


def load_theme(theme: str) -> None:
    """Loads theme."""

    global __THEME_TOML

    theme_path: Path = paths.theme_dir / f"{theme}.toml"
    assert theme_path.exists()

    with open(theme_path, "r") as f:
        __THEME_TOML = toml.load(f)


class WallpaperTheme:
    """Wallpaper-related theming."""

    def __init__(self) -> None:
        self.path: Optional[Path] = None

        if __THEME_TOML:
            for s in ["path"]:
                setattr(self, s, __THEME_TOML["wallpaper"][s])


class FontsTheme:
    """Font-related theming."""

    def __init__(self) -> None:
        self.default: str = "sans"
        self.symbols: str = "sans"

        if __THEME_TOML and "fonts" in __THEME_TOML:
            for s in ["default", "symbols"]:
                if s in __THEME_TOML["layouts"]:
                    setattr(self, s, __THEME_TOML["fonts"][s])


class LayoutsTheme:
    """Layouts-related theming."""

    def __init__(self) -> None:
        self.default: dict = dict()
        self.columns: dict = dict()
        self.floating: dict = dict()

        if __THEME_TOML and "layouts" in __THEME_TOML:
            for s in ["default", "columns", "floating"]:
                if s in __THEME_TOML["layouts"]:
                    setattr(self, s, __THEME_TOML["layouts"][s])


class WidgetsTheme:
    """Widgets-related theming."""

    def __init__(self) -> None:
        self.show_battery: bool = False

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

        if __THEME_TOML and "layouts" in __THEME_TOML:
            for s in [
                "show_battery",
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
                if s in __THEME_TOML["layouts"]:
                    setattr(self, s, __THEME_TOML["layouts"][s])
