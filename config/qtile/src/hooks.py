"""Provides the hooks to be used by qtile."""

import subprocess

from libqtile import hook
from libqtile.backend.base import Window

from .util import paths


@hook.subscribe.startup_once
def autostart() -> None:
    """Executes startup programs."""

    subprocess.call([paths.scripts_dir / "autostart.sh"])


@hook.subscribe.client_new
def float_firefox(window: Window) -> None:
    """Floats firefox windows such as dialogs and prompts."""

    info: dict = window.info()
    wm_class = info["wm_class"]
    w_name = info["name"]
    if wm_class == ("Places", "firefox") and w_name == "Library":
        window.floating = True


@hook.subscribe.client_new
def float_pycharm(window: Window) -> None:
    """Floats dialog windows in PyCharm."""

    info: dict = window.info()
    wm_class = info["wm_class"]
    w_name = info["name"]
    if (
        wm_class == ("jetbrains-pycharm-ce", "jetbrains-pycharm-ce") and w_name == " "
    ) or (wm_class == ("java-lang-Thread", "java-lang-Thread") and w_name == "win0"):
        window.floating = True


@hook.subscribe.client_new
def float_steam(window: Window) -> None:
    """Floats windows in Steam such as friends list."""

    info: dict = window.info()
    wm_class = info["wm_class"]
    w_name = info["name"]
    if wm_class == ("Steam", "Steam") and (
        w_name != "Steam"
        or w_name == "Friends List"
        or w_name == "Screenshot Uploader"
        or w_name.startswith("Steam - News")
    ):
        window.floating = True
