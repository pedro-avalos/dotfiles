import os.path

from libqtile import qtile, widget
from libqtile.backend.wayland.inputs import InputConfig
from libqtile.bar import Bar
from libqtile.config import Rule, Screen
from libqtile.lazy import lazy

from src.bindings import make_keys, make_mouse
from src.groups import make_groups
from src.hooks import start_once  # pyright: ignore
from src.layouts import make_floating_layout, make_layouts
from src.utils import paths

compositor = "x11" if qtile is None else qtile.core.name

# Default applications
CAL_CMD = "xdg-open https://calendar.proton.me"
TERMINAL_CMD = "kitty"
LAUNCHER_CMD = "rofi -show drun" if compositor == "x11" else "wofi --show drun"

# Volume control
RAISE_VOL_CMD = "pamixer -ui 2"
LOWER_VOL_CMD = "pamixer -ud 2"
TOGGLE_MUTE_CMD = "pamixer -t"
VOL_CTRL_CMD = "pavucontrol"

# Brightness controls
INC_BRIGHTNESS_CMD = "brightnessctl set +5%"
DEC_BRIGHTNESS_CMD = "brightnessctl set -5%"

# System-ish tools
LOCK_CMD = "light-locker-command -l"
SCREENSHOT_CMD = "xfce4-screenshooter"
FULL_SCREENSHOT_CMD = "xfce4-screenshooter -fc"


layouts = make_layouts()
floating_layout = make_floating_layout()
groups = make_groups()


class m:
    LEFT = "Button1"
    MIDDLE = "Button2"
    RIGHT = "Button3"

    WHEEL_UP = "Button4"
    WHEEL_DOWN = "Button5"
    WHEEL_LEFT = "Button6"
    WHEEL_RIGHT = "Button7"

    PREVIOUS = "Button8"
    NEXT = "Button9"


keys = make_keys(groups=groups)
mouse = make_mouse()

# Check if this machine has a battery
BATT_PATHS = ["/sys/class/power_supply/BAT0"]
show_battery = any(os.path.exists(path) for path in BATT_PATHS)

# Default color scheme
colors = {
    "bg": ["#161616", "#161616"],  # Background color
    "fg": ["#f4f4f4", "#f4f4f4"],  # Foreground color
    "py": ["#f1c21b", "#f1c21b"],  # Color for python icon
    "err": ["#ff8389", "#ff8389"],  # Color for error text
    "red": ["#fa4d56", "#fa4d56"],  # Color for exit button
    "current": ["#4589ff", "#4589ff"],  # Current border color
    "unfocus": ["#6f6f6f", "#6f6f6f"],  # Current (unfocused) border color
    "inactive": ["#6f6f6f", "#6f6f6f"],  # Inactive element
}

# Default fonts
fonts = {
    "default": "IBM Plex Mono",
    "icons": "BlexMono Nerd Font",
}

# Default widget settings
widget_defaults = {
    "font": fonts["default"],
    "fontsize": 16,
    "background": colors["bg"],
    "foreground": colors["fg"],
}

# Widgets for the main screen
main_widgets = [
    widget.Spacer(length=6, **widget_defaults),
    widget.TextBox(
        text="",
        mouse_callbacks={m.LEFT: lazy.spawn(LAUNCHER_CMD)},
        **{
            **widget_defaults,
            "foreground": colors["py"],
            "font": fonts["icons"],
        },
    ),
    widget.Spacer(length=6, **widget_defaults),
    widget.GroupBox(
        disable_drag=True,
        active=colors["fg"],
        inactive=colors["inactive"],
        highlight_method="line",
        highlight_color=colors["bg"],
        this_current_screen_border=colors["current"],
        this_screen_border=colors["unfocus"],
        other_current_screen_border="#8d8d8d",
        other_screen_border="#6f6f6f",
        urgent_alert_method="line",
        urgent_border=colors["red"],
        urgent_text=colors["err"],
        **{**widget_defaults, "font": fonts["icons"]},
    ),
    widget.Spacer(length=6, **widget_defaults),
    widget.CurrentLayoutIcon(padding=0, scale=0.6, **widget_defaults),
    widget.Spacer(**widget_defaults),
    widget.Clock(
        format=" %Y/%m/%d (%a)",
        mouse_callbacks={m.LEFT: lazy.spawn(CAL_CMD)},
        **{**widget_defaults, "font": fonts["icons"]},
    ),
    widget.Clock(
        format=" %H:%M",
        **{**widget_defaults, "font": fonts["icons"]},
    ),
    widget.Spacer(**widget_defaults),
    widget.Systray(**widget_defaults)
    if compositor == "x11"
    else widget.StatusNotifier(**widget_defaults),
    widget.Spacer(length=6, **widget_defaults),
    widget.Volume(
        fmt="󱄠 {}",
        mouse_callbacks={m.RIGHT: lazy.spawn(VOL_CTRL_CMD)},
        **{**widget_defaults, "font": fonts["icons"]},
    ),
    widget.Battery(
        format="{char} {percent:2.0%}",
        update_interval=30,
        low_percentage=0.2,
        low_foreground=colors["err"],
        full_char="󰁹",
        charge_char="󰂄",
        discharge_char="󰂀",
        empty_char="󰂎",
        unknown_char="󰂑",
        **{**widget_defaults, "font": fonts["icons"]},
    )
    if show_battery
    else widget.TextBox(text="", **widget_defaults),
    widget.KeyboardLayout(
        fmt="󰌌 {}",
        configured_keyboards=["us", "es"],
        **{**widget_defaults, "font": fonts["icons"]},
    ),
    widget.QuickExit(
        default_text="󰍃",
        countdown_format="{}",
        **{**widget_defaults, "foreground": colors["red"], "font": fonts["icons"]},
    ),
    widget.Spacer(length=6, **widget_defaults),
]

# Widgets for other screens
other_widgets = [
    widget.Spacer(length=6, **widget_defaults),
    widget.GroupBox(
        disable_drag=True,
        active=colors["fg"],
        inactive=colors["inactive"],
        highlight_method="line",
        highlight_color=colors["bg"],
        this_current_screen_border=colors["current"],
        this_screen_border=colors["unfocus"],
        other_current_screen_border="#8d8d8d",
        other_screen_border="#6f6f6f",
        urgent_alert_method="line",
        urgent_border=colors["red"],
        urgent_text=colors["err"],
        **{**widget_defaults, "font": fonts["icons"]},
    ),
    widget.CurrentLayoutIcon(scale=0.6, **widget_defaults),
    widget.Spacer(**widget_defaults),
    widget.CurrentScreen(
        active_color=colors["fg"],
        active_text="A",
        inactive_color=colors["inactive"],
        inactive_text="i",
        **widget_defaults,
    ),
    widget.Spacer(length=6, **widget_defaults),
]

# Screens for qtile to use
screens = [
    Screen(
        wallpaper=str(paths.wallpaper),
        wallpaper_mode="fill",
        top=Bar(
            widgets=main_widgets,
            size=32,
            opacity=0.95,
            background=colors["bg"],
        ),
    ),
    Screen(
        wallpaper=str(paths.wallpaper),
        wallpaper_mode="fill",
        top=Bar(
            widgets=other_widgets,
            size=32,
            opacity=0.95,
            backgrounds=colors["bg"],
        ),
    ),
]

# Miscellaneous settings
dgroups_key_binder = None
dgroups_app_rules: list[Rule] = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
auto_minimize = True
reconfigure_screns = True
focus_on_window_activation = "smart"
wl_input_rules = {
    "type:pointer": InputConfig(tap=True),
}
wmname = "LG3D"
