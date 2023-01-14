"""Provides useful lazy functions."""

from libqtile.lazy import lazy


@lazy.function
def float_to_front(qtile):
    """Brings all flaoting windows to the top.

    Useful when floating windows are 'lost' behind tiled windows.
    """

    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()
