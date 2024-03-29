#!/usr/bin/env sh

# Show help menu
usage () {
		1>&2 printf -- "Usage: %s [-hf] [-d DOTS_DIR]\n" "$0"
		1>&2 printf -- "\t-h: Show help menu\n"
		1>&2 printf -- "\t-d DOTS_DIR: Path to dotfiles directory\n"
		1>&2 printf -- "\t-f: Force install\n"
}

# Default option values
unset FORCE                  # Don't force
DOTS_DIR="${HOME}/.dotfiles" # Default path to dotfiles

# Parse options
while getopts "hfd:" opt ; do
		case "${opt}" in
				f)
						FORCE=1
						;;
				d)
						DOTS_DIR="${OPTARG}"
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

# Helper function to replace existing file/directory with my dotfiles
# Takes in two parameters: (src, dest)
install_dots ()
{
		if [ "${FORCE}" ] ; then
				rm -rf  "$2"      2> /dev/null
				ln -Tsf "$1" "$2" 2> /dev/null
		else
				ln -Ts "$1" "$2" 2> /dev/null
		fi
}

# Update dotfiles
git -C ~/.dotfiles pull --recurse-submodules

echo "ensuring directories exist..."
[ ! -d ~/.config ]      && mkdir "${HOME}/.config"
[ ! -d ~/.local ]       && mkdir "${HOME}/.local"
[ ! -d ~/.local/share ] && mkdir "${HOME}/.local/share"

echo "installing dots scripts..."
install_dots "${DOTS_DIR}/bin" "${HOME}/.bin"

echo "installing xfce dots..."
install_dots "${DOTS_DIR}/local/share/xfce4" "${HOME}/.local/share/xfce4"

echo "installing shell dots..."
install_dots "${DOTS_DIR}/bash_profile" "${HOME}/.bash_profile"
install_dots "${DOTS_DIR}/bashrc"       "${HOME}/.bashrc"
install_dots "${DOTS_DIR}/config/bash"  "${HOME}/.config/bash"
install_dots "${DOTS_DIR}/zshenv"       "${HOME}/.zshenv"
install_dots "${DOTS_DIR}/config/zsh"   "${HOME}/.config/zsh"

echo "installing tmux dots..."
install_dots "${DOTS_DIR}/config/tmux"  "${HOME}/.config/tmux"
install_dots "${DOTS_DIR}/config/tmuxp" "${HOME}/.config/tmuxp"

echo "installing (neo)vim dots..."
install_dots "${DOTS_DIR}/vim"          "${HOME}/.vim"
install_dots "${DOTS_DIR}/vim/init.vim" "${HOME}/.vimrc"
install_dots "${DOTS_DIR}/config/nvim"  "${HOME}/.config/nvim"

echo "installing emacs dots..."
install_dots "${DOTS_DIR}/config/emacs" "${HOME}/.config/emacs"

echo "installing window manager dots..."
install_dots "${DOTS_DIR}/config/autostart" "${HOME}/.config/autostart"
install_dots "${DOTS_DIR}/config/i3"        "${HOME}/.config/i3"
install_dots "${DOTS_DIR}/config/qtile"     "${HOME}/.config/qtile"
install_dots "${DOTS_DIR}/dwm"              "${HOME}/.dwm"
install_dots "${DOTS_DIR}/wallpapers"       "${HOME}/.wallpapers"

echo "installing qutebrowser dots..."
install_dots "${DOTS_DIR}/config/qutebrowser" "${HOME}/.config/qutebrowser"

echo "installing rofi dots..."
install_dots "${DOTS_DIR}/config/rofi"      "${HOME}/.config/rofi"
install_dots "${DOTS_DIR}/local/share/rofi" "${HOME}/.local/share/rofi"

echo "installing terminal dots..."
install_dots "${DOTS_DIR}/config/kitty"     "${HOME}/.config/kitty"
install_dots "${DOTS_DIR}/config/alacritty" "${HOME}/.config/alacritty"

echo "installing misc dots..."
install_dots "${DOTS_DIR}/xsession"         "${HOME}/.xsession"
install_dots "${DOTS_DIR}/inputrc"          "${HOME}/.inputrc"
install_dots "${DOTS_DIR}/config/picom"     "${HOME}/.config/picom"
install_dots "${DOTS_DIR}/config/latexmk"   "${HOME}/.config/latexmk"
install_dots "${DOTS_DIR}/config/dunst"     "${HOME}/.config/dunst"
install_dots "${DOTS_DIR}/config/clangd"    "${HOME}/.config/clangd"
install_dots "${DOTS_DIR}/config/gammastep" "${HOME}/.config/gammastep"
install_dots "${DOTS_DIR}/config/redshift"  "${HOME}/.config/redshift"
