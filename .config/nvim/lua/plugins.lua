local vim = vim

vim.pack.add({
		'https://github.com/neovim/nvim-lspconfig',
		'https://github.com/nvim-tree/nvim-web-devicons',
		'https://github.com/nvim-tree/nvim-tree.lua',
		'https://github.com/Mofiqul/vscode.nvim',
		'https://github.com/goolord/alpha-nvim',
		'https://github.com/nvim-lualine/lualine.nvim',
		'https://github.com/nickjvandyke/opencode.nvim',
	})

local c = require('vscode.colors').get_colors()
require('vscode').setup({
		transparent = true,
		italic_comments = true,
		italic_inlayhints = true,
		underline_links = true,
		disable_nvimtree_bg = true,
		terminal_colors = true,
		color_overrides = {
			vscLineNumber = '#FFFFFF',
		},
		group_overrides = {
			Cursor = { fg=c.vscDarkBlue, bg=c.vscLightGreen, bold=true },
		},
	})
require('lualine').setup({
		options = {
			theme = 'vscode',
		},
		sections = {
			lualine_z = {
				{
					require('opencode').statusline,
				},
			},
		},
	})

require('nvim-tree').setup()

local startify = require('alpha.themes.startify')
startify.file_icons.provider = 'devicons'
require('alpha').setup(startify.config)

vim.o.autoread = true
vim.keymap.set({ "n", "x" }, "<leader>oa", function() require("opencode").ask("@this: ") end, { desc = "Ask OpenCode…" })
vim.keymap.set({ "n", "x" }, "<leader>os", function() require("opencode").select() end, { desc = "Select OpenCode…" })
vim.keymap.set({ "n", "x" }, "go",  function() return require("opencode").operator("@this ") end, { desc = "Append range to OpenCode", expr = true })
vim.keymap.set("n", "goo", function() return require("opencode").operator("@this ") .. "_" end, { desc = "Append line to OpenCode", expr = true })
vim.keymap.set("n", "<S-C-u>", function() require("opencode").command("session.half.page.up") end, { desc = "Scroll OpenCode up" })
vim.keymap.set("n", "<S-C-d>", function() require("opencode").command("session.half.page.down") end, { desc = "Scroll OpenCode down" })
