#!/usr/bin/env sh
gnome-keyring-daemon --start --daemonize --components=secrets
light-locker --lock-on-lid &
nm-applet --indicator &
blueman-applet &
dunst &
xfce4-clipman &

if [ "${XDG_SESSION_TYPE}" = "x11" ] ; then
    redshift-gtk &
    mkdir -p "${HOME}/.local/share/picom"
    picom --daemon --log-file "${HOME}/.local/share/picom"
    udiskie --no-automount --tray --appindicator &
elif [ "${XDG_SESSION_TYPE}" = "wayland" ] ; then
    gammastep-indicator &
    udiskie --no-automount --tray --appindicator --menu-update-workaround &
fi
