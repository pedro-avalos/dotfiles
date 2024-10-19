#!/usr/bin/env bash

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
