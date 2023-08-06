#!/usr/bin/env zsh

typeset -U path PATH

[[ -d ~/bin ]]        && path+=( ~/bin )
[[ -d ~/.bin ]]       && path+=( ~/.bin )
[[ -d ~/.local/bin ]] && path+=( ~/.local/bin )

[[ -d ~/.config/nvim/bin ]]  && path+=( ~/.config/nvim/bin )
[[ -d ~/.config/emacs/bin ]] && path+=( ~/.config/emacs/bin )

export PATH

# vim: ft=zsh
