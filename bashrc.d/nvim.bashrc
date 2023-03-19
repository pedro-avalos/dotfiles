#!/usr/bin/env bash
# File: nvim.bashrc
# Useful aliases for (neo)vim

# Check if neovim is available, otherwise use vim
if command -v nvim &> /dev/null ; then # neovim is available
  alias vi='nvim'
  alias vim='nvim'
  alias diff='nvim -d'
elif command -v vim &> /dev/null ; then # vim is available
  alias vi='vim'
  alias diff='vim -d'
fi

# vim: ft=bash
