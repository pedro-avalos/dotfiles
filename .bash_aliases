#!/usr/bin/env bash
# Set up common aliases

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
alias l='ls --color=auto -CF'
alias la='ls --color=auto -A'
alias ll='ls --color=auto -alF'
alias grep='grep --color=auto'
alias egrep='grep --color=auto -E'
alias fgrep='grep --color=auto -F'
alias diff='diff --color=auto'
alias ip='ip --color=auto'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Editor-related aliases
alias emacs_tui='emacsclient -ta ""'
alias emacs_gui='emacsclient -ca emacs'

# Fun stuff
alias tuxsay='cowsay -f tux'
alias nfetch='neofetch'

# vim: ft=bash
