let g:ascii=[
			\ '        __',
			\ '.--.--.|__|.--------.',
			\ '|  |  ||  ||        |',
			\ ' \___/ |__||__|__|__|',
			\ ''
			\]
let g:startify_custom_header=startify#center(g:ascii)
let g:startify_bookmarks = systemlist("cut -sd' ' -f 2- ~/.NERDTreeBookmarks")
