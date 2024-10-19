"""Oxocarbon themes.

Based on: https://github.com/nyoom-engineering/base16-oxocarbon.
"""
from typing import Literal


def setup(c, scheme: Literal["dark", "light"] = "dark"):
    palette = {}
    if scheme == "light":
        palette = {
            "base00": "#f2f4f8",
            "base01": "#dde1e6",
            "base02": "#525252",
            "base03": "#161616",
            "base04": "#262626",
            "base05": "#393939",
            "base06": "#525252",
            "base07": "#08bdba",
            "base08": "#ff7eb6",
            "base09": "#ee5396",
            "base0A": "#FF6F00",
            "base0B": "#0f62fe",
            "base0C": "#673AB7",
            "base0D": "#42be65",
            "base0E": "#be95ff",
            "base0F": "#37474F",
        }
    else:
        palette = {
            "base00": "#161616",
            "base01": "#262626",
            "base02": "#393939",
            "base03": "#525252",
            "base04": "#dde1e6",
            "base05": "#f2f4f8",
            "base06": "#ffffff",
            "base07": "#08bdba",
            "base08": "#3ddbd9",
            "base09": "#78a9ff",
            "base0A": "#ee5396",
            "base0B": "#33b1ff",
            "base0C": "#ff7eb6",
            "base0D": "#42be65",
            "base0E": "#be95ff",
            "base0F": "#82cfff",
        }

    # Text color of the completion widget. May be a single color to use for
    # all columns or a list of three colors, one for each column.
    c.colors.completion.fg = palette["base05"]

    # Background color of the completion widget for odd rows.
    c.colors.completion.odd.bg = palette["base01"]

    # Background color of the completion widget for even rows.
    c.colors.completion.even.bg = palette["base00"]

    # Foreground color of completion widget category headers.
    c.colors.completion.category.fg = palette["base0A"]

    # Background color of the completion widget category headers.
    c.colors.completion.category.bg = palette["base00"]

    # Top border color of the completion widget category headers.
    c.colors.completion.category.border.top = palette["base00"]

    # Bottom border color of the completion widget category headers.
    c.colors.completion.category.border.bottom = palette["base00"]

    # Foreground color of the selected completion item.
    c.colors.completion.item.selected.fg = palette["base05"]

    # Background color of the selected completion item.
    c.colors.completion.item.selected.bg = palette["base02"]

    # Top border color of the selected completion item.
    c.colors.completion.item.selected.border.top = palette["base02"]

    # Bottom border color of the selected completion item.
    c.colors.completion.item.selected.border.bottom = palette["base02"]

    # Foreground color of the matched text in the selected completion item.
    c.colors.completion.item.selected.match.fg = palette["base0B"]

    # Foreground color of the matched text in the completion.
    c.colors.completion.match.fg = palette["base0B"]

    # Color of the scrollbar handle in the completion view.
    c.colors.completion.scrollbar.fg = palette["base05"]

    # Color of the scrollbar in the completion view.
    c.colors.completion.scrollbar.bg = palette["base00"]

    # Background color of disabled items in the context menu.
    c.colors.contextmenu.disabled.bg = palette["base01"]

    # Foreground color of disabled items in the context menu.
    c.colors.contextmenu.disabled.fg = palette["base04"]

    # Background color of the context menu. If set to null, the Qt default is used.
    c.colors.contextmenu.menu.bg = palette["base00"]

    # Foreground color of the context menu. If set to null, the Qt default is used.
    c.colors.contextmenu.menu.fg = palette["base05"]

    # Background color of the context menu’s selected item. If set to null, the Qt default is used.
    c.colors.contextmenu.selected.bg = palette["base02"]

    # Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
    c.colors.contextmenu.selected.fg = palette["base05"]

    # Background color for the download bar.
    c.colors.downloads.bar.bg = palette["base00"]

    # Color gradient start for download text.
    c.colors.downloads.start.fg = palette["base00"]

    # Color gradient start for download backgrounds.
    c.colors.downloads.start.bg = palette["base0D"]

    # Color gradient end for download text.
    c.colors.downloads.stop.fg = palette["base00"]

    # Color gradient stop for download backgrounds.
    c.colors.downloads.stop.bg = palette["base0C"]

    # Foreground color for downloads with errors.
    c.colors.downloads.error.fg = palette["base08"]

    # Font color for hints.
    c.colors.hints.fg = palette["base00"]

    # Background color for hints. Note that you can use a `rgba(...)` value
    # for transparency.
    c.colors.hints.bg = palette["base0A"]

    # Font color for the matched part of hints.
    c.colors.hints.match.fg = palette["base05"]

    # Text color for the keyhint widget.
    c.colors.keyhint.fg = palette["base05"]

    # Highlight color for keys to complete the current keychain.
    c.colors.keyhint.suffix.fg = palette["base05"]

    # Background color of the keyhint widget.
    c.colors.keyhint.bg = palette["base00"]

    # Foreground color of an error message.
    c.colors.messages.error.fg = palette["base00"]

    # Background color of an error message.
    c.colors.messages.error.bg = palette["base08"]

    # Border color of an error message.
    c.colors.messages.error.border = palette["base08"]

    # Foreground color of a warning message.
    c.colors.messages.warning.fg = palette["base00"]

    # Background color of a warning message.
    c.colors.messages.warning.bg = palette["base0E"]

    # Border color of a warning message.
    c.colors.messages.warning.border = palette["base0E"]

    # Foreground color of an info message.
    c.colors.messages.info.fg = palette["base05"]

    # Background color of an info message.
    c.colors.messages.info.bg = palette["base00"]

    # Border color of an info message.
    c.colors.messages.info.border = palette["base00"]

    # Foreground color for prompts.
    c.colors.prompts.fg = palette["base05"]

    # Border used around UI elements in prompts.
    c.colors.prompts.border = palette["base00"]

    # Background color for prompts.
    c.colors.prompts.bg = palette["base00"]

    # Background color for the selected item in filename prompts.
    c.colors.prompts.selected.bg = palette["base02"]

    # Foreground color for the selected item in filename prompts.
    c.colors.prompts.selected.fg = palette["base05"]

    # Foreground color of the statusbar.
    c.colors.statusbar.normal.fg = palette["base0B"]

    # Background color of the statusbar.
    c.colors.statusbar.normal.bg = palette["base00"]

    # Foreground color of the statusbar in insert mode.
    c.colors.statusbar.insert.fg = palette["base00"]

    # Background color of the statusbar in insert mode.
    c.colors.statusbar.insert.bg = palette["base0D"]

    # Foreground color of the statusbar in passthrough mode.
    c.colors.statusbar.passthrough.fg = palette["base00"]

    # Background color of the statusbar in passthrough mode.
    c.colors.statusbar.passthrough.bg = palette["base0C"]

    # Foreground color of the statusbar in private browsing mode.
    c.colors.statusbar.private.fg = palette["base00"]

    # Background color of the statusbar in private browsing mode.
    c.colors.statusbar.private.bg = palette["base01"]

    # Foreground color of the statusbar in command mode.
    c.colors.statusbar.command.fg = palette["base05"]

    # Background color of the statusbar in command mode.
    c.colors.statusbar.command.bg = palette["base00"]

    # Foreground color of the statusbar in private browsing + command mode.
    c.colors.statusbar.command.private.fg = palette["base05"]

    # Background color of the statusbar in private browsing + command mode.
    c.colors.statusbar.command.private.bg = palette["base00"]

    # Foreground color of the statusbar in caret mode.
    c.colors.statusbar.caret.fg = palette["base00"]

    # Background color of the statusbar in caret mode.
    c.colors.statusbar.caret.bg = palette["base0E"]

    # Foreground color of the statusbar in caret mode with a selection.
    c.colors.statusbar.caret.selection.fg = palette["base00"]

    # Background color of the statusbar in caret mode with a selection.
    c.colors.statusbar.caret.selection.bg = palette["base0D"]

    # Background color of the progress bar.
    c.colors.statusbar.progress.bg = palette["base0D"]

    # Default foreground color of the URL in the statusbar.
    c.colors.statusbar.url.fg = palette["base05"]

    # Foreground color of the URL in the statusbar on error.
    c.colors.statusbar.url.error.fg = palette["base08"]

    # Foreground color of the URL in the statusbar for hovered links.
    c.colors.statusbar.url.hover.fg = palette["base05"]

    # Foreground color of the URL in the statusbar on successful load
    # (http).
    c.colors.statusbar.url.success.http.fg = palette["base0C"]

    # Foreground color of the URL in the statusbar on successful load
    # (https).
    c.colors.statusbar.url.success.https.fg = palette["base0B"]

    # Foreground color of the URL in the statusbar when there's a warning.
    c.colors.statusbar.url.warn.fg = palette["base0E"]

    # Background color of the tab bar.
    c.colors.tabs.bar.bg = palette["base00"]

    # Color gradient start for the tab indicator.
    c.colors.tabs.indicator.start = palette["base0D"]

    # Color gradient end for the tab indicator.
    c.colors.tabs.indicator.stop = palette["base0C"]

    # Color for the tab indicator on errors.
    c.colors.tabs.indicator.error = palette["base08"]

    # Foreground color of unselected odd tabs.
    c.colors.tabs.odd.fg = palette["base05"]

    # Background color of unselected odd tabs.
    c.colors.tabs.odd.bg = palette["base01"]

    # Foreground color of unselected even tabs.
    c.colors.tabs.even.fg = palette["base05"]

    # Background color of unselected even tabs.
    c.colors.tabs.even.bg = palette["base00"]

    # Background color of pinned unselected even tabs.
    c.colors.tabs.pinned.even.bg = palette["base0C"]

    # Foreground color of pinned unselected even tabs.
    c.colors.tabs.pinned.even.fg = palette["base07"]

    # Background color of pinned unselected odd tabs.
    c.colors.tabs.pinned.odd.bg = palette["base0B"]

    # Foreground color of pinned unselected odd tabs.
    c.colors.tabs.pinned.odd.fg = palette["base07"]

    # Background color of pinned selected even tabs.
    c.colors.tabs.pinned.selected.even.bg = palette["base02"]

    # Foreground color of pinned selected even tabs.
    c.colors.tabs.pinned.selected.even.fg = palette["base05"]

    # Background color of pinned selected odd tabs.
    c.colors.tabs.pinned.selected.odd.bg = palette["base02"]

    # Foreground color of pinned selected odd tabs.
    c.colors.tabs.pinned.selected.odd.fg = palette["base05"]

    # Foreground color of selected odd tabs.
    c.colors.tabs.selected.odd.fg = palette["base05"]

    # Background color of selected odd tabs.
    c.colors.tabs.selected.odd.bg = palette["base02"]

    # Foreground color of selected even tabs.
    c.colors.tabs.selected.even.fg = palette["base05"]

    # Background color of selected even tabs.
    c.colors.tabs.selected.even.bg = palette["base02"]

    # Background color for webpages if unset (or empty to use the theme's
    # color).
    c.colors.webpage.bg = palette["base00"]
