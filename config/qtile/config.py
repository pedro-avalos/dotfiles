"""Qtile configuration entrypoint."""

from src.util import theme
from src import bindings

# Create theme
theme.load_theme("oxocarbon")
wallpaper_theme = theme.WallpaperTheme()
fonts_theme = theme.FontsTheme()
layouts_theme = theme.LayoutsTheme()
widgets_theme = theme.WidgetsTheme()

keys = bindings.keyboard_bindings
mouse = bindings.mouse_bindings

# Other settings
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
