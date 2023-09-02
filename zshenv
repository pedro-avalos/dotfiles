export XDG_CONFIG_HOME=$HOME/.config
export XDG_DATA_HOME=$HOME/.local/share
export XDG_CACHE_HOME=$HOME/.cache
export XDG_STATE_HOME=$HOME/.local/state

typeset -U path PATH
path+=(~/bin ~/.bin ~/.local/bin)
path+=($XDG_CONFIG_HOME/bin $XDG_CONFIG_HOME/emacs/bin)
export PATH

# vim: ft=zsh
