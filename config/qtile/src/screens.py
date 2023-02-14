"""Provides screen-related code."""

import subprocess

from libqtile.bar import Bar
from libqtile.config import Screen

from .util import widgets
from .util.apps import Apps
from .util.settings import WidgetsSettings
from .util.theme import FontsTheme, WallpaperTheme, WidgetsTheme


def get_monitors() -> list[str]:
    """Finds the monitors that are connected."""

    # TODO: Make a wayland-equivalent alternative
    output = list(subprocess.check_output(["xrandr"]).decode("utf-8").splitlines())
    return [l.split()[0] for l in output if " connected " in l]


def make_screens(
    wallpaper_theme: WallpaperTheme,
    fonts_theme: FontsTheme,
    widgets_theme: WidgetsTheme,
    widgets_settings: WidgetsSettings,
    apps: Apps,
) -> list[Screen]:
    """Creates the screen(s) with bars to be used by qtile."""

    widgets_maker = widgets.WidgetsMaker(
        fonts_theme=fonts_theme,
        widgets_theme=widgets_theme,
        widgets_settings=widgets_settings,
        apps=apps,
    )

    screens: list[Screen] = [
        Screen(
            wallpaper=wallpaper_theme.wallpaper,
            wallpaper_mode=wallpaper_theme.wallpaper_mode,
            top=Bar(
                widgets_maker.main_widgets,
                32,
                opacity=0.95,
                margin=6,
            ),
        ),
    ]

    monitors: list[str] = get_monitors()
    if len(monitors) > 1:
        subprocess.call(["autorandr"])

    screens.extend(
        [
            Screen(
                top=Bar(
                    widgets_maker.other_widgets,
                    32,
                    opacity=0.95,
                    margin=6,
                )
            )
            for _ in range(1, len(monitors))
        ]
    )

    return screens
