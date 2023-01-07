#!/usr/bin/env bash
# File: .bashrc

# If not running interactively, don't do anything
if [[ $- != *i* ]] ; then
  return
fi

# Source global definitions
if [[ -e /etc/bashrc ]] ; then
  source /etc/bashrc
fi

# Ensure essential directories and files exist
# Bash history parent directory
if [[ ! -d ~/.cache/bash ]] ; then
  mkdir -p ~/.cache/bash
fi
# Bash history file
if [[ ! -f ${HISTFILE} ]] ; then
  touch ${HISTFILE}
fi

# Export environmental variables
export HISTFILE=~/.cache/bash/history # Bash history file
export HISTSIZE=10000                 # History length
export HISTFILESIZE=10000             # History file length
export HISTCONTROL=ignoreboth         # Don't put duplicate lines in history

export GPG_TTY=$(tty)

# Change some shell settings
shopt -s histappend   # Append to history file
shopt -s autocd       # When given just a path/directory, cd into it
shopt -s checkwinsize # Check window size after each command

# Source personal configuration files
if [[ -d ~/.bashrc.d ]] ; then
  for file in ~/.bashrc.d/*.bashrc ; do
    source "${file}"
  done
fi

# Enable completion features
if [[ -e /usr/share/bash-completion/bash_completion ]] ; then
  source /usr/share/bash-completion/bash_completion
fi

# vim: ft=bash
