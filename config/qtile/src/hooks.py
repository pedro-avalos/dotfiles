"""Provides the hooks to be used by qtile."""

import subprocess
from libqtile import hook
from .util import paths


@hook.subscribe.startup_once
def autostart() -> None:
    """Executes startup programs."""

    subprocess.call([paths.scripts_dir / "autostart.sh"])


@hook.subscribe.client_new
def float_firefox(window) -> None:
    """Floats firefox windows such as dialogs and prompts."""

    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if wm_class == ("Places", "firefox") and w_name == "Library":
        window.floating = True


@hook.subscribe.client_new
def float_pycharm(window) -> None:
    """Floats dialog windows in PyCharm."""

    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if (
        wm_class == ("jetbrains-pycharm-ce", "jetbrains-pycharm-ce") and w_name == " "
    ) or (wm_class == ("java-lang-Thread", "java-lang-Thread") and w_name == "win0"):
        window.floating = True


@hook.subscribe.client_new
def float_steam(window) -> None:
    """Floats windows in Steam such as friends list."""

    wm_class = window.window.get_wm_class()
    w_name = window.window.get_name()
    if wm_class == ("Steam", "Steam") and (
        w_name != "Steam"
        or w_name == "Friends List"
        or w_name == "Screenshot Uploader"
        or w_name.startswith("Steam - News")
        or "PMaxSize" in window.window.get_wm_normal_hints().get("flags", ())
    ):
        window.floating = True
