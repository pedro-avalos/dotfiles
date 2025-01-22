#!/usr/bin/env bash

export XDG_CONFIG_HOME="${XDG_CONFIG_HOME:=$HOME/.config}"
export XDG_DATA_HOME="${XDG_DATA_HOME:=$HOME/.local/share}"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:=$HOME/.cache}"
export XDG_STATE_HOME="${XDG_STATE_HOME:=$HOME/.local/state}"

# GitHub CLI completion
eval "$(gh completion -s bash)"

# Source bashrc if in interactive shell
if [[ -n "${BASH_VERSION}" && -n "${PS1}" ]] ; then
	if [[ -f "${HOME}/.bashrc" ]] ; then
		# shellcheck source=.bashrc
		source "${HOME}/.bashrc"
	fi
fi

# vim: ft=bash
