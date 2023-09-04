#!/usr/bin/env zsh
# Configuration related to bat.

# Check if bat exists in the first place
! command -v bat &> /dev/null && return

# Use bat as a colorizing pager for man
export MANROFFOPT='-c'
export MANPAGER="sh -c 'col -bx | bat --language=man --plain'"

# Interprets stdin as a help menu; displays it with highlighting
alias bathelp='bat --plain --language=help'

# Runs a command with the `--help` option and displays it using `bathelp`.
function help() {
		"$@" --help 2>&1 | bathelp
}

# `git diff`, but pretty.
function batdiff() {
		git diff --name-only --relative --diff-filter=d | xargs bat --diff
}

# vim: ft=zsh
