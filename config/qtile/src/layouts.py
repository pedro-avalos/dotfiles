"""Provides the layouts (and settings for them) that qtile will use."""

from libqtile import layout
from libqtile.config import Match

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
        float_rules=[
            Match(title="Open File"),
            Match(title="File Operation Progress", wm_class="thunar"),  # Wayland
            Match(wm_class="Arandr"),
            Match(wm_class="org.kde.ark"),
            Match(wm_class="confirm"),
            Match(wm_class="dialog"),
            Match(wm_class="download"),
            Match(wm_class="error"),
            Match(wm_class="fiji-Main"),
            Match(wm_class="file_progress"),
            Match(wm_class="imv"),
            Match(wm_class="lxappearance"),
            Match(wm_class="mpv"),
            Match(wm_class="notification"),
            Match(wm_class="notify"),
            Match(wm_class="popup_menu"),
            Match(wm_class="splash"),
            Match(wm_class="pavucontrol"),
            Match(wm_class="Pinentry-gtk-2"),  # GPG key password entry
            Match(wm_class="pinentry"),  # GPG key password entry
            Match(wm_class="qt5ct"),
            Match(wm_class="ssh-askpass"),
            Match(wm_class="Dragon-drag-and-drop"),
            Match(wm_class="toolbar"),
            Match(wm_class="wlroots"),
            Match(wm_class="Xephyr"),
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_type="dialog"),
            Match(role="gimp-file-export"),
            Match(func=lambda c: c.has_fixed_size()),
            Match(func=lambda c: bool(c.is_transient_for())),
        ],
        **layouts_theme.floating,
    )


# pyright: reportPrivateImportUsage=false
