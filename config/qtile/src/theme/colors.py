"""This module contains qtile's color schemes."""

import os

dark: dict[str, list[str]] = {
    # Bar
    "bg": ["#161616", "#161616"],
    "fg": ["#f4f4f4", "#f4f4f4"],
    "py": ["#f1c21b", "#f1c21b"],
    "err": ["#ff8389", "#ff8389"],
    "red": ["#fa4d56", "#fa4d56"],
    # Groupbox
    "current": ["#4589ff", "#4589ff"],
    "unfocus": ["#6f6f6f", "#6f6f6f"],
    "inactive": ["#6f6f6f", "#6f6f6f"],
    # Layout
    "border_focus": ["#4589ff", "#4589ff"],
    "border_normal": ["#393939", "#393939"],
    "border_normal_stack": ["#393939", "#393939"],
    "border_focus_stack": ["#be95ff", "#be95ff"],
}

# TODO: Add light theme
light: dict[str, list[str]] = {
    # Bar
    "bg": ["#161616", "#161616"],
    "fg": ["#f4f4f4", "#f4f4f4"],
    "py": ["#f1c21b", "#f1c21b"],
    "err": ["#ff8389", "#ff8389"],
    "red": ["#fa4d56", "#fa4d56"],
    # Groupbox
    "current": ["#4589ff", "#4589ff"],
    "unfocus": ["#6f6f6f", "#6f6f6f"],
    "inactive": ["#6f6f6f", "#6f6f6f"],
    # Layout
    "border_focus": ["#4589ff", "#4589ff"],
    "border_normal": ["#393939", "#393939"],
    "border_normal_stack": ["#393939", "#393939"],
    "border_focus_stack": ["#be95ff", "#be95ff"],
}

colors = dark
if "QTILE_THEME" in os.environ:
    colors = light if os.environ["QTILE_THEME"].lower() == "light" else dark
