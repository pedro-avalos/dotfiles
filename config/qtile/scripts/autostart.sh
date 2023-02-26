#!/usr/bin/env sh
# File: autostart.sh

nm-applet --indicator &

if [ "${XDG_SESSION_TYPE}" = "x11" ] ; then
	redshift-gtk &
elif [ "${XDG_SESSION_TYPE}" = "wayland" ] ; then
	gammastep-indicator &
fi

# vim: ft=sh
