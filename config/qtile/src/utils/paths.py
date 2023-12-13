"""This module contains commonly used paths."""

from pathlib import Path

qtile_config: Path = Path("~/.config/qtile").expanduser()
autostart_sh: Path = qtile_config / "autostart.sh"
wallpaper: Path = Path("~/.wallpapers/carbon-dark.png").expanduser()

batt_paths: list[Path] = [
    Path("/sys/class/power_supply/BAT0/"),
]
