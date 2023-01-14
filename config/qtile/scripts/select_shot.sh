#!/usr/bin/env sh
# File: select_shot.sh
# Author: Pedro Avalos

_now=$(date +"%Y_%m_%d-%H_%M_%S")
_file="${HOME}/Pictures/screenshots/select-${_now}.png"
maim -su "${_file}"
