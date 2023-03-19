#!/usr/bin/env sh
# File: autostart.sh

gnome-keyring-daemon --start --components=secrets &
light-locker --lock-on-lid &
nm-applet --indicator &
blueman-applet &
dunst &

if [ "${XDG_SESSION_TYPE}" = "x11" ] ; then
	redshift-gtk &
	picom -b &
elif [ "${XDG_SESSION_TYPE}" = "wayland" ] ; then
	gammastep-indicator &
fi

# vim: ft=sh
