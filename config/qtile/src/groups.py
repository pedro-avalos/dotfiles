"""Provides qtile's groups."""

from libqtile.config import Group, Match


def make_groups(settings: dict) -> list[Group]:
    assert "groups" in settings
    return [
        Group(
            f"{v['num']}",
            layout=v["layout"],
            label=v["icon"],
            matches=[Match(wm_class=m) for m in v["matches"]],
        )
        for v in settings["groups"].values()
    ]
