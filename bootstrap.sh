#!/usr/bin/env bash
# Bootstraps my dotfiles
# Inspired by https://github.com/mathiasbynens/dotfiles

# Show help menu
usage ()
{
    1>&2 printf -- "Usage: %s [-hfx]\n" "$0"
    1>&2 printf -- "\t-h: Show help menu\n"
    1>&2 printf -- "\t-f: Force install\n"
    1>&2 printf -- "\t-x: Install codium extensions\n"
}

# Default option values
unset FORCE CODIUM_EXTENSIONS
cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1
pwd

# Parse command-line options
while getopts "hfx" opt ; do
    case "${opt}" in
        f)
            FORCE=1
            ;;
        x)
            CODIUM_EXTENSIONS=1
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
        --exclude "**/.pre-commit-config.yaml" \
        --exclude "**/.vscode/" \
        --exclude "**/README.md" \
        --exclude "**/LICENSE" \
        --exclude "**/.mypy_cache" \
        --exclude "**/.ruff_cache" \
        --exclude "bootstrap.sh" \
        --exclude ".config/VSCodium/extensions.txt" \
        -avgh --no-perms . "${HOME}"

    if [[ "${CODIUM_EXTENSIONS}" ]] ; then
        if command -v codium > /dev/null ; then
            echo -e "\nInstalling VSCodium extensions"
            while IFS= read -r line ; do
                echo "${line}"
                codium --install-extension "${line}" > /dev/null
            done < <(grep -v '^ *#' < .config/VSCodium/extensions.txt)
        else
            echo -e "\nVSCodium is not installed"
        fi
    fi

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

unset CODIUM_EXTENSIONS FORCE rsync_dots

# vim: ft=bash
