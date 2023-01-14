#!/usr/bin/env sh
# File: select_shot_clip.sh
# Author: Pedro Avalos

case ${XDG_SESSION_TYPE} in
  "wayland")
    maim -su | wl-copy -t image/png
    ;;
  "x11")
    maim -su | xclip -selection clipboard -t image/png
    ;;
  *)
    ;;
esac

