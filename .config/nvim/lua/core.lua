local vim = vim
local home = os.getenv('HOME')
local cache_dir = require('helper').get_cache_path()

-- Create cache dir and subs dir
local createdir = function()
	local data_dir = {
		cache_dir .. '/backup',
		cache_dir .. '/session',
		cache_dir .. '/swap',
		cache_dir .. '/tags',
		cache_dir .. '/undo',
	}

	if vim.fn.isdirectory(cache_dir) == 0 then
		os.execute('mkdir -p ' .. cache_dir)
		for _, v in pairs(data_dir) do
			if vim.fn.isdirectory(v) == 0 then
				os.execute('mkdir -p ' .. v)
			end
		end
	end
end

createdir()

-- Disable netrw
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1
