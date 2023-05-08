"""This module creates the layouts and respective settings for qtile."""

from libqtile.config import Match
from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating
from libqtile.layout.max import Max
from libqtile.layout.stack import Stack
from libqtile.layout.xmonad import MonadTall

from .theme import colors

# Commonly used settings
layout_defaults = {
    "grow_amount": 3,
    "margin": 6,
    "border_focus": colors.colors["border_focus"],
    "border_normal": colors.colors["border_normal"],
    "border_normal_stack": colors.colors["border_normal_stack"],
    "border_focus_stack": colors.colors["border_focus_stack"],
}


def make_layouts() -> list:
    """Makes the layouts used by qtile."""

    return [
        MonadTall(**layout_defaults),
        Stack(**layout_defaults),
        Columns(num_columns=3, **layout_defaults),
        Max(**layout_defaults),
        Floating(
            float_rules=None,
            no_reposition_rules=None,
            border_width=0,
            **layout_defaults,
        ),
    ]


def make_floating_layout() -> Floating:
    """Makes the floating layout used by qtile."""

    return Floating(
        float_rules=[
            Match(title="Open File"),
            Match(title="File Operation Progress", wm_class="thunar"),
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
            Match(wm_class="Pinentry-gtk-2"),
            Match(wm_class="pinentry"),
            Match(wm_class="qt5ct"),
            Match(wm_class="ssh-askpass"),
            Match(wm_class="Dragon-drag-and-drop"),
            Match(wm_class="toolbar"),
            Match(wm_class="wlroots"),
            Match(wm_class="Xephyr"),
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="blueman-manager"),
            Match(wm_type="dialog"),
            Match(role="gimp-file-export"),
            Match(func=lambda c: c.has_fixed_size()),
            Match(func=lambda c: bool(c.is_transient_for())),
        ],
        border_width=0,
        **layout_defaults,
    )
