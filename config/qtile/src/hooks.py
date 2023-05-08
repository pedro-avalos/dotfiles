"""This module contains the functions for qtile's hooks."""

import subprocess

from libqtile import hook

from .utils import paths


@hook.subscribe.startup_once
def start_once():
    """Executes the startup script."""

    p = subprocess.Popen([paths.autostart_sh])
    hook.subscribe.shutdown(p.terminate)
