#!/usr/bin/env bash

# My editor depends on what's available on the system
if command -v nvim &> /dev/null ; then
	export VISUAL='nvim'
	export EDITOR='nvim'
elif command -v vim &> /dev/null ; then
	export VISUAL='vim'
	export EDITOR='vim'
fi

# If not running interactively, don't go further
[[ $- != *i* ]] && return

# Ensure essential directories and files exist
[[ ! -d ~/.cache/bash ]]         && mkdir -p ~/.cache/bash
[[ ! -f ~/.cache/bash/history ]] && touch ~/.cache/bash/history

# Export environmental variables
export HISTFILE=~/.cache/bash/history # Bash history file
export HISTSIZE=10000                 # History length
export HISTFILESIZE=10000             # History file length
export HISTCONTROL=ignoreboth         # Don't put duplicate lines in history

# Change some shell options
shopt -s histappend   # Append to history file
shopt -s autocd       # When given just a path/directory, cd into it
shopt -s checkwinsize # Check window size after each command

# Source some of my extra configurations scripts
[[ -f ~/.config/bash/alias.bashrc ]]  && . ~/.config/bash/alias.bashrc
[[ -f ~/.config/bash/path.bashrc ]]   && . ~/.config/bash/path.bashrc
[[ -f ~/.config/bash/prompt.bashrc ]] && . ~/.config/bash/prompt.bashrc
if [[ -d ~/.config/bash/extra ]] ; then
	for file in ~/.config/bash/extra/*.bashrc ; do
		# shellcheck source=/dev/null
		source "${file}"
	done
fi

# Source some common scripts I install
[[ -f /opt/conda/etc/profile.d/conda.sh ]]          && . /opt/conda/etc/profile.d/conda.sh
[[ -f /usr/share/bash-completion/bash_completion ]] && . /usr/share/bash-completion/bash_completion

# vim: ft=bash
