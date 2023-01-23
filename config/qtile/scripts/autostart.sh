#!/usr/bin/env sh
# File: autostart.sh
# Author: Pedro Avalos

gnome-keyring-daemon --start --components=secrets &
nm-applet &

if [ "${XDG_SESSION_TYPE}" = "x11" ] ; then
  picom -b &
  redshift-gtk &
elif [ "${XDG_SESSION_TYPE}" = "wayland" ] ; then
  gammastep-indicator &
fi
