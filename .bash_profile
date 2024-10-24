#!/usr/bin/env bash

export XDG_CONFIG_HOME="${XDG_CONFIG_HOME:=$HOME/.config}"
export XDG_DATA_HOME="${XDG_DATA_HOME:=$HOME/.local/share}"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:=$HOME/.cache}"
export XDG_STATE_HOME="${XDG_STATE_HOME:=$HOME/.local/state}"
export VISUAL='vim'
export EDITOR='vim'
export SUDO_EDITOR='vim'

mkdir -p "${XDG_CACHE_HOME}/bash"
export HISTFILE="${XDG_CACHE_HOME}/bash/history"
export HISTSIZE=1000
export HISTFILESIZE=2000
export HISTCONTROL=ignoreboth

[[ -d "${HOME}/bin" ]]        && PATH="${PATH}:${HOME}/bin"
[[ -d "${HOME}/.bin" ]]       && PATH="${PATH}:${HOME}/.bin"
[[ -d "${HOME}/.local/bin" ]] && PATH="${PATH}:${HOME}/.local/bin"
[[ -d "${HOME}/.meteor" ]]    && PATH="${PATH}:${HOME}/.meteor"

export PATH

# Source bashrc if in interactive shell
if [[ -n "${BASH_VERSION}" && -n "${PS1}" ]] ; then
	if [[ -f "${HOME}/.bashrc" ]] ; then
		source "${HOME}/.bashrc"
	fi
fi

# vim: ft=bash
