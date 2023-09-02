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
for f in ~/.config/zsh/extra/*.zsh ; do source $f ; done

if [[ -f /opt/conda/etc/profile.d/conda.sh ]] ; then . /opt/conda/etc/profile.d/conda.sh ; fi

# vim: ft=zsh
