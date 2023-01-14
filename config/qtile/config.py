"""Qtile configuration entrypoint."""

from src.util import theme

from src.hooks import (
    autostart,  # pyright: ignore
    float_firefox,  # pyright: ignore
    float_pycharm,  # pyright: ignore
    float_steam,  # pyright: ignore
)
from src.groups import qtile_groups
from src.bindings import keyboard_bindings, mouse_bindings
from src.screens import make_screens
from src.layouts import make_layouts, make_floating_layout

# Create theme
t = theme.load_theme("oxocarbon")
wallpaper_theme = theme.WallpaperTheme(theme=t)
fonts_theme = theme.FontsTheme(theme=t)
layouts_theme = theme.LayoutsTheme(theme=t)
widgets_theme = theme.WidgetsTheme(theme=t)

groups = qtile_groups
keys = keyboard_bindings
mouse = mouse_bindings
layouts = make_layouts(layouts_theme=layouts_theme)
floating_layout = make_floating_layout(layouts_theme=layouts_theme)
screens = make_screens(
    wallpaper_theme=wallpaper_theme,
    fonts_theme=fonts_theme,
    widgets_theme=widgets_theme,
)

# Other settings
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
