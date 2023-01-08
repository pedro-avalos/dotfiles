#!/usr/bin/env bash
# File: .bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Ensure essential directories and files exist
[[ ! -d ~/.cache/bash ]]         && mkdir -p ~/.cache/bash
[[ ! -f ~/.cache/bash/history ]] && touch ~/.cache/bash/history

GPG_TTY=$(tty)

# Export environmental variables
export HISTFILE=~/.cache/bash/history # Bash history file
export HISTSIZE=10000                 # History length
export HISTFILESIZE=10000             # History file length
export HISTCONTROL=ignoreboth         # Don't put duplicate lines in history
export GPG_TTY                        # Makes GPG passphrase prompts work

# Change some shell options
shopt -s histappend   # Append to history file
shopt -s autocd       # When given just a path/directory, cd into it
shopt -s checkwinsize # Check window size after each command

# Source personal configuration files
if [[ -d ~/.bashrc.d ]] ; then
  for file in ~/.bashrc.d/*.bashrc ; do
    # shellcheck source=/dev/null
    source "${file}"
  done
fi

# Enable completion features
[[ -e /usr/share/bash-completion/bash_completion ]] &&
  source /usr/share/bash-completion/bash_completion

# vim: ft=bash
