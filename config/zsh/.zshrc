#!/usr/bin/env zsh

if [[ ! -d $XDG_CACHE_HOME/zsh ]] ; then mkdir -p $XDG_CACHE_HOME/zsh ; fi
HISTFILE=$XDG_CACHE_HOME/zsh/history
HISTSIZE=10000
SAVEHIST=10000

setopt histignorealldups beep autocd extendedglob nomatch
unsetopt notify

autoload -U colors && colors
autoload -Uz compinit && compinit

bindkey -v

export EDITOR=emacs
export SUDOEDITOR=emacs
export VISUAL=emacs

source $ZDOTDIR/alias.zsh
source $ZDOTDIR/prompt.zsh
for f in $ZDOTDIR/extra/*.zsh ; do source $f ; done

# vim: ft=zsh
