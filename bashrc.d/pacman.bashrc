#!/usr/bin/env bash
# File: pacman.bashrc
# Configuration related to pacman.

alias pacref='sudo pacman -Syy'                # Refresh repos
alias pacup='sudo pacman -Syu'                 # Update
alias pacse='pacman -Ss'                       # Search in repos
alias pacif='pacman -Si'                       # Get info on repo package
alias pacin='sudo pacman -S --needed'          # Install from repos
alias pacrm='sudo pacman -Rs'                  # Remove a package
alias paccl='sudo pacman -Rns $(pacman -Qtdq)' # Remove orphans

# vim: ft=bash