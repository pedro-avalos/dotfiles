#!/usr/bin/env sh
# File: autostart.sh
# Author: Pedro Avalos

redshift-gtk &
nm-applet &
gnome-keyring-daemon --start --components=secrets &
([ "${XDG_SESSION_TYPE}" = "x11" ] && picom) &
