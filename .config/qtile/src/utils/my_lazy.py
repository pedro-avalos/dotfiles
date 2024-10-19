"""This module contains my custom lazy functions for qtile."""

from libqtile.lazy import lazy


@lazy.function
def float_to_front(qtile):
    """Moves all floating windows to the front."""

    for win in qtile.current_group.windows:
        if win.floating:
            win.cmd_bring_to_front()
