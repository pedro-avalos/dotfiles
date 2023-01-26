#!/usr/bin/env sh
# File: install_dots.sh

DOTS_DIR="${HOME}/.dotfiles"

# Helper function to replace existing file/directory with my dotfiles
# Takes in two parameters: (src, dest)
install_dots ()
{
  rm -rf "$2"
  ln -Tsf "$1" "$2"
}

# Update dotfiles
git -C ~/.dotfiles pull

# Ensure directories exist
echo "ensuring directories exist..."
[ ! -d ~/.config ]      && mkdir "${HOME}/.config"
[ ! -d ~/.local ]       && mkdir "${HOME}/.local"
[ ! -d ~/.local/share ] && mkdir "${HOME}/.local/share"

# Install dotfiles executables and scripts
echo "installing dots scripts..."
install_dots "${DOTS_DIR}/bin" "${HOME}/.bin"

# Install xfce dotfiles
echo "installing xfce dots..."
install_dots "${DOTS_DIR}/local/share/xfce4" "${HOME}/.local/share/xfce4"

# Install keybindings
echo "installing inputrc dots..."
install_dots "${DOTS_DIR}/inputrc" "${HOME}/.inputrc"

# Install bash dotfiles
echo "installing bash dots..."
install_dots "${DOTS_DIR}/bashrc"       "${HOME}/.bashrc"
install_dots "${DOTS_DIR}/bashrc.d"     "${HOME}/.bashrc.d"
install_dots "${DOTS_DIR}/bash_profile" "${HOME}/.bash_profile"
install_dots "${DOTS_DIR}/bash_logout"  "${HOME}/.bash_logout"

echo "installing emacs dots..."
install_dots "${DOTS_DIR}/emacs.d" "${HOME}/.emacs.d"

# Install tmux dotfiles
echo "installing tmux dots..."
install_dots "${DOTS_DIR}/config/tmux"  "${HOME}/.config/tmux"
install_dots "${DOTS_DIR}/config/tmuxp" "${HOME}/.config/tmuxp"

# Install gtk dotfiles
echo "installing gtk dots..."
install_dots "${DOTS_DIR}/config/gtk-3.0" "${HOME}/.config/gtk-3.0"

# Install color temperature dotfiles
echo "installing color-temp dots..."
install_dots "${DOTS_DIR}/config/gammastep"     "${HOME}/.config/gammastep"
install_dots "${DOTS_DIR}/config/redshift.conf" "${HOME}/.config/redshift.conf"

# Install qtile dotfiles
echo "installing qtile dots..."
install_dots "${DOTS_DIR}/config/qtile" "${HOME}/.config/qtile"

# Install rofi dotfiles
echo "installing rofi dots..."
install_dots "${DOTS_DIR}/config/rofi"      "${HOME}/.config/rofi"
install_dots "${DOTS_DIR}/local/share/rofi" "${HOME}/.local/share/rofi"

# Install terminal dotfiles
echo "installing kitty dots..."
install_dots "${DOTS_DIR}/config/kitty" "${HOME}/.config/kitty"
echo "installing alacritty dots..."
install_dots "${DOTS_DIR}/config/alacritty" "${HOME}/.config/alacritty"
