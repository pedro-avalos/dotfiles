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

shopt -s histappend autocd checkwinsize

source "${HOME}/.bash_aliases"
source "${XDG_CONFIG_HOME}/bash/bat.bashrc"
source "${XDG_CONFIG_HOME}/bash/pacman.bashrc"
source "${XDG_CONFIG_HOME}/bash/prompt.bashrc"

# Use bash-completion, if available
if ! shopt -oq posix; then
	if [[ -f /usr/share/bash-completion/bash_completion ]] ; then
		source /usr/share/bash-completion/bash_completion
	elif [[ -f /etc/bash_completion ]] ; then
		source /etc/bash_completion
	fi
fi

# vim: ft=bash
