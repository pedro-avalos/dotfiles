#!/usr/bin/env sh
# File: autostart.sh

gnome-keyring-daemon --start --components=secrets &
light-locker --lock-on-lid &
~/.dwm/bar.sh &
redshift &
picom -b &
