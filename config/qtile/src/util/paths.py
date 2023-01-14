"""Provides common paths used by the qtile configuration."""

from pathlib import Path

CONFIG_DIR: Path = Path("~/.config/qtile").expanduser()
scripts_dir: Path = CONFIG_DIR / "scripts"
theme_dir: Path = CONFIG_DIR / "theme"
