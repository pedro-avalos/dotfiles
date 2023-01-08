#!/usr/bin/env sh
# File: install_dots.sh

# Update dotfiles
git -C ~/.dotfiles pull

# Ensure directories exist
[ ! -d ~/.config ] && mkdir ~/.config

# Install dotfiles executables and scripts
ln -sf ~/.dotfiles/bin ~/.bin

# Install keybindings
ln -sf ~/.dotfiles/inputrc ~/.inputrc

# Install bash dotfiles
ln -sf ~/.dotfiles/bashrc       ~/.bashrc
ln -sf ~/.dotfiles/bashrc.d     ~/.bashrc.d
ln -sf ~/.dotfiles/bash_profile ~/.bash_profile
ln -sf ~/.dotfiles/bash_logout  ~/.bash_logout

# Install tmux dotfiles
ln -sf ~/.dotfiles/config/tmux  ~/.config/tmux
ln -sf ~/.dotfiles/config/tmuxp ~/.config/tmuxp
