#!/usr/bin/env sh
# File: install_dots.sh

# Update dotfiles
git -C ~/.dotfiles pull

# Ensure directories exist
echo "ensuring directories exist..."
[ ! -d ~/.config ] && mkdir ~/.config

# Install dotfiles executables and scripts
echo "installing dots scripts..."
ln -Tsf ~/.dotfiles/bin ~/.bin

# Install keybindings
echo "installing inputrc dots..."
ln -Tsf ~/.dotfiles/inputrc ~/.inputrc

# Install bash dotfiles
echo "installing bash dots..."
ln -Tsf ~/.dotfiles/bashrc       ~/.bashrc
ln -Tsf ~/.dotfiles/bashrc.d     ~/.bashrc.d
ln -Tsf ~/.dotfiles/bash_profile ~/.bash_profile
ln -Tsf ~/.dotfiles/bash_logout  ~/.bash_logout

# Install tmux dotfiles
echo "installing tmux dots..."
ln -Tsf ~/.dotfiles/config/tmux  ~/.config/tmux
ln -Tsf ~/.dotfiles/config/tmuxp ~/.config/tmuxp

# Install gtk dotfiles
echo "installing gtk dots..."
ln -Tsf ~/.dotfiles/config/gtk-3.0 ~/.config/gtk-3.0

# Install redshift dotfiles
echo "installing redshift dots..."
ln -Tsf ~/.dotfiles/config/redshift.conf ~/.config/redshift.conf

# Install qtile dotfiles
echo "installing qtile dots..."
ln -Tsf ~/.dotfiles/config/qtile ~/.config/qtile

# Install terminal dotfiles
echo "installing kitty dots..."
ln -Tsf ~/.dotfiles/config/kitty ~/.config/kitty
