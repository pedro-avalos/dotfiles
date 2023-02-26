"""Provides useful lazy functions."""

from typing import Literal

from libqtile.config import Screen
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


@lazy.function
def traverse_up(qtile: Qtile) -> None:
    _focus_window(qtile=qtile, dir=-1, axis="y")


@lazy.function
def traverse_down(qtile: Qtile) -> None:
    _focus_window(qtile=qtile, dir=1, axis="y")


@lazy.function
def traverse_left(qtile: Qtile) -> None:
    _focus_window(qtile=qtile, dir=-1, axis="x")


@lazy.function
def traverse_right(qtile: Qtile) -> None:
    _focus_window(qtile=qtile, dir=1, axis="x")


def _focus_window(qtile: Qtile, dir: Literal[-1, 1], axis: Literal["x", "y"]) -> None:
    win = None
    win_wide = None
    dist = 10_000
    dist_wide = 10_000
    cur = qtile.current_window
    if not cur:
        cur = qtile.current_screen

    if axis == "x":
        dim = "width"
        band_axis = "y"
        band_dim = "height"
        cur_pos = cur.x  # type: ignore
        band_min = cur.y  # type: ignore
        band_max = cur.y + cur.height  # type: ignore
    elif axis == "y":
        dim = "height"
        band_axis = "x"
        band_dim = "width"
        cur_pos = cur.y  # type: ignore
        band_min = cur.x  # type: ignore
        band_max = cur.x + cur.width  # type: ignore

    cur_pos += getattr(cur, dim) / 2

    windows = [w for g in qtile.groups if g.screen for w in g.windows]
    windows.extend([s for s in qtile.screens if not s.group.windows])

    if cur in windows:
        windows.remove(cur)

    for w in windows:
        if isinstance(w, Screen) or not w.minimized:
            pos = getattr(w, axis) + getattr(w, dim) / 2
            gap = dir * (pos - cur_pos)
            if gap > 5:
                band_pos = getattr(w, band_axis) + getattr(w, band_dim) / 2
                if band_min < band_pos < band_max:
                    if gap < dist:
                        dist = gap
                        win = w
                    else:
                        if gap < dist_wide:
                            dist_wide = gap
                            win_wide = w

    if not win:
        win = win_wide
    if win:
        qtile.focus_screen(win.group.screen.index)  # type: ignore
        win.group.focus(win, True)
        if not isinstance(win, Screen):
            win.focus(False)
