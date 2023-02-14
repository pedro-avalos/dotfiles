#!/usr/bin/env sh
# File: autostart.sh
# Author: Pedro Avalos

gnome-keyring-daemon --start --components=secrets &
light-locker --lock-on-lid &
nm-applet --indicator &
gammastep-indicator &

if [ "${XDG_SESSION_TYPE}" = "x11" ] ; then
  picom -b &
elif [ "${XDG_SESSION_TYPE}" = "wayland" ] ; then
  :
fi
