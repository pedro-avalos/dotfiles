"""Provides the layouts (and settings for them) that qtile will use."""

from libqtile import layout

from .util.theme import LayoutsTheme


def make_layouts(layouts_theme: LayoutsTheme) -> list:
    """Creates the layouts used."""

    return [
        # layout.Bsp(**layouts_theme.default),
        layout.Columns(**{**layouts_theme.default, **layouts_theme.columns}),
        layout.Floating(**layouts_theme.floating),
        layout.Max(**layouts_theme.default),
        # layout.Matrix(**layouts_theme.default),
        layout.MonadTall(**layouts_theme.default),
        # layout.MonadThreeCol(**layouts_theme.default),
        # layout.MonadWide(**layouts_theme.default),
        # layout.RatioTile(**layouts_theme.default),
        layout.Stack(**layouts_theme.default),
        layout.Tile(**layouts_theme.default),
        # layout.TreeTab(**layouts_theme.default),
        # layout.VerticalTile(**layouts_theme.default),
        # layout.Zoomy(**layouts_theme.default),
    ]


def make_floating_layout(layouts_theme: LayoutsTheme) -> layout.Floating:
    """Creates the floating layout used."""

    return layout.Floating(
        auto_float_typesR=[
            # Run the utility `xprop` to see the wm class and name of an X client
            {"wmclass": "confirm"},
            {"wmclass": "dialog"},
            {"wmclass": "download"},
            {"wmclass": "error"},
            {"wmclass": "file_progress"},
            {"wmclass": "notification"},
            {"wmclass": "notify"},
            {"wmclass": "popup_menu"},
            {"wmclass": "splash"},
            {"wmclass": "toolbar"},
            {"wmclass": "confirmreset"},  # gitk
            {"wmclass": "makebranch"},  # gitk
            {"wmclass": "maketag"},  # gitk
            {"wmclass": "branchdialog"},  # gitk
            {"wmclass": "pinentry"},  # GPG key password entry
            {"wmclass": "ssh-askpass"},  # ssh-askpass
        ],
        **layouts_theme.floating,
    )


# pyright: reportPrivateImportUsage=false
