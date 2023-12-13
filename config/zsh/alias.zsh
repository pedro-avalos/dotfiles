#!/usr/bin/env zsh

# Reload zsh configuration
alias resource='source $ZDOTDIR/.zshrc'

# Directory-related aliases
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
alias vi='vim'

# Fun stuff
alias tuxsay='cowsay -f tux'
alias nfetch='neofetch'

# vim: ft=zsh
