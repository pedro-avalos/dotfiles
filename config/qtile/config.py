# -*- coding: utf-8 -*-
import os
import os.path
import subprocess

import dbus
from libqtile import hook, layout, qtile, widget
from libqtile.backend.wayland.inputs import InputConfig
from libqtile.bar import Bar
from libqtile.config import Click, Drag, Group, Key, Match, Rule, Screen
from libqtile.lazy import lazy

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

@lazy.function
def float_to_front(qtile):
    """Moves all floating windows to the front."""

    for win in qtile.current_group.windows:
        if win.floating:
            win.cmd_bring_to_front()

@hook.subscribe.startup_once
def start_once():
    p = subprocess.Popen(
        [os.path.expanduser("~/.config/qtile/autostart.sh")]
    )
    hook.subscribe.shutdown(p.terminate)

# Default configuation for all layouts
layout_defaults = {
    "grow_amount": 3,
    "margin": 6,
    "border_focus": "#4589ff",
    "border_normal": "#393939",
    "border_normal_stack": "#393939",
    "border_focus_stack": "#be95ff",
}

# Layouts for qtile to use
layouts = [
    # layout.Bsp(**layout_defaults),
    layout.Columns(num_columns=3, **layout_defaults),
    layout.Floating(border_width=0, **layout_defaults),
    layout.Max(**layout_defaults),
    # layout.Matrix(**layout_defaults),
    layout.MonadTall(**layout_defaults),
    # layout.MonadThreeCol(**layout_defaults),
    # layout.MonadWide(**layout_defaults),
    # layout.RatioTile(**layout_defaults),
    layout.Stack(**layout_defaults),
    layout.Tile(**layout_defaults),
    # layout.TreeTab(**layout_defaults),
    # layout.VerticalTile(**layout_defaults),
    # layout.Zoomy(**layoutdefaultse),
]

# Setup for floating layout
floating_layout = layout.Floating(
    float_rules=[
        Match(title="Open File"),
        Match(title="File Operation Progress", wm_class="thunar"),
        Match(wm_class="Arandr"),
        Match(wm_class="org.kde.ark"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="fiji-Main"),
        Match(wm_class="file_progress"),
        Match(wm_class="imv"),
        Match(wm_class="lxappearance"),
        Match(wm_class="mpv"),
        Match(wm_class="notification"),
        Match(wm_class="notify"),
        Match(wm_class="popup_menu"),
        Match(wm_class="splash"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="Pinentry-gtk-2"),
        Match(wm_class="pinentry"),
        Match(wm_class="qt5ct"),
        Match(wm_class="ssh-askpass"),
        Match(wm_class="Dragon-drag-and-drop"),
        Match(wm_class="toolbar"),
        Match(wm_class="wlroots"),
        Match(wm_class="Xephyr"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="blueman-manager"),
        Match(wm_type="dialog"),
        Match(role="gimp-file-export"),
        Match(func=lambda c: c.has_fixed_size()),
        Match(func=lambda c: bool(c.is_transient_for())),
    ],
    border_width=0, **layout_defaults,
)

# Groups for qtile to use
groups = [
    Group(
        name="1",
        label=" 󰖟 ",
        layout="monadtall",
        matches=[],
    ),
    Group(
        name="2",
        label="  ",
        layout="monadtall",
        matches=[],
    ),
    Group(
        name="3",
        label=" 󰈙 ",
        layout="monadtall",
        matches=[],
    ),
    Group(
        name="4",
        label=" 󰭹 ",
        layout="monadtall",
        matches=[Match(wm_class="discord")],
    ),
    Group(
        name="5",
        label="  ",
        layout="monadtall",
        matches=[Match(wm_class="spotify")],
    ),
    Group(
        name="6",
        label=" 󰟴 ",
        layout="max",
        matches=[Match(wm_class="vlc"), Match(wm_class="mpv")],
    ),
    Group(
        name="7",
        label="  ",
        layout="monadtall",
        matches=[Match(wm_class="Steam")],
    ),
    Group(
        name="8",
        layout="monadtall",
        label="  ",
        matches=[],
    ),
    Group(
        name="9",
        layout="monadtall",
        label=" 󰇘 ",
        matches=[],
    ),
]

class kb:
    ALT = "mod1"
    HYPER = "mod3"
    SUPER = "mod4"
    CTRL = "control"
    SHIFT = "shift"
    SPACE = "space"
    BACKSPACE = "BackSpace"
    ENTER = "Return"
    DELETE = "Delete"
    TAB = "Tab"
    ESC = "Escape"

    EXCLAM = "exclam"
    QUOTEDBL = "quotedbl"

    PRINT = "Print"
    HOME = "Home"
    END = "End"

    LEFT = "Left"
    RIGHT = "Right"
    UP = "Up"
    DOWN = "Down"

    AUDIO_RAISE_VOLUME = "XF86AudioRaiseVolume"
    AUDIO_LOWER_VOLUME = "XF86AudioLowerVolume"
    AUDIO_MUTE = "XF86AudioMute"
    AUDIO_NEXT = "XF86AudioNext"
    AUDIO_PREV = "XF86AudioPrev"
    AUDIO_PLAY = "XF86AudioPlay"
    AUDIO_STOP = "XF86AudioStop"

    BRIGHTNESS_UP = "XF86MonBrightnessUp"
    BRIGHTNESS_DOWN = "XF86MonBrightnessDown"

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

keys = [
    Key(
        [kb.SUPER, kb.CTRL],
        "Q",
        lazy.window.kill(),
        desc="Close window",
    ),
    Key(
        [kb.SUPER],
        "F",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen",
    ),
    Key(
        [kb.SUPER, kb.SHIFT],
        kb.SPACE,
        lazy.window.toggle_floating(),
        desc="Toggle floating",
    ),
    Key(
        [kb.SUPER],
        kb.SPACE,
        float_to_front,
        desc="Float to front",
    ),
    Key(
        [kb.SUPER],
        "H",
        lazy.layout.left(),
        desc="Traverse left",
    ),
    Key(
        [kb.SUPER],
        "J",
        lazy.layout.down(),
        desc="Traverse down",
    ),
    Key(
        [kb.SUPER],
        "K",
        lazy.layout.up(),
        desc="Traverse up",
    ),
    Key(
        [kb.SUPER],
        "L",
        lazy.layout.right(),
        desc="Traverse right",
    ),
    Key(
        [kb.SUPER, kb.SHIFT],
        "H",
        lazy.layout.shuffle_left(),
        desc="Shuffle left",
    ),
    Key(
        [kb.SUPER, kb.SHIFT],
        "J",
        lazy.layout.shuffle_down(),
        desc="Shuffle down",
    ),
    Key(
        [kb.SUPER, kb.SHIFT],
        "K",
        lazy.layout.shuffle_up(),
        desc="Shuffle up",
    ),
    Key(
        [kb.SUPER, kb.SHIFT],
        "L",
        lazy.layout.shuffle_right(),
        desc="Shuffle right",
    ),
    Key(
        [kb.SUPER, kb.ALT],
        "H",
        lazy.layout.grow_left().when(layout=["bsp", "columns"]),
        desc="Grow left",
    ),
    Key(
        [kb.SUPER, kb.ALT], "J",
        lazy.layout.grow_down().when(layout=["bsp", "columns"]),
        lazy.layout.shrink().when(layout=["monadtall", "monadwide", "monadthreecol"]),
        desc="Grow down",
    ),
    Key(
        [kb.SUPER, kb.ALT], "K",
        lazy.layout.grow_up().when(layout=["bsp", "columns"]),
        lazy.layout.grow().when(layout=["monadtall", "monadwide", "monadthreecol"]),
        desc="Grow up",
    ),
    Key(
        [kb.SUPER, kb.ALT], "L",
        lazy.layout.grow_right().when(layout=["bsp", "columns"]),
        desc="Grow right",
    ),
    Key(
        [kb.SUPER, kb.ALT],
        "N",
        lazy.layout.normalize(),
        desc="Reset window size",
    ),
    Key(
        [kb.SUPER],
        kb.ESC,
        lazy.reload_config(),
        desc="Reload config",
    ),
    Key(
        [kb.SUPER, kb.SHIFT],
        kb.ESC,
        lazy.restart(),
        desc="Restart qtile",
    ),
    Key(
        [kb.SUPER, kb.CTRL],
        kb.ESC,
        lazy.shutdown(),
        desc="Shutdown qtile",
    ),
    Key(
        [kb.SUPER],
        kb.TAB,
        lazy.next_layout(),
        desc="Next layout",
    ),
    Key(
        [kb.SUPER, kb.SHIFT],
        kb.TAB,
        lazy.prev_layout(),
        desc="Previous layout",
    ),
    Key(
        [kb.SUPER],
        kb.ENTER,
        lazy.spawn(TERMINAL_CMD),
        desc="Spawn terminal",
    ),
    Key(
        [kb.SUPER],
        "R",
        lazy.spawn(LAUNCHER_CMD),
        desc="Spawn launcher",
    ),
    Key(
        [kb.SUPER, kb.CTRL],
        "L",
        lazy.spawn(LOCK_CMD),
        desc="Lock screen",
    ),
    Key(
        [],
        kb.PRINT,
        lazy.spawn(SCREENSHOT_CMD),
        desc="Take screenshot",
    ),
    Key(
        [kb.ALT],
        kb.PRINT,
        lazy.spawn(FULL_SCREENSHOT_CMD),
        desc="Take fullscreen screenshot",
    ),
    Key(
        [],
        kb.AUDIO_LOWER_VOLUME,
        lazy.spawn(LOWER_VOL_CMD),
        desc="Lower volume",
    ),
    Key(
        [],
        kb.AUDIO_RAISE_VOLUME,
        lazy.spawn(RAISE_VOL_CMD),
        desc="Raise volume",
    ),
    Key(
        [],
        kb.AUDIO_MUTE,
        lazy.spawn(TOGGLE_MUTE_CMD),
        desc="Toggle mute",
    ),
    Key(
        [],
        kb.BRIGHTNESS_UP,
        lazy.spawn(INC_BRIGHTNESS_CMD),
        desc="Increase brightness",
    ),
    Key(
        [],
        kb.BRIGHTNESS_DOWN,
        lazy.spawn(DEC_BRIGHTNESS_CMD),
        desc="Decrease brightness",
    ),
]

for group in groups:
    keys.extend([
        Key(
            [kb.SUPER],
            group.name,
            lazy.group[group.name].toscreen(),
            desc=f"Switch to group {group.name}"
        ),
        Key(
            [kb.SUPER, kb.SHIFT],
            group.name,
            lazy.window.togroup(group.name),
            desc=f"Move focused window to group {group.name}"
        ),
    ])

mouse = [
    Drag(
        [kb.SUPER], m.LEFT,
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [kb.SUPER], m.RIGHT,
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click(
        [kb.SUPER],
        m.WHEEL_UP,
        lazy.screen.prev_group()
    ),
    Click(
        [kb.SUPER],
        m.WHEEL_DOWN,
        lazy.screen.next_group(),
    ),
]

# Try to get the wallpaper from accountsservice
bus = dbus.SystemBus()
uid = os.getuid()
accts_obj = bus.get_object(
    "org.freedesktop.Accounts", f"/org/freedesktop/Accounts/User{uid}"
)
props_iface = dbus.Interface(accts_obj, "org.freedesktop.DBus.Properties")
wallpaper = props_iface.Get(
    "org.freedesktop.DisplayManager.AccountsService", "BackgroundFile"
)

# If no accountsservice wallpaper found, use backup wallpaper
if not wallpaper:
    wallpaper = "~/.config/qtile/wallpaper.png"

widget_defaults = {
    "font": "IBM Plex Mono",
    "fontsize": 16,
    "foreground": "#f4f4f4",
    "background": "#161616",
}

# Check if this machine has a battery
BATT_PATHS = ["/sys/class/power_supply/BAT0"]
show_battery = any(os.path.exists(path) for path in BATT_PATHS)

# Widgets for the main screen
main_widgets = [
    widget.Spacer(length=6, **widget_defaults),
    widget.TextBox(
        text="  ",
        mouse_callbacks={m.LEFT: lazy.spawn(LAUNCHER_CMD)},
        **{**widget_defaults, "foreground": "#f1c21b", "font": "BlexMono Nerd Font"},
    ),
    widget.Spacer(length=6, **widget_defaults),
    widget.GroupBox(
        disable_drag=True,
        active="#c6c6c6",
        inactive="#6f6f6f",
        highlight_method="line",
        highlight_color="#161616",
        this_current_screen_border="#4589ff",
        this_screen_border="#6f6f6f",
        other_current_screen_border="#8d8d8d",
        other_screen_border="#6f6f6f",
        urgent_alert_method="line",
        urgent_border="#ff8389",
        urgent_text="#ff8389",
        **{**widget_defaults, "font": "BlexMono Nerd Font"},
    ),
    widget.Spacer(length=6, **widget_defaults),
    widget.CurrentLayoutIcon(padding=0, scale=0.6, **widget_defaults),
    widget.Spacer(**widget_defaults),
    widget.Clock(
        format=" %Y/%m/%d (%a)",
        mouse_callbacks={m.LEFT: lazy.spawn(CAL_CMD)},
        **{**widget_defaults, "foreground": "#78a9ff", "font": "BlexMono Nerd Font"},
    ),
    widget.Clock(
        format=" %H:%M",
        **{**widget_defaults, "foreground": "#78a9ff", "font": "BlexMono Nerd Font"},
    ),
    widget.Spacer(**widget_defaults),
    widget.Systray(**widget_defaults)
      if compositor == "x11"
      else widget.StatusNotifier(**widget_defaults),
    widget.Spacer(length=6, **widget_defaults),
    widget.Volume(
        fmt="󱄠 {}",
        mouse_callbacks={m.RIGHT: lazy.spawn(VOL_CTRL_CMD)},
        **{**widget_defaults, "font": "BlexMono Nerd Font"},
    ),
    widget.Battery(
        format="{char} {percent:2.0%}",
        update_interval=30,
        low_percentage=0.2,
        full_char="󰁹",
        charge_char="󰂄",
        discharge_char="󰂀",
        empty_char="󰂎",
        unknown_char="󰂑",
        **{**widget_defaults, "font": "BlexMono Nerd Font"},
    ) if show_battery else widget.TextBox(text="", **widget_defaults),
    widget.KeyboardLayout(
        configured_keyboards=["us", "es"],
        **widget_defaults,
    ),
    widget.QuickExit(
        default_text="󰍃",
        **{**widget_defaults, "foreground": "#fa4d56", "font": "BlexMono Nerd Font"},
    ),
    widget.Spacer(length=6, **widget_defaults),
]

# Widgets for other screens
other_widgets = [
    widget.Spacer(length=6, **widget_defaults),
    widget.GroupBox(
        disable_drag=True,
        active="#c6c6c6",
        inactive="#6f6f6f",
        highlight_method="line",
        highlight_color="#161616",
        this_current_screen_border="#4589ff",
        this_screen_border="#6f6f6f",
        other_current_screen_border="#8d8d8d",
        other_screen_border="#6f6f6f",
        urgent_alert_method="line",
        urgent_border="#ff8389",
        urgent_text="#ff8389",
        **widget_defaults,
    ),
    widget.CurrentLayoutIcon(scale=0.6, **widget_defaults),
    widget.Spacer(**widget_defaults),
    widget.CurrentScreen(
        active_color="#f4f4f4",
        active_text="A",
        inactive_color="#8d8d8d",
        inactive_text="i",
        **widget_defaults,
    ),
    widget.Spacer(length=6, **widget_defaults),
]

# Screens for qtile to use
screens = [
    Screen(
        wallpaper=wallpaper,
        wallpaper_mode="fill",
        top=Bar(
            main_widgets, 32, opacity=0.95, margin=6,
        ),
    ),
    Screen(
        wallpaper=wallpaper,
        wallpaper_mode="fill",
        top=Bar(
            other_widgets, 32, opacity=0.95, margin=6,
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
