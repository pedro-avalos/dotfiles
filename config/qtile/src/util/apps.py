"""Provides what the default apps are, and functions related to them."""

from libqtile import qtile

BROWSER = "firefox"
CALENDAR = "xdg-open https://calendar.google.com/"
EDITOR = "kitty nvim"
LAUNCHER = "rofi -show drun" if qtile.core.name == "x11" else "wofi --show drun"
LOCKER = "xscreensaver-command -l"
TERMINAL = "kitty"
VOLUME_CONTROL = "pamixer"


def kill_window() -> None:
    """Kills focused window."""

    if qtile.core.name == "x11":
        qtile.cmd_spawn("xdotool getwindowfocus windowkill")
    elif qtile.core.name == "wayland":
        qtile.cmd_spawn("wtype getwindowfocus windowkill")


def open_browser() -> None:
    """Spawns the default browser."""

    qtile.cmd_spawn(BROWSER)


def open_calendar() -> None:
    """Spawns the default calendar."""

    qtile.cmd_spawn(CALENDAR)


def open_launcher() -> None:
    """Spawns the default launcher."""

    qtile.cmd_spawn(LAUNCHER)


def open_volume_control() -> None:
    """Spawns the default volume control."""

    qtile.cmd_spawn(VOLUME_CONTROL)
