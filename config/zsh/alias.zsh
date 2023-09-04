#!/usr/bin/env zsh

# Reload zsh configuration
alias resource='source $ZDOTDIR/.zshrc'

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
alias vi='vim'

# Fun stuff
alias tuxsay='cowsay -f tux'
alias nfetch='neofetch'

# vim: ft=zsh
