"""This module contains constants for useful apps and commands."""

# Apps
TERM = "kitty"
LAUNCHER = "rofi -show drun"
CALENDAR = "xdg-open https://calendar.proton.me"

# Screen lock
LOCKER = "light-locker-command -l"

# Audio
AUDIO_RAISE = "pamixer -ui 2"
AUDIO_LOWER = "pamixer -ud 2"
AUDIO_MUTE = "pamixer -t"
AUDIO_CTRL = "pavucontrol"

# Brightness
BRIGHT_INC = "brightnessctl set +5%"
BRIGHT_DEC = "brightnessctl set -5%"

# Screenshots
SCREENSHOT = "xfce4-screenshooter"
FULL_SCREENSHOT = "xfce4-screenshooter -fc"
