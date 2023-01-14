"""Provides screen-related code."""

import subprocess
from libqtile.bar import Bar
from libqtile.config import Screen
from .util import theme, widgets


def get_monitors() -> list[str]:
    """Finds the monitors that are connected."""

    # TODO: Make a wayland-equivalent alternative
    output = list(subprocess.check_output(["xrandr"]).decode("utf-8").splitlines())
    return [l.split()[0] for l in output if " connected " in l]


def make_screens(
    wallpaper_theme: theme.WallpaperTheme,
    fonts_theme: theme.FontsTheme,
    widgets_theme: theme.WidgetsTheme,
) -> list[Screen]:
    """Creates the screen(s) with bars to be used by qtile."""

    widgets_maker = widgets.WidgetsMaker(
        fonts_theme=fonts_theme, widgets_theme=widgets_theme
    )

    screens: list[Screen] = [
        Screen(
            wallpaper=wallpaper_theme.path,
            wallpaper_mode=wallpaper_theme.mode,
            top=Bar(
                widgets_maker.main_widgets,
                32,
                opacity=0.95,
                margin=6,
            ),
        ),
    ]

    # TODO: Add this back in when it works for Wayland too
    # monitors: list[str] = get_monitors()
    # if len(monitors) > 1:
    #     subprocess.call(["autorandr"])

    # for _ in range(1, len(monitors)):
    #     screens.append(
    #         Screen(
    #             wallpaper=wallpaper_theme.path,
    #             wallpaper_mode=wallpaper_theme.mode,
    #             top=Bar(
    #                 widgets_maker.other_widgets,
    #                 32,
    #                 opacity=0.95,
    #                 margin=6,
    #             ),
    #         )
    #     )

    return screens
