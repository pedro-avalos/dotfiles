"""Provides common paths used by the qtile configuration."""

from pathlib import Path

CONFIG_DIR = Path("~/.config/qtile").expanduser()
scripts_dir = CONFIG_DIR / "scripts"
theme_dir = CONFIG_DIR / "theme"
settings_dir = CONFIG_DIR / "settings"
settings_filepath = settings_dir / "settings.toml"
settings_template = settings_dir / "_template.toml"
