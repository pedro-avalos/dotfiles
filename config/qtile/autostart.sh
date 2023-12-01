#!/usr/bin/env sh
gnome-keyring-daemon --start --daemonize --components=secrets
light-locker --lock-on-lid &
nm-applet --indicator &
blueman-applet &
dunst &
udiskie --appindicator &
xfce4-clipman &

if [ "${XDG_SESSION_TYPE}" = "x11" ] ; then
    redshift-gtk &
    mkdir -p "${HOME}/.local/share/picom"
    picom --daemon --log-file "${HOME}/.local/share/picom"
elif [ "${XDG_SESSION_TYPE}" = "wayland" ] ; then
    gammastep-indicator &
fi
