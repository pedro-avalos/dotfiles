#!/usr/bin/env bash

[[ -d ~/bin ]]        && PATH="${PATH}:${HOME}/bin"
[[ -d ~/.bin ]]       && PATH="${PATH}:${HOME}/.bin"
[[ -d ~/.local/bin ]] && PATH="${PATH}:${HOME}/.local/bin"

[[ -d ~/.config/nvim/bin ]] && PATH="${PATH}:~/.config/nvim/bin"
[[ -d ~/.emacs.d/bin ]] && PATH="${PATH}:~/.emacs.d/bin"

[[ -d ~/.meteor ]] && PATH="${PATH}:~/.meteor"

export PATH

# vim: ft=bash
