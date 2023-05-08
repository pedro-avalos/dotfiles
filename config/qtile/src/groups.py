"""This module contains the functions to create qtile's groups."""

from libqtile.config import Group, Match


def make_groups() -> list[Group]:
    """Makes the list of groups used by qtile."""

    return [
        Group(
            name="1",
            label=" 󰖟 ",
            layout="monadtall",
            matches=[],
        ),
        Group(
            name="2",
            label="  ",
            layout="monadtall",
            matches=[],
        ),
        Group(
            name="3",
            label=" 󰈙 ",
            layout="monadtall",
            matches=[],
        ),
        Group(
            name="4",
            label=" 󰭹 ",
            layout="monadtall",
            matches=[Match(wm_class="discord")],
        ),
        Group(
            name="5",
            label="  ",
            layout="monadtall",
            matches=[Match(wm_class="spotify")],
        ),
        Group(
            name="6",
            label=" 󰟴 ",
            layout="max",
            matches=[Match(wm_class="vlc"), Match(wm_class="mpv")],
        ),
        Group(
            name="7",
            label="  ",
            layout="monadtall",
            matches=[Match(wm_class="Steam")],
        ),
        Group(
            name="8",
            layout="monadtall",
            label="  ",
            matches=[],
        ),
        Group(
            name="9",
            layout="monadtall",
            label=" 󰇘 ",
            matches=[],
        ),
    ]
