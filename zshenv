#!/usr/bin/env zsh

export XDG_CONFIG_HOME="${XDG_CONFIG_HOME:=$HOME/.config}"
export XDG_DATA_HOME="${XDG_DATA_HOME:=$HOME/.local/share}"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:=$HOME/.cache}"
export XDG_STATE_HOME="${XDG_STATE_HOME:=$HOME/.local/state}"
export VISUAL=vim
export EDITOR=vim
export SUDO_EDITOR=vim

typeset -U path PATH
path+=($HOME/bin $HOME/.bin $HOME/.local/bin)
path+=($XDG_CONFIG_HOME/nvim/bin $XDG_CONFIG_HOME/emacs/bin)
export PATH

typeset -U xdg_data_dirs XDG_DATA_DIRS
path+=(/var/lib/snapd/desktop)
export XDG_DATA_DIRS

export ZDOTDIR="${ZDOTDIR:=$XDG_CONFIG_HOME/zsh}"

# vim: ft=zsh
