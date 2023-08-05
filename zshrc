#!/usr/bin/env zsh

[[ ! -d ~/.cache/zsh ]] && mkdir -p ~/.cache/zsh

HISTFILE=~/.cache/zsh/history
HISTSIZE=10000
SAVEHIST=10000

setopt histignorealldups beep autocd extendedglob nomatch
unsetopt notify

autoload -U colors && colors
autoload -Uz compinit && compinit

bindkey -v

source ~/.config/zsh/alias.zsh
source ~/.config/zsh/prompt.zsh

# vim: ft=zsh
