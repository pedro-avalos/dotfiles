#!/usr/bin/env bash
# Configuration related to bat.

# Depending on distribution, the command may be different
bat_cmd="bat"
if [[ -f "/etc/debian_version" ]] ; then
	bat_cmd="batcat"
fi

# Check if bat exists in the first place
! command -v "${bat_cmd}" &> /dev/null && return

# Use bat for man pages
export MANROFFOPT='-c'
export MANPAGER="sh -c 'col -bx | ${bat_cmd} --language=man --plain'"

# Interprets stdin as a help menu; displays it with highlighting
alias bathelp="${bat_cmd} --plain --language=help"

# Runs a command with the `--help` option and displays it using `bathelp`
function help() {
	"$@" --help 2>&1 | bathelp
}

# `git diff`, but pretty
function batdiff() {
	git diff --name-only --relative --diff-filter=d | xargs ${bat_cmd} --diff
}

# vim: ft=bash
