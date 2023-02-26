"""Provides the bindings (mouse and keyboard) used by qtile."""

from libqtile.config import Click, Drag, Group, Key, Mouse
from libqtile.lazy import lazy

from .util.apps import Apps
from .util.io import keyboard as kb
from .util.io import mouse as m
from .util.lazy_functions import (
    float_to_front,
    traverse_down,
    traverse_left,
    traverse_right,
    traverse_up,
)


def make_keys(groups: list[Group], apps: Apps) -> list[Key]:
    keys: list[Key] = [
        # Window management
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
            "J",
            traverse_down,
            desc="Traverse down",
        ),
        Key(
            [kb.SUPER],
            "K",
            traverse_up,
            desc="Traverse up",
        ),
        Key(
            [kb.SUPER],
            "H",
            traverse_left,
            desc="Traverse left",
        ),
        Key(
            [kb.SUPER],
            "L",
            traverse_right,
            desc="Traverse right",
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
            "H",
            lazy.layout.shuffle_left(),
            desc="Shuffle left",
        ),
        Key(
            [kb.SUPER, kb.SHIFT],
            "L",
            lazy.layout.shuffle_right(),
            desc="Shuffle right",
        ),
        Key(
            [kb.SUPER, kb.ALT],
            "J",
            lazy.layout.grow_down(),
            desc="Grow down",
        ),
        Key(
            [kb.SUPER, kb.ALT],
            "K",
            lazy.layout.grow_up(),
            desc="Grow up",
        ),
        Key(
            [kb.SUPER, kb.ALT],
            "H",
            lazy.layout.grow_left(),
            desc="Grow left",
        ),
        Key(
            [kb.SUPER, kb.ALT],
            "L",
            lazy.layout.grow_right(),
            desc="Grow right",
        ),
        Key(
            [kb.SUPER, kb.SHIFT],
            "R",
            lazy.reload_config(),
            desc="Reload config",
        ),
        Key(
            [kb.SUPER, kb.CTRL],
            "R",
            lazy.restart(),
            desc="Restart qtile",
        ),
        Key(
            [kb.SUPER],
            kb.TAB,
            lazy.next_layout(),
            desc="Next layout",
        ),
        Key(
            [kb.SUPER, kb.CTRL],
            "H",
            lazy.window.toggle_minimize(),
            desc="Minimize window",
        ),
        Key(
            [kb.SUPER],
            "S",
            lazy.window.static(),
            desc="Make window static",
        ),
        Key(
            [kb.SUPER, kb.CTRL],
            kb.ESC,
            lazy.shutdown(),
            desc="Shutdown qtile",
        ),
        # Volume controls
        Key(
            [],
            kb.AUDIO_RAISE_VOLUME,
            lazy.spawn("pamixer -i 2"),
            desc="Raise volume",
        ),
        Key(
            [],
            kb.AUDIO_LOWER_VOLUME,
            lazy.spawn("pamixer -d 2"),
            desc="Lower volume",
        ),
        Key(
            [],
            kb.AUDIO_MUTE,
            lazy.spawn("pamixer -t"),
            desc="Toggle mute",
        ),
        # Brightness control
        Key(
            [],
            kb.BRIGHTNESS_UP,
            lazy.spawn("brightnessctl set +5%"),
            desc="Increase brightness",
        ),
        Key(
            [],
            kb.BRIGHTNESS_DOWN,
            lazy.spawn("brightnessctl set 5%-"),
            desc="Decrease brightness",
        ),
        # Apps
        Key(
            [kb.SUPER],
            kb.RETURN,
            lazy.spawn(apps["TERMINAL"]),
            desc="Spawn terminal",
        ),
        Key(
            [kb.SUPER],
            "R",
            lazy.spawn(apps["LAUNCHER"]),
            desc="Spawn launcher",
        ),
        Key(
            [kb.SUPER, kb.CTRL],
            "L",
            lazy.spawn(apps["LOCKER_CMD"]),
            desc="Spawn screenlocker",
        ),
        Key(
            [kb.SUPER, kb.SHIFT],
            "B",
            lazy.spawn(apps["BROWSER"]),
            desc="Spawn browser",
        ),
        # Screenshots
        Key(
            [],
            kb.PRINT,
            lazy.spawn("xfce4-screenshooter"),
            desc="Spawn screenshot",
        ),
        Key(
            [kb.ALT],
            kb.PRINT,
            lazy.spawn("xfce4-screenshooter"),
            desc="Spawn full screenshot",
        ),
    ]

    for group in groups:
        keys.extend(
            [
                Key(
                    [kb.SUPER],
                    group.name,
                    lazy.group[group.name].toscreen(),
                    desc=f"Switch to group {group.name}",
                ),
                Key(
                    [kb.SUPER, kb.SHIFT],
                    group.name,
                    lazy.window.togroup(group.name),
                    desc=f"Move focused window to group {group.name}",
                ),
            ]
        )

    return keys


def make_mouse() -> list[Mouse]:
    return [
        # Window control
        Drag(
            [kb.SUPER],
            m.LEFT,
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [kb.SUPER],
            m.RIGHT,
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        # Group control
        Click(
            [kb.SUPER],
            m.WHEEL_UP,
            lazy.screen.prev_group(),
        ),
        Click(
            [kb.SUPER],
            m.WHEEL_DOWN,
            lazy.screen.next_group(),
        ),
    ]
