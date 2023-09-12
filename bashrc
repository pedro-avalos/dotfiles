#!/usr/bin/env bash

export XDG_CONFIG_HOME="${XDG_CONFIG_HOME:=$HOME/.config}"
export XDG_DATA_HOME="${XDG_DATA_HOME:=$HOME/.local/share}"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:=$HOME/.cache}"
export XDG_STATE_HOME="${XDG_STATE_HOME:=$HOME/.local/state}"
export VISUAL='emacs'
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

# Source some of my extra configurations scripts
[[ -f ~/.config/bash/alias.bashrc ]]  && . ~/.config/bash/alias.bashrc
[[ -f ~/.config/bash/path.bashrc ]]   && . ~/.config/bash/path.bashrc
[[ -f ~/.config/bash/prompt.bashrc ]] && . ~/.config/bash/prompt.bashrc
if [[ -d ~/.config/bash/extra ]] ; then
		for file in ~/.config/bash/extra/*.bashrc ; do source "${file}" ; done
fi

# Use bash-completion, if available
if [[ $PS1 && -f /usr/share/bash-completion/bash_completion ]] ; then
		source /usr/share/bash-completion/bash_completion
fi

# vim: ft=bash
