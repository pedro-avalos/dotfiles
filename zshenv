#!/usr/bin/env zsh

export XDG_CONFIG_HOME="${XDG_CONFIG_HOME:=$HOME/.config}"
export XDG_DATA_HOME="${XDG_DATA_HOME:=$HOME/.local/share}"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:=$HOME/.cache}"
export XDG_STATE_HOME="${XDG_STATE_HOME:=$HOME/.local/state}"

typeset -U path PATH
path+=($HOME/bin $HOME/.bin $HOME/.local/bin)
path+=($XDG_CONFIG_HOME/bin $XDG_CONFIG_HOME/emacs/bin)
export PATH

export ZDOTDIR="${ZDOTDIR:=$XDG_CONFIG_HOME/zsh}"

# vim: ft=zsh
