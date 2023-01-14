"""Provides the layouts (and settings for them) that qtile will use."""

# from libqtile.layout.bsp import Bsp
from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating
from libqtile.layout.max import Max

# from libqtile.layout.matrix import Matrix
from libqtile.layout.xmonad import (
    MonadTall,
    # MonadThreeCol,
    # MonadWide,
)

# from libqtile.layout.ratiotile import RatioTile
from libqtile.layout.stack import Stack
from libqtile.layout.tile import Tile

# from libqtile.layout.tree import TreeTab
# from libqtile.layout.verticaltile import VerticalTile
# from libqtile.layout.zoomy import Zoomy
from .util import theme


def make_layouts(layouts_theme: theme.LayoutsTheme) -> list:
    """Creates the layouts used."""

    return [
        # Bsp(**layouts_theme.default),
        Columns(**{**layouts_theme.default, **layouts_theme.columns}),
        Floating(**layouts_theme.floating),
        Max(**layouts_theme.default),
        # Matrix(**layouts_theme.default),
        MonadTall(**layouts_theme.default),
        # MonadThreeCol(**layouts_theme.default),
        # MonadWide(**layouts_theme.default),
        # RatioTile(**layouts_theme.default),
        Stack(**layouts_theme.default),
        Tile(**layouts_theme.default),
        # TreeTab(**layouts_theme.default),
        # VerticalTile(**layouts_theme.default),
        # Zoomy(**layouts_theme.default),
    ]


def make_floating_layout(layouts_theme: theme.LayoutsTheme) -> Floating:
    """Creates the floating layout used."""

    return Floating(
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
