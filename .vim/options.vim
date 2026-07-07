if has('termguicolors')
	set termguicolors
endif

" Styled and colored underline support
if has('&t_AU')
	let &t_AU = "\e[58:5:%dm"
endif
if has('&t_8u')
	let &t_8u = "\e[58:2:%lu:%lu:%lum"
endif
if has('&t_Us')
	let &t_Us = "\e[4:2m"
endif
if has('&t_Cs')
	let &t_Cs = "\e[4:3m"
endif
if has('&t_ds')
	let &t_ds = "\e[4:4m"
endif
if has('&t_Ds')
	let &t_Ds = "\e[4:5m"
endif
if has('&t_Ce')
	let &t_Ce = "\e[4:0m"
endif
" Strikethrough
if has('&t_Ts')
	let &t_Ts = "\e[9m"
endif
if has('&t_Te')
	let &t_Te = "\e[29m"
endif
" Truecolor support
if has('&t_8f')
	let &t_8f = "\e[38:2:%lu:%lu:%lum"
endif
if has('&t_8b')
	let &t_8b = "\e[48:2:%lu:%lu:%lum"
endif
if has('&t_RF')
	let &t_RF = "\e]10;?\e\\"
endif
if has('&t_RB')
	let &t_RB = "\e]11;?\e\\"
endif
" Bracketed paste
if has('&t_BE')
	let &t_BE = "\e[?2004h"
endif
if has('&t_BD')
	let &t_BD = "\e[?2004l"
endif
if has('&t_PS')
	let &t_PS = "\e[200~"
endif
if has('&t_PE')
	let &t_PE = "\e[201~"
endif
" Cursor control
if has('&t_RC')
	let &t_RC = "\e[?12$p"
endif
if has('&t_SH')
	let &t_SH = "\e[%d q"
endif
if has('&t_RS')
	let &t_RS = "\eP$q q\e\\"
endif
if has('&t_SI')
	let &t_SI = "\e[5 q"
endif
if has('&t_SR')
	let &t_SR = "\e[3 q"
endif
if has('&t_EI')
	let &t_EI = "\e[1 q"
endif
if has('&t_VS')
	let &t_VS = "\e[?12l"
endif
" Focus tracking
if has('&t_fe')
	let &t_fe = "\e[?1004h"
endif
if has('&t_fd')
	let &t_fd = "\e[?1004l"
endif
if has('FocusGained')
	execute "set <FocusGained>=\<Esc>[I"
endif
if has('FocusLost')
	execute "set <FocusLost>=\<Esc>[O"
endif
" Window title
if has('&t_ST')
	let &t_ST = "\e[22;2t"
endif
if has('&t_RT')
	let &t_RT = "\e[23;2t"
endif

" vim hardcodes background color erase even if the terminfo file does
" not contain bce. This causes incorrect background rendering when
" using a color theme with a background color in terminals such as
" kitty that do not support background color erase.
let &t_ut=''

" Make vim use XDG directories for backups &c...
if !has('nvim')
	if empty($XDG_DATA_HOME)
		let $XDG_DATA_HOME=$HOME.'/.local/share'
	endif

	if !isdirectory($XDG_DATA_HOME.'/vim/swap')
		call mkdir($XDG_DATA_HOME.'/vim/swap', "p", 0700)
	endif
	if !isdirectory($XDG_DATA_HOME.'/vim/backup')
		call mkdir($XDG_DATA_HOME.'/vim/backup', "p", 0700)
	endif
	if !isdirectory($XDG_DATA_HOME.'/vim/undo')
		call mkdir($XDG_DATA_HOME.'/vim/undo', "p", 0700)
	endif

	set directory=$XDG_DATA_HOME/vim/swap/
	set backupdir=$XDG_DATA_HOME/vim/backup/
	set undodir=$XDG_DATA_HOME/vim/undo
	set undofile
endif

" Mouse support
set mouse=a
set ttymouse=sgr
if has('balloonevalterm')
	set balloonevalterm
endif

set wildignorecase ignorecase smartcase infercase
set virtualedit=block
set redrawtime=1500
syntax on

set noshowmode noruler list
set completeopt=menu
set completeopt+=menuone
try
	set completeopt+=noselect
catch
endtry
set scrolloff=2
set showtabline=1
set winwidth=30
set pumheight=15
set cmdheight=1
set laststatus=2
set listchars=tab:\ \ ,nbsp:+,trail:·,extends:→,precedes:←

" tab
set smarttab noexpandtab autoindent smartindent shiftround
set tabstop=2 shiftwidth=2 softtabstop=2

" wrap
set linebreak
set whichwrap=h,l,<,>,[,],~
set breakindentopt=shift:2,min:20
set showbreak=↳
set foldlevelstart=99
set foldmethod=syntax

set number
if has('signcolumn')
	set signcolumn=yes
endif

set textwidth=100
set colorcolumn=80
set background=dark
