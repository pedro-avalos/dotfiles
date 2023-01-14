"""Provides qtile's groups."""

from libqtile.config import Group, Match
from .util.groups import groups

qtile_groups = [
    Group(
        f"{group.num}",
        layout=group.layout,
        label=group.icon,
        matches=[Match(wm_class=m) for m in group.matches],
    )
    for group in groups
]
