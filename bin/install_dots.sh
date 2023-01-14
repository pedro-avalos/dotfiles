#!/usr/bin/env sh
# File: install_dots.sh

# Update dotfiles
git -C ~/.dotfiles pull

# Ensure directories exist
[ ! -d ~/.config ] && mkdir ~/.config

# Install dotfiles executables and scripts
ln -Tsf ~/.dotfiles/bin ~/.bin

# Install keybindings
ln -Tsf ~/.dotfiles/inputrc ~/.inputrc

# Install bash dotfiles
ln -Tsf ~/.dotfiles/bashrc       ~/.bashrc
ln -Tsf ~/.dotfiles/bashrc.d     ~/.bashrc.d
ln -Tsf ~/.dotfiles/bash_profile ~/.bash_profile
ln -Tsf ~/.dotfiles/bash_logout  ~/.bash_logout

# Install tmux dotfiles
ln -Tsf ~/.dotfiles/config/tmux  ~/.config/tmux
ln -Tsf ~/.dotfiles/config/tmuxp ~/.config/tmuxp

# Install redshift dotfiles
ln -Tsf ~/.dotfiles/config/redshift.conf ~/.config/redshift.conf

# Install qtile dotfiles
ln -Tsf ~/.dotfiles/config/qtile ~/.config/qtile

