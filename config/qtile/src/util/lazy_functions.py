"""Provides useful lazy functions."""

from libqtile.core.manager import Qtile
from libqtile.lazy import lazy


@lazy.function
def float_to_front(qtile: Qtile) -> None:
    """Brings all floating windows to the top.

    Useful when floating windows are 'lost' behind tiled windows.
    """

    for win in qtile.current_group.windows:
        if win.floating:
            win.cmd_bring_to_front()
