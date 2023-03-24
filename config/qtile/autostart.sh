#!/usr/bin/env sh
gnome-keyring-daemon --start --components=secrets &
light-locker --lock-on-lid &
nm-applet --indicator &
blueman-applet &
dunst &
emacs --daemon &
xfce4-clipman &

if [ "${XDG_SESSION_TYPE}" = "x11" ] ; then
    redshift-gtk &
    picom --daemon &
elif [ "${XDG_SESSION_TYPE}" = "wayland" ] ; then
    gammastep-indicator
fi
