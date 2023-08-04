#!/usr/bin/env bash
# Configuration related to pacman and paru.

# Check if pacman exists in the first place
if command -v pacman &> /dev/null ; then
  alias pacref='sudo pacman -Syy'                # Refresh repos
  alias pacup='sudo pacman -Syu'                 # Update
  alias pacse='pacman -Ss'                       # Search in repos
  alias pacif='pacman -Si'                       # Get info on repo package
  alias pacin='sudo pacman -S --needed'          # Install from repos
  alias pacrm='sudo pacman -Rs'                  # Remove a package
  alias paccl='sudo pacman -Rns $(pacman -Qtdq)' # Remove orphans
fi

# Check if paru exists in the first place
if command -v paru &> /dev/null ; then
  alias paruref='paru -Syy'              # Refresh repos
  alias paruup='paru -Syu'               # Update
  alias paruse='paru -Ss'                # Search in AUR+repos
  alias paruif='paru -Si'                # Get info on a package
  alias paruin='paru -S --needed'        # Install from AUR+repos
  alias parurm='paru -Rs'                # Remove a package
  alias parucl='paru -Rns $(paru -Qtdq)' # Remove orphans
fi

# vim: ft=bash
