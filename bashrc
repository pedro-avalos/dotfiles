#!/usr/bin/env bash
# File: .bashrc

# Source global definitions
if [[ -e /etc/bashrc ]] ; then
  source /etc/bashrc
fi

export HISTSIZE=10000
export HISTFILESIZE=${HISTSIZE}
export HISTCONTROL=ignoreboth

# If not running interactively, don't do anything
if [[ $- != *i* ]] ; then
  return
fi

# Source external configuration files
if [[ -e /usr/share/bash-completion/bash_completion ]] ; then
  source /usr/share/bash-completion/bash_completion
fi

# Change some shell settings
shopt -s autocd       # When given just a path/directory, cd into it
shopt -s checkwinsize # Check window size after each command

# Source personal configuration files
if [[ -d ~/.bashrc.d ]] ; then
  for file in ~/.bashrc.d/*.bashrc ; do
    source "${file}"
  done
fi

# vim: ft=bash