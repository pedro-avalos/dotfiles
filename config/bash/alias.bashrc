#!/usr/bin/env bash

# Root aliases
if [[ ${EUID} -eq 0 ]] ; then
	alias rm='rm -i'
	alias cp='cp -i'
	alias mv='mv -i'
fi

# Reload bash configuration
alias resource='source ~/.bashrc'

# Directory-related aliases
alias ls='ls --color=auto -F'
alias l='ls --color=auto -lh'
alias la='ls --color=auto -a'
alias ll='ls --color=auto -lha'

# Grep-related aliases
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# Editor-related aliases
alias emacs_tui='emacsclient -ta ""'
alias emacs_gui='emacsclient -ca emacs'
if command -v nvim &> /dev/null ; then # neovim is available
  alias vi='nvim'
  alias vim='nvim'
  alias diff='nvim -d'
elif command -v vim &> /dev/null ; then # vim is available
  alias vi='vim'
  alias diff='vim -d'
fi

# Fun stuff
alias tuxsay='cowsay -f tux'
alias nfetch='neofetch'

# vim: ft=bash
