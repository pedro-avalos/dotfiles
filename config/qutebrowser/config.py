config.load_autoconfig(False)

# UI settings
config.set("colors.webpage.darkmode.enabled", True)
config.set("colors.webpage.preferred_color_scheme", "dark")

# General settings
config.set("content.default_encoding", "utf-8")
config.set("content.notifications.enabled", True)
config.set("input.insert_mode.auto_load", True)
config.set("spellcheck.languages", ["en-US", "es-ES"])

# Privacy
config.set("content.cookies.accept", "no-3rdparty")
config.set("content.webrtc_ip_handling_policy", "default-public-interface-only")
config.set("content.blocking.method", "both")
config.set(
    "content.blocking.adblock.lists",
    [
        "https://easylist.to/easylist/easylist.txt",
        "https://easylist.to/easylist/easyprivacy.txt",
        "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
        "https://easylist.to/easylist/fanboy-social.txt",
        "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
        "https://easylist-downloads.adblockplus.org/fanboy-notifications.txt",
    ],
)

# URL
config.set("url.default_page", "https://search.brave.com/")
config.set("url.start_pages", "https://search.brave.com/")
config.set(
    "url.searchengines",
    {
        "DEFAULT": "https://search.brave.com/?q={}",
        "?": "https://search.brave.com/?q={}",
        "ddg": "https://duckduckgo.com/?q={}",
    },
)
