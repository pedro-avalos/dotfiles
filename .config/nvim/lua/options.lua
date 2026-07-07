local opt = vim.opt
local cache_dir = require('helper').get_cache_path()

opt.background = 'dark'
opt.termguicolors = true
opt.hidden = true
opt.magic = true
opt.virtualedit = 'block'
opt.clipboard = 'unnamedplus'
opt.wildignorecase = true
opt.swapfile = false
opt.directory = cache_dir .. '/swap/'
opt.undodir = cache_dir .. '/undo/'
opt.backupdir = cache_dir .. '/backup/'
opt.viewdir = cache_dir .. '/view/'
opt.spellfile = cache_dir .. '/spell/en.utf-8.add'
opt.history = 2000
opt.updatetime = 100
opt.redrawtime = 1500
opt.ignorecase = true
opt.smartcase = true
opt.infercase = true
opt.syntax = 'ON'
opt.mouse = 'a'

opt.completeopt = 'menu,menuone,noselect'
opt.showmode = false
opt.scrolloff = 2
opt.ruler = false
opt.showtabline = 1
opt.winwidth = 30
opt.pumheight = 15
opt.cmdheight = 1
opt.laststatus = 2
opt.list = true
opt.listchars = 'tab:»·,nbsp:+,trail:·,extends:→,precedes:←'
opt.pumblend = 10
opt.winblend = 10
opt.undofile = true

-- tab
opt.smarttab = true
opt.autoindent = true
opt.smartindent = true
opt.shiftround = true
opt.expandtab = false
opt.tabstop = 2
opt.shiftwidth = 2
opt.softtabstop = 2

-- indentation
opt.cinoptions = 't0'

-- wrap
opt.linebreak = true
opt.whichwrap = 'h,l,<,>,[,],~'
opt.breakindentopt = 'shift:2,min:20'
opt.showbreak = '↳ '
opt.foldlevelstart = 99
opt.foldmethod = 'syntax'

-- gutter
opt.number = true
opt.signcolumn = 'yes'

-- line lengths
opt.textwidth = 100
opt.colorcolumn = '80'
