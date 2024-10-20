#!/usr/bin/env bash
# Bootstraps my dotfiles
# Inspired by https://github.com/mathiasbynens/dotfiles

# Show help menu
usage ()
{
    1>&2 printf -- "Usage: %s [-hf]\n" "$0"
    1>&2 printf -- "\t-h: Show help menu\n"
    1>&2 printf -- "\t-f: Force install\n"
}

# Default option values
unset FORCE
cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1
pwd

# Parse command-line options
while getopts "hfd:" opt ; do
    case "${opt}" in
        f)
            FORCE=1
            ;;
        h)
            usage
            exit 0
            ;;
        *)
            usage
            exit 1
            ;;
    esac
done

# Helper function to sync dotfiles
rsync_dots ()
{
    rsync --exclude "**/.git/" \
        --exclude "**/.gitmodules" \
        --exclude "**/.git" \
        --exclude "**/.gitignore" \
        --exclude "**/.gitlab-ci.yml" \
        --exclude "**/.vscode/" \
        --exclude "**/README.md" \
        --exclude "**/LICENSE" \
        --exclude "**/.mypy_cache" \
        --exclude "**/.ruff_cache" \
        --exclude "bootstrap.sh" \
        -avgh --no-perms . "${HOME}"
        
    source "${HOME}/.bash_profile"
}

# Update repository
git pull --recurse-submodules

if [[ "${FORCE}" ]] ; then
    rsync_dots
else
    read -r -p "This may overwrite the existing configuration. Are you sure? [y/N] " -n 1
    echo
    if [[ "${REPLY}" =~ ^[Yy]$ ]] ; then
        rsync_dots
    else
        exit 1
    fi
fi

unset FORCE
unset rsync_dots

# vim: ft=bash
