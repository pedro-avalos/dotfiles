"""This module contains the functions to create qtile's bindings."""

from libqtile.config import Click, Drag, Group, Key, Mouse
from libqtile.lazy import lazy

from .utils import cmd, my_lazy
from .utils.io import keyboard as kb
from .utils.io import mouse as mb


def make_keys(groups: list[Group]) -> list[Key]:
    """Makes the keyboard bindings for qtile.

    Args:
        groups: List of groups used by qtile.
    """

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
            [kb.SUPER],
            kb.SPACE,
            lazy.window.toggle_floating(),
            desc="Toggle floating",
        ),
        Key(
            [kb.SUPER, kb.SHIFT],
            kb.SPACE,
            my_lazy.float_to_front,
            desc="Toggle floating",
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
            lazy.layout.shuffle_left().when(
                layout=[
                    "bsp",
                    "columns",
                ],
            ),
            lazy.layout.swap_left().when(
                layout=[
                    "monadtall",
                    "monadthreecol",
                    "monadwide",
                ],
            ),
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
            lazy.layout.shuffle_right().when(
                layout=[
                    "bsp",
                    "columns",
                ],
            ),
            lazy.layout.swap_right().when(
                layout=[
                    "monadtall",
                    "monadthreecol",
                    "monadwide",
                ],
            ),
            desc="Shuffle right",
        ),
        Key(
            [kb.SUPER, kb.SHIFT],
            "Z",
            lazy.layout.swap_main().when(
                layout=[
                    "monadtall",
                    "monadthreecol",
                    "monadwide",
                ],
            ),
            desc="Swap main",
        ),
        Key(
            [kb.SUPER, kb.ALT],
            "H",
            lazy.layout.grow_left().when(
                layout=[
                    "bsp",
                    "columns",
                ],
            ),
            desc="Grow left",
        ),
        Key(
            [kb.SUPER, kb.ALT],
            "J",
            lazy.layout.grow_down().when(
                layout=[
                    "bsp",
                    "columns",
                ],
            ),
            lazy.layout.shrink().when(
                layout=[
                    "monadtall",
                    "monadthreecol",
                    "monadwide",
                ],
            ),
            desc="Grow down",
        ),
        Key(
            [kb.SUPER, kb.ALT],
            "K",
            lazy.layout.grow_up().when(
                layout=[
                    "bsp",
                    "columns",
                ],
            ),
            lazy.layout.grow().when(
                layout=[
                    "monadtall",
                    "monadthreecol",
                    "monadwide",
                ],
            ),
            desc="Grow up",
        ),
        Key(
            [kb.SUPER, kb.ALT],
            "L",
            lazy.layout.grow_right().when(
                layout=[
                    "bsp",
                    "columns",
                ],
            ),
            desc="Grow right",
        ),
        Key(
            [kb.SUPER, kb.ALT],
            "N",
            lazy.layout.reset(),
            desc="Reset sizes",
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
            lazy.spawn(cmd.TERM),
            desc="Spawn terminal",
        ),
        Key(
            [kb.SUPER],
            "R",
            lazy.spawn(cmd.LAUNCHER),
            desc="Spawn launcher",
        ),
        Key(
            [kb.SUPER, kb.CTRL],
            "L",
            lazy.spawn(cmd.LOCKER),
            desc="Spawn screen locker",
        ),
        Key(
            [],
            kb.PRINT,
            lazy.spawn(cmd.SCREENSHOT),
            desc="Take screenshot",
        ),
        Key(
            [kb.ALT],
            kb.PRINT,
            lazy.spawn(cmd.FULL_SCREENSHOT),
            desc="take fullscreen screenshot",
        ),
        Key(
            [],
            kb.AUDIO_LOWER,
            lazy.spawn(cmd.AUDIO_LOWER),
            desc="Lower volume",
        ),
        Key(
            [],
            kb.AUDIO_RAISE,
            lazy.spawn(cmd.AUDIO_RAISE),
            desc="Raise volume",
        ),
        Key(
            [],
            kb.AUDIO_MUTE,
            lazy.spawn(cmd.AUDIO_MUTE),
            desc="Toggle mute volume",
        ),
        Key(
            [],
            kb.BRIGHT_INC,
            lazy.spawn(cmd.BRIGHT_INC),
            desc="Increase brightness",
        ),
        Key(
            [],
            kb.BRIGHT_DEC,
            lazy.spawn(cmd.BRIGHT_DEC),
            desc="Decrease brightness",
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
    """Makes the mouse bindings for qtile."""

    return [
        Drag(
            [kb.SUPER],
            mb.LEFT,
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [kb.SUPER],
            mb.RIGHT,
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        Click(
            [kb.SUPER],
            mb.WHEEL_UP,
            lazy.screen.prev_group(),
        ),
        Click(
            [kb.SUPER],
            mb.WHEEL_DOWN,
            lazy.screen.next_group(),
        ),
    ]
