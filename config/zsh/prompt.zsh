#!/usr/bin/env zsh

setopt prompt_subst
autoload -Uz vcs_info

zstyle ':vcs_info:*' enable git
zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:*' get-revision true
zstyle ':vcs_info:*' formats \
  '(%{%F{green}%}%b%{%f%}%u%c)'
zstyle ':vcs_info:*' actionformats \
  '(%{%F{red}%}%m%{%f%}%u%c|%a)'

zstyle ':vcs_info:git:*' patch-format '(%10>...>%p%<<)'
zstyle ':vcs_info:git:*' stagedstr '%{%F{green}%}+%{%f%}'
zstyle ':vcs_info:git:*' unstagedstr '%{%F{red}%}*%{%f%}'

precmd_vcs_info() { vcs_info }
precmd_functions+=( precmd_vcs_info )

# TODO: Add icon and colors like in my bashrc
PROMPT='%n@%m:%1~${vcs_info_msg_0_} %{%f%E%}'

# vim: ft=zsh
