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

# Create theme
t = theme.load_theme("oxocarbon")
wallpaper_theme = theme.WallpaperTheme(theme=t)
fonts_theme = theme.FontsTheme(theme=t)
layouts_theme = theme.LayoutsTheme(theme=t)
widgets_theme = theme.WidgetsTheme(theme=t)

groups = qtile_groups
keys = keyboard_bindings
mouse = mouse_bindings

# Other settings
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
