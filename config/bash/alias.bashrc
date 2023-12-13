#!/usr/bin/env bash

# Root aliases
if [[ ${EUID} -eq 0 ]] ; then
		alias rm='rm -i'
		alias cp='cp -i'
		alias mv='mv -i'
fi

# Reload bash configuration
alias resource='source ~/.bashrc'

# Commands
alias ls='ls --color=auto -F'
alias l='ls --color=auto -lh'
alias la='ls --color=auto -a'
alias ll='ls --color=auto -lha'
alias grep='grep --color=auto'
alias egrep='grep --color=auto -E'
alias fgrep='grep --color=auto -F'
alias diff='diff --color=auto'
alias ip='ip --color=auto'

# Editor-related aliases
alias emacs_tui='emacsclient -ta ""'
alias emacs_gui='emacsclient -ca emacs'

# Fun stuff
alias tuxsay='cowsay -f tux'
alias nfetch='neofetch'

# vim: ft=bash
