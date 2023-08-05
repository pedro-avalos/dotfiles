#!/usr/bin/env bash

# Needed for git repo status
# shellcheck source=./git-prompt.sh
[[ -f ~/.config/bash/git-prompt.sh ]] && . ~/.config/bash/git-prompt.sh

# Settings for git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1     # '*'=unstaged, '+'=staged
export GIT_PS1_SHOWSTASHSTATE=1     # '$'=stashed
export GIT_PS1_SHOWUNTRACKEDFILES=1 # '%'=untracked
export GIT_PS1_STATESEPARATOR=''    # No space betweend branch and index status

# Check if the terminal supports colors
function __color_enabled() {
  local exit=$?
  local -i colors
  colors=$(tput colors 2> /dev/null)
  [[ ${exit} -eq 0 ]] && [[ ${colors} -gt 2 ]]
}

# Whether to use colors in the prompt
unset __colorize_prompt && __color_enabled && __colorize_prompt=1

# Main icon to the left side of the prompt.
# It will differ depending on whether the shell is running under ssh or tmux.
# This function takes up to three arguments (ssh_icon, tmux_icon, norm_icon).
function __icon_ps1() {
  local exit=$?       # Exit status
  local ssh_icon='s'  # Icon for ssh connection
  local tmux_icon='t' # Icon for tmux shell
  local norm_icon=''  # Icon normally

  case "$#" in
    0|1|2|3)
      ssh_icon="${1:-${ssh_icon}}"
      tmux_icon="${2:-${tmux_icon}}"
      norm_icon="${3:-${norm_icon}}"
      ;;
    *) return ${exit}
  esac

  # Display the appropriate icon
  if   [[ -n ${SSH_CONNECTION} ]] ; then printf -- '%s' "${ssh_icon}"
  elif [[ -n ${TMUX} ]]           ; then printf -- '%s' "${tmux_icon}"
  else                                   printf -- '%s' "${norm_icon}"
  fi

  return ${exit}
}

# Icon for a child shell instance.
# This function takes up one argument (child_icon).
function __child_ps1() {
  local exit=$?        # Exit status
  local child_icon='b' # Icon to display
  local -i child_lvl=1 # What level is required to consider this a child

  case "$#" in
    0|1)
      child_icon="${1:${child_icon}}"
      ;;
    *) return ${exit}
  esac

  # Increase child shell requirement to 2 in case tmux is being used
  [[ -n ${TMUX} ]] && child_lvl=2

  # Display child shell icon
  [[ ${SHLVL} -gt ${child_lvl} ]] && printf -- '%s' "${child_icon}"

  return ${exit}
}

# Create the bash prompt.
function __set_ps1() {
  local exit=$?

  # Colors      ; Bright colors
  local black   ; local bblack
  local red     ; local bred
  local green   ; local bgreen
  local yellow  ; local byellow
  local blue    ; local bblue
  local magenta ; local bmagenta
  local cyan    ; local bcyan
  local white   ; local bwhite
  local bold
  local blink
  local sgr0

  if [[ ${__colorize_prompt} ]] ; then
    export GIT_PS1_SHOWCOLORHINTS=1

    black="\[$(tput setaf 0)\]"   ; bblack="\[$(tput setaf 8)\]"
    red="\[$(tput setaf 1)\]"     ; bred="\[$(tput setaf 9)\]"
    green="\[$(tput setaf 2)\]"   ; bgreen="\[$(tput setaf 10)\]"
    yellow="\[$(tput setaf 3)\]"  ; byellow="\[$(tput setaf 11)\]"
    blue="\[$(tput setaf 4)\]"    ; bblue="\[$(tput setaf 12)\]"
    magenta="\[$(tput setaf 5)\]" ; bmagenta="\[$(tput setaf 13)\]"
    cyan="\[$(tput setaf 6)\]"    ; bcyan="\[$(tput setaf 14)\]"
    white="\[$(tput setaf 7)\]"   ; bwhite="\[$(tput setaf 15)\]"
    bold="\[$(tput bold)\]"
    blink="\[$(tput blink)\]"
    sgr0="\[$(tput sgr0)\]"
  else
    unset GIT_PS1_SHOWCOLORHINTS
  fi

  # Colors for each situation
  local root_color="${bold}${red}"
  local ssh_color="${magenta}"
  local tmux_color="${green}"
  local norm_color="${blue}"
  local child_color="${cyan}"

  # Set up pre_ps1
  local ssh_icon=''   # Icon for ssh connection
  local tmux_icon=''  # Icon for tmux shell
  local norm_icon=''  # Icon for local shell
  local child_icon='' # Icon for child shell

  # Set up icons and their color
  if [[ ${EUID} -eq 0 ]] ; then
    ssh_icon+="${root_color}Σ"
    tmux_icon+="${root_color}Τ"
    norm_icon+="${root_color}Λ"
    child_icon+="${root_color}Β"
  else
    ssh_icon+="${ssh_color}σ"
    tmux_icon+="${tmux_color}τ"
    norm_icon+="${norm_color}λ"
    child_icon+="${child_color}β"
  fi
  ssh_icon+="${sgr0} "
  tmux_icon+="${sgr0} "
  norm_icon+="${sgr0} "
  child_icon+="${sgr0} "

  local icon_ps1
  local child_ps1

  icon_ps1=$(__icon_ps1 "${ssh_icon}" "${tmux_icon}" "${norm_icon}")
  child_ps1=$(__child_ps1 "${child_icon}")

  local pre_ps1="${icon_ps1}${child_ps1}"

  # If root, make the following bold
  # Show the user and host: `<user>@<host>:`
  [[ ${EUID} -eq 0 ]] && pre_ps1+="${bold}"
  pre_ps1+='\u@\h:'
  [[ ${EUID} -eq 0 ]] && pre_ps1+="${sgr0}"

  # Add the current directory (color matched to icon)
  pre_ps1+="${_bold}"
  if   [[ ${EUID} -eq 0 ]]        ; then pre_ps1+="${root_color}"
  elif [[ -n ${SSH_CONNECTION} ]] ; then pre_ps1+="${ssh_color}"
  elif [[ -n ${TMUX} ]]           ; then pre_ps1+="${tmux_color}"
  else                                   pre_ps1+="${norm_color}"
  fi
  pre_ps1+="\W${sgr0}"

  # Set up post_ps1
  local post_ps1
  post_ps1=''

  # If nonzero exit code, display it in red
  [[ ${exit} -ne 0 ]] && post_ps1+="${red}[${exit}]${sgr0}"

  post_ps1+=' '

  __git_ps1 "${pre_ps1}" "${post_ps1}" '(%s)'
}

export PROMPT_COMMAND=__set_ps1

# vim: ft=bash
