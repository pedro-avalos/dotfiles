#!/usr/bin/env bash
# File: bash-path.bashrc
# Add executable paths to PATH environmental variable.

# Expected executable paths
[[ -d ${HOME}/bin ]]        && PATH="${PATH}:${HOME}/bin"
[[ -d ${HOME}/.bin ]]       && PATH="${PATH}:${HOME}/.bin"
[[ -d ${HOME}/.local/bin ]] && PATH="${PATH}:${HOME}/.local/bin"

# Neovim executables, e.g. updating repository
[[ -d ${HOME}/.config/nvim/bin ]] && PATH="${PATH}:${HOME}/.config/nvim/bin"

# Emacs executables, e.g. Doom Emacs
[[ -d ${HOME}/.emacs.d/bin ]] && PATH="${PATH}:${HOME}/.emacs.d/bin"

export PATH

# vim: ft=bash
