"""This is my qutebrowser configuration."""

from themes import oxocarbon

config.load_autoconfig(False)

# UI settings
oxocarbon.setup(c, "dark")
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.preferred_color_scheme = "dark"

# General settings
c.content.default_encoding = "utf-8"
c.content.notifications.enabled = True
c.input.insert_mode.auto_load = True
c.spellcheck.languages = ["en-US", "es-ES"]

# Privacy
c.content.cookies.accept = "no-3rdparty"
c.content.webrtc_ip_handling_policy = "default-public-interface-only"
c.content.blocking.method = "both"
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://easylist.to/easylist/fanboy-social.txt",
    "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
    "https://secure.fanboy.co.nz/fanboy-problematic-sites.txt",
]

# URL
c.url.default_page = "https://search.brave.com/"
c.url.start_pages = "https://search.brave.com/"
c.url.searchengines = {
    "DEFAULT": "https://search.brave.com/search?q={}",
    "?": "https://search.brave.com/search?q={}",
    "wikt": "https://wiktionary.org/w/?search={}",
    "wiki": "https://en.wikipedia.org/w/?search={}",
    "ddg": "https://duckduckgo.com/?q={}",
    "sp": "https://startpage.com/sp/search?query={}",
    "g": "https://google.com/search?q={}",
    "yt": "https://youtube.com/results?search_query={}",
    "gh": "https://github.com/search?q={}&type=repositories",
    "gl": "https://gitlab.com/explore/projects?name={}&sort=stars_desc",
}

# Bindings
config.bind("<Ctrl+/>", "hint links spawn --detach mpv {hint-url}")
config.bind("M", "hint links spawn mpv {hint-url}")
