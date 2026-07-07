" Check if vim-plug is installed. Install if not yet installed.
let data_dir = has('nvim') ? stdpath('data').'/site' : '~/.vim'
if empty(glob(data_dir.'/autoload/plug.vim'))
	silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
	autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

" Install missing plugins.
autocmd VimEnter * if len(filter(values(g:plugs), '!isdirectory(v:val.dir)'))
			\| PlugInstall --sync | source $VIMRC
			\| endif

set nocompatible

" Plugins to install.
call plug#begin()

Plug 'preservim/nerdcommenter'
Plug 'preservim/nerdtree' |
			\ Plug 'Xuyuanp/nerdtree-git-plugin'

Plug 'mhinz/vim-startify'
if has('nvim') || has('patch-8.0.902')
	Plug 'mhinz/vim-signify'
else
	Plug 'mhinz/vim-signify', { 'branch': 'legacy' }
endif

Plug 'prabirshrestha/vim-lsp'

Plug 'sheerun/vim-polyglot'

Plug 'lervag/vimtex'

Plug 'rust-lang/rust.vim'

Plug 'rafamadriz/friendly-snippets'

Plug 'itchyny/lightline.vim'

Plug 'tomasiser/vim-code-dark'

call plug#end()

source $HOME/.vim/plugs/nerdtree.vim
source $HOME/.vim/plugs/nerdcommenter.vim
source $HOME/.vim/plugs/startify.vim
source $HOME/.vim/plugs/vimtex.vim
source $HOME/.vim/plugs/lsp.vim
