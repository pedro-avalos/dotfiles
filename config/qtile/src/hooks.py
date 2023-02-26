"""Provides the hooks to be used by qtile."""

import subprocess

from libqtile import hook

from .util import scripts
from .util.compositor import float_windows # pyright: ignore


@hook.subscribe.startup_once
def autostart() -> None:
    """Executes startup programs."""

    p = subprocess.Popen([scripts.autostart])
    hook.subscribe.shutdown(p.terminate)
