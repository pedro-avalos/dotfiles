"""Qtile configuration entrypoint."""

from src.bindings import make_keys, make_mouse
from src.groups import make_groups
from src.hooks import autostart  # pyright: ignore
from src.hooks import float_firefox  # pyright: ignore
from src.hooks import float_pycharm  # pyright: ignore
from src.hooks import float_steam  # pyright: ignore
from src.layouts import make_floating_layout, make_layouts
from src.screens import make_screens
from src.util import settings, theme
from src.util.apps import Apps

# Create settings
s = settings.load_settings()
a = Apps(settings=s)
widgets_settings = settings.WidgetsSettings(settings=s)

# Create theme
t = theme.load_theme(theme_name=s["theme"]["name"])
wallpaper_theme = theme.WallpaperTheme(theme=t)
fonts_theme = theme.FontsTheme(theme=t)
layouts_theme = theme.LayoutsTheme(theme=t)
widgets_theme = theme.WidgetsTheme(theme=t)

groups = make_groups(settings=s)
keys = make_keys(groups=groups, apps=a)
mouse = make_mouse()
layouts = make_layouts(layouts_theme=layouts_theme)
floating_layout = make_floating_layout(layouts_theme=layouts_theme)
screens = make_screens(
    wallpaper_theme=wallpaper_theme,
    fonts_theme=fonts_theme,
    widgets_theme=widgets_theme,
    widgets_settings=widgets_settings,
    apps=a,
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
