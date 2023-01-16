import shutil

import toml

from . import paths


def load_settings() -> dict:
    """Creates a dictionary out of the settings toml file."""

    settings: dict = dict()
    if not paths.settings_filepath.exists():
        shutil.copy(paths.settings_template, paths.settings_filepath)
    with open(paths.settings_filepath, "r") as f:
        settings = toml.load(f)

    return settings


class WidgetsSettings:
    """Widgets-related settings."""

    def __init__(self, settings: dict) -> None:
        self.show_battery: bool = False

        if settings and "widgets" in settings:
            for s in [
                "show_battery",
            ]:
                if s in settings["widgets"]:
                    setattr(self, s, settings["widgets"][s])
