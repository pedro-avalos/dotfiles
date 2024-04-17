#!/usr/bin/env bash

export XDG_CONFIG_HOME="${XDG_CONFIG_HOME:=$HOME/.config}"
export XDG_DATA_HOME="${XDG_DATA_HOME:=$HOME/.local/share}"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:=$HOME/.cache}"
export XDG_STATE_HOME="${XDG_STATE_HOME:=$HOME/.local/state}"
export XDG_DATA_DIRS="${XDG_DATA_DIRS}:/var/lib/snapd/desktop/"
export VISUAL='vim'
export EDITOR='vim'
export SUDO_EDITOR='vim'

# If not running interactively, don't go further
[[ $- != *i* ]] && return

[[ ! -d "${XDG_CACHE_HOME}/bash" ]] && mkdir -p "${XDG_CACHE_HOME}/bash"
export HISTFILE="${XDG_CACHE_HOME}/bash/history"
export HISTSIZE=10000
export HISTFILESIZE=10000
export HISTCONTROL=ignoreboth

shopt -s histappend autocd checkwinsize

if [[ -f "${XDG_CONFIG_HOME}/bash/alias.bashrc" ]] ; then
	source "${XDG_CONFIG_HOME}/bash/alias.bashrc"
fi
if [[ -f "${XDG_CONFIG_HOME}/bash/path.bashrc" ]] ; then
	source "${XDG_CONFIG_HOME}/bash/path.bashrc"
fi
if [[ -f "${XDG_CONFIG_HOME}/bash/prompt.bashrc" ]] ; then
	source "${XDG_CONFIG_HOME}/bash/prompt.bashrc"
fi
if [[ -d "${XDG_CONFIG_HOME}/bash/extra" ]] ; then
		for file in ${XDG_CONFIG_HOME}/bash/extra/*.bashrc ; do
			source "${file}"
		done
fi

# Use bash-completion, if available
if [[ ${PS1} && -f /usr/share/bash-completion/bash_completion ]] ; then
		source /usr/share/bash-completion/bash_completion
fi

# vim: ft=bash
