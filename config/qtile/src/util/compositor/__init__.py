from typing import Literal

from libqtile import qtile

name: Literal["x11", "wayland"] = "x11" if qtile is None else qtile.core.name

if name == "x11":
    from .x11 import float_windows
elif name == "wayland":
    from .wayland import float_windows
else:
    raise Exception(f"Unexpected compositor name {name}")
