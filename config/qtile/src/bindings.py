"""Provides the bindings (mouse and keyboard) used by qtile."""

from libqtile.config import Click, Drag, Group, Key
from libqtile.lazy import lazy

from .util import lazy_functions, scripts
from .util.apps import Apps
from .util.io import keyboard, mouse


def make_keys(groups: list[Group], apps: Apps) -> list[Key]:
    keys: list[Key] = [
        # Layout controls
        Key(
            [keyboard.SUPER],
            keyboard.TAB,
            lazy.next_layout(),
            desc="Toggle between layouts",
        ),
        # Change focus
        Key(
            [keyboard.SUPER],
            keyboard.SPACE,
            lazy.layout.next(),
            desc="Switch window focus to other pane(s) of stack",
        ),
        Key(
            [keyboard.SUPER],
            "K",
            lazy.layout.up(),
            desc="Move focus up in stack pane",
        ),
        Key(
            [keyboard.SUPER],
            "J",
            lazy.layout.down(),
            desc="Move focus down in stack pane",
        ),
        Key(
            [keyboard.SUPER],
            "H",
            lazy.layout.left(),
            desc="Move focus left in stack pane",
        ),
        Key(
            [keyboard.SUPER],
            "L",
            lazy.layout.right(),
            desc="Move focus right in stack pane",
        ),
        # Move window
        Key(
            [keyboard.SUPER, keyboard.SHIFT],
            keyboard.SPACE,
            lazy.layout.rotate(),
            lazy.layout.flip(),
            desc="Swap panes of split stack",
        ),
        Key(
            [keyboard.SUPER, keyboard.SHIFT],
            "K",
            lazy.layout.shuffle_up(),
            lazy.layout.section_up(),
            desc="Move window up in current stack",
        ),
        Key(
            [keyboard.SUPER, keyboard.SHIFT],
            "J",
            lazy.layout.shuffle_down(),
            lazy.layout.section_down(),
            desc="Move window down in current stack",
        ),
        Key(
            [keyboard.SUPER, keyboard.SHIFT],
            "H",
            lazy.layout.shuffle_left(),
            desc="Move window left in current stack",
        ),
        Key(
            [keyboard.SUPER, keyboard.SHIFT],
            "L",
            lazy.layout.shuffle_right(),
            desc="Move window right in current stack",
        ),
        # Resize window or increase number in master (tile)
        Key(
            [keyboard.SUPER],
            "M",
            lazy.layout.maximize(),
            desc="Toggle between min and max sizes",
        ),
        Key(
            [keyboard.SUPER, keyboard.SHIFT],
            "M",
            lazy.layout.toggle_fullscreen(),
            desc="Toggle fullscreen",
        ),
        Key(
            [keyboard.SUPER, keyboard.CTRL],
            "K",
            lazy.layout.grow(),
            lazy.layout.increase_nmaster(),
            desc="Expand window (monadtall), increase number in master pane (tile)",
        ),
        Key(
            [keyboard.SUPER, keyboard.CTRL],
            "J",
            lazy.layout.shrink(),
            lazy.layout.decrease_nmaster(),
            desc="Shrink window (monadtall), decrease number in master pane (tile)",
        ),
        # Move floating windows to front
        Key(
            [keyboard.SUPER, keyboard.SHIFT],
            "F",
            lazy_functions.float_to_front,
            desc="Move floating windows to front",
        ),
        # Toggle split
        Key(
            [keyboard.SUPER, keyboard.SHIFT],
            keyboard.RETURN,
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        # Reset windows/layout
        Key(
            [keyboard.SUPER],
            "N",
            lazy.layout.normalize(),
            desc="Normalize window size ratios",
        ),
        # Close window
        Key(
            [keyboard.SUPER],
            "W",
            lazy.window.kill(),
            desc="Close focused window",
        ),
        # Apps
        Key(
            [keyboard.SUPER],
            "R",
            lazy.spawn(apps.get_app("LAUNCHER")),
            desc="Open default launcher",
        ),
        Key(
            [keyboard.SUPER],
            keyboard.RETURN,
            lazy.spawn(apps.get_app("TERMINAL")),
            desc="Open default terminal",
        ),
        Key(
            [keyboard.SUPER],
            "B",
            lazy.spawn(apps.get_app("BROWSER")),
            desc="Open default browser",
        ),
        Key(
            [keyboard.SUPER],
            "E",
            lazy.spawn(apps.get_app("EDITOR")),
            desc="Open default editor",
        ),
        Key(
            [keyboard.SUPER],
            "F",
            lazy.spawn(apps.get_app("FILE_MANAGER")),
            desc="Open default file manager",
        ),
        # Screenshots
        Key(
            [],
            keyboard.PRINT,
            lazy.spawn("xfce4-screenshooter"),
            desc="Open screenshot utility",
        ),
        Key(
            [keyboard.ALT],
            keyboard.PRINT,
            lazy.spawn("xfce4-screenshooter -f -c"),
            desc="Take fullscreen screenshot",
        ),
        # Volume controls
        Key(
            [],
            keyboard.AUDIO_RAISE_VOLUME,
            lazy.spawn("pamixer -i 2"),
            desc="Raise volume",
        ),
        Key(
            [],
            keyboard.AUDIO_LOWER_VOLUME,
            lazy.spawn("pamixer -d 2"),
            desc="Lower volume",
        ),
        Key(
            [],
            keyboard.AUDIO_MUTE,
            lazy.spawn("pamixer -t"),
            desc="Toggle mute",
        ),
        # Brightness
        Key(
            [],
            keyboard.BRIGHTNESS_UP,
            lazy.spawn("brightnessctl set +5%"),
            desc="Increase monitor brightness",
        ),
        Key(
            [],
            keyboard.BRIGHTNESS_DOWN,
            lazy.spawn("brightnessctl set 5%-"),
            desc="Decrease monitor brightness",
        ),
        # Reload qtile configuration
        Key(
            [keyboard.SUPER, keyboard.CTRL],
            "R",
            lazy.reload_config(),
            desc="Restart qtile config",
        ),
        # Quit qtile
        Key(
            [keyboard.SUPER, keyboard.CTRL],
            "Q",
            lazy.shutdown(),
            desc="Exit qtile",
        ),
    ]

    for group in groups:
        keys.extend(
            [
                # super + num = switch to group
                Key(
                    [keyboard.SUPER],
                    group.name,
                    lazy.group[group.name].toscreen(),
                    desc=f"Switch to group {group.name}",
                ),
                # super + shift + name = move focused window to group
                Key(
                    [keyboard.SUPER, keyboard.SHIFT],
                    group.name,
                    lazy.window.togroup(group.name),
                    desc=f"Move focused window to group {group.name}",
                ),
            ]
        )

    return keys


def make_mouse() -> list:
    return [
        # Drag windows (turns into a floating mode)
        Drag(
            [keyboard.SUPER],
            mouse.LEFT,
            lazy.window.set_position_floating(),
        ),
        # Resize windows (turns into a floating window)
        Drag(
            [keyboard.SUPER],
            mouse.RIGHT,
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        # Bring a floating window to the front
        Click(
            [keyboard.SUPER],
            mouse.MIDDLE,
            lazy.window.bring_to_front(),
        ),
        # Change group
        Click(
            [keyboard.SUPER],
            mouse.WHEEL_UP,
            lazy.screen.prev_group(),
        ),
        Click(
            [keyboard.SUPER],
            mouse.WHEEL_DOWN,
            lazy.screen.next_group(),
        ),
    ]
