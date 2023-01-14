"""Provides the groups to use in qtile."""

from dataclasses import dataclass, field


@dataclass
class Group:
    """Contains the information about a group."""

    name: str
    """What this group is typically used for."""

    num: str
    """Number to use in keybindings."""

    icon: str
    """Icon to display in a bar."""

    layout: str = "columns"
    """Name of default layout in this group."""

    matches: list[str] = field(default_factory=list)
    """Names of processes that should automatically open in this group."""


groups: list[Group] = [
    Group(name="web", num="1", icon="爵"),
    Group(name="dev", num="2", icon="", matches=["code"]),
    Group(name="doc", num="3", icon=""),
    Group(name="chat", num="4", icon="", matches=["discord", "zoom", "skype"]),
    Group(name="music", num="5", icon="", matches=["spotify"]),
    Group(name="video", num="6", icon="", layout="max", matches=["vlc", "mpv"]),
    Group(
        name="games",
        num="7",
        icon="",
        layout="monadtall",
        matches=["Steam, lutris", "supertuxkart", "xonotic-sdl"],
    ),
    Group(name="sys", num="8", icon=""),
    Group(name="virt", num="9", icon="", matches=["virt-manager", "remote-viewer"]),
]
