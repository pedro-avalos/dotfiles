#!/usr/bin/env zsh

setopt prompt_subst
autoload -Uz vcs_info
precmd_functions+=( vcs_info )

zstyle ':vcs_info:*' enable git
zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:*' get-revision true
zstyle ':vcs_info:*' formats '(%F{green}%b%f%u%c)'
zstyle ':vcs_info:*' actionformats '(%F{red}%m%f%u%c|%a)'

zstyle ':vcs_info:git:*' patch-format '(%10>...>%p%<<)'
zstyle ':vcs_info:git:*' stagedstr '%F{green}+%f'
zstyle ':vcs_info:git:*' unstagedstr '%F{red}*%f'
zstyle ':vcs_info:git*+set-message:*' hooks git-untracked

function +vi-git-untracked() {
		if [[ $(git rev-parse --is-inside-work-tree 2> /dev/null) == 'true' ]] && \
					 git status --porcelain | grep -q '^?? ' 2> /dev/null ; then
				hook_com[staged]+="%F{red}%%%f"
		fi
}

function +icon_ps1() {
    local exit=$?
    local ssh_icon='s'
    local tmux_icon='t'
    local norm_icon=''

    case "$#" in
				0|1|2|3)
						ssh_icon="${1:-${ssh_icon}}"
						tmux_icon="${2:-${tmux_icon}}"
						norm_icon="${3:-${norm_icon}}"
						;;
				*) return ${exit}
    esac

    if   [[ -n ${SSH_CONNECTION} ]] ; then printf -- '%s' "${ssh_icon}"
    elif [[ -n ${TMUX} ]]           ; then printf -- '%s' "${tmux_icon}"
    else                                   printf -- '%s' "${norm_icon}"
    fi
    return ${exit}
}

function +child_ps1() {
		local exit=$?
		local child_icon='z'
		local -i child_lvl=1

		case "$#" in
				0|1)
						child_icon="${1:${child_icon}}"
						;;
				*) return ${exit}
		esac

		[[ -n ${TMUX} ]] && child_lvl=2
		[[ ${SHLVL} -gt ${child_lvl} ]] && printf -- '%s' "${child_icon}"
		return ${exit}
}

function +pre_vcs() {
		local root_color='%F{red}'
		local ssh_color='%F{magenta}'
		local tmux_color='%F{green}'
		local norm_color='%F{blue}'
		local child_color='%F{cyan}'

		local ssh_icon=''
		local tmux_icon=''
		local norm_icon=''
		local child_icon=''

		if [[ ${EUID} -eq 0 ]] ; then
				ssh_icon+="${root_color}Σ"
				tmux_icon+="${root_color}Τ"
				norm_icon+="${root_color}Λ"
				child_icon+="${root_color}Ζ"
		else
				ssh_icon+="${ssh_color}σ"
				tmux_icon+="${tmux_color}τ"
				norm_icon+="${norm_color}λ"
				child_icon+="${child_color}ζ"
		fi
		ssh_icon+='%f '
		tmux_icon+='%f '
		norm_icon+='%f '
		child_icon+='%f '

		local icon=$(+icon_ps1 "${ssh_icon}" "${tmux_icon}" "${norm_icon}")
		local child=$(+child_ps1 "${child_icon}")

		local out="${icon}${child}"

		out+='%n@%m:'

		if [[ ${EUID} -eq 0 ]]          ; then out+="${root_color}"
		elif [[ -n ${SSH_CONNECTION} ]] ; then out+="${ssh_color}"
		elif [[ -n ${TMUX} ]]           ; then out+="${tmux_color}"
		else                                   out+="${norm_color}"
		fi
		out+='%1~%f'

		printf -- '%s' "${out}"
}

function +post_vcs() {
		local code='%(?..%F{red}[%?]%f)'

		printf -- '%s' "${code}"
}

PROMPT='$(+pre_vcs)${vcs_info_msg_0_}$(+post_vcs) %E'

# vim: ft=zsh
