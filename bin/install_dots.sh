#!/usr/bin/env sh
# File: install_dots.sh

# Update dotfiles
git -C ~/.dotfiles pull

# Install dotfiles executables and scripts
ln -bsf ~/.dotfiles/bin ~/.bin

# Install bash dotfiles
ln -bsf ~/.dotfiles/bashrc       ~/.bashrc
ln -bsf ~/.dotfiles/bashrc.d     ~/.bashrc.d
ln -bsf ~/.dotfiles/bash_profile ~/.bash_profile
ln -bsf ~/.dotfiles/bash_logout  ~/.bash_logout

# Install tmux dotfiles
ln -bsf ~/.dotfiles/config/tmux  ~/.config/tmux
ln -bsf ~/.dotfiles/config/tmuxp ~/.config/tmuxp
