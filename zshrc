#!/usr/bin/env zsh
# File: .zshrc

# Enable colors
autoload -U colors && colors

# Ensure essential directories and files exist
[[ ! -d ~/.cache/zsh ]]         && mkdir -p ~/.cache/zsh
[[ ! -f ~/.cache/zsh/history ]] && touch ~/.cache/zsh/history

GPG_TTY=$(tty)

HISTFILE=~/.cache/zsh/history
HISTSIZE=10000
SAVEHIST=10000

# Shell options
setopt histignorealldups # Substitute commands in the prompt
setopt beep              # Make a beep noise
setopt autocd            # Assume `cd` if command is only directory
setopt promptsubst       # Required for git plugin
setopt extendedglob      #
setopt nomatch           #
unsetopt notify          # Notify after a command, not immediately

# Completion
autoload -Uz compinit
compinit

# Keybindings
bindkey -v # Use vi-style keybindings

# vim: ft=zsh
