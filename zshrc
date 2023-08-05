#!/usr/bin/env zsh

# Enable colors
autoload -U colors && colors

# Ensure essential directories and files exist
[[ ! -d ~/.cache/zsh ]] && mkdir -p ~/.cache/zsh

HISTFILE=~/.cache/zsh/history
HISTSIZE=10000
SAVEHIST=10000

# Shell options
setopt histignorealldups beep autocd extendedglob nomatch
unsetopt notify

# Completion
autoload -Uz compinit
compinit

# Keybindings
bindkey -v # Use vi-style keybindings

source ~/.config/zsh/alias.zsh
source ~/.config/zsh/prompt.zsh

# vim: ft=zsh
