" This is necessary for VimTeX to load properly. The "indent" is optional.
" Note that most plugin managers will do this automatically.
filetype plugin indent on

" This enables Vim's and neovim's syntax-related features. Without this, some
" VimTeX features will not work (see ":help vimtex-requirements" for more
" info).
syntax enable

" Viewer options
let g:vimtex_view_method = 'general'
let g:vimtex_view_general_viewer = 'xdg-open'
let g:vimtex_view_general_options = '@pdf'

" Compiler
let g:vimtex_compiler_method = 'latexmk'
