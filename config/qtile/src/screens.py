"""Provides screen-related code."""

from libqtile.bar import Bar
from libqtile.config import Screen

from .util.apps import Apps
from .util.settings import WidgetsSettings
from .util.theme import FontsTheme, WallpaperTheme, WidgetsTheme
from .util.widgets import WidgetsMaker


def make_screens(
    wallpaper_theme: WallpaperTheme,
    fonts_theme: FontsTheme,
    widgets_theme: WidgetsTheme,
    widgets_settings: WidgetsSettings,
    apps: Apps,
) -> list[Screen]:
    """Creates the screen(s) with bars to be used by qtile."""

    widgets_maker = WidgetsMaker(
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
        Screen(
            wallpaper=wallpaper_theme.wallpaper,
            wallpaper_mode=wallpaper_theme.wallpaper_mode,
            top=Bar(
                widgets_maker.other_widgets,
                32,
                opacity=0.95,
                margin=6,
            ),
        ),
    ]

    return screens
