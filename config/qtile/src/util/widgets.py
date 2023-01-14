"""Provides the widgets to be used by the bar(s)."""

from libqtile.widget import (
    Battery,
    # CapsNumLockIndicator,
    # CheckUpdates,
    Clock,
    # CurrentLayout,
    CurrentLayoutIcon,
    CurrentScreen,
    GroupBox,
    # Memory,
    # Net,
    # Prompt,
    PulseVolume,
    # Sep,
    Spacer,
    Systray,
    # TaskList,
    TextBox,
    # ThermalSensor,
    QuickExit,
    # Volume,
    # WindowCount,
    WindowName,
    # Wlan,
)

from . import apps, mouse, theme


class WidgetsMaker:
    """Creates the lists of widgets to be used by the bar(s).

    Args:
        fonts_theme (theme.FontsTheme): Theming for the fonts.
        widgets_theme (theme.WidgetsTheme): Theming for the widgets.

    Attributes:
        main_widgets (list): Widgets for main screen.
        other_widgets (list): Widgets for all other screens.
    """

    def __init__(
        self,
        fonts_theme: theme.FontsTheme,
        widgets_theme: theme.WidgetsTheme,
    ) -> None:

        self.fonts_theme: theme.FontsTheme = fonts_theme
        self.widgets_theme: theme.WidgetsTheme = widgets_theme
        self._create_settings()
        self.main_widgets = [
            Spacer(**self._spacer),
            TextBox(**self._launcher),
            Spacer(**self._spacer),
            GroupBox(**self._groupbox),
            CurrentLayoutIcon(**self._current_layout_icon),
            Spacer(**self._spacer),
            WindowName(**self._window_name),
            Spacer(**self._spacer_stretch),
            Systray(**self._systray),
            Spacer(**self._spacer),
            PulseVolume(**self._pulse_volume),
            Clock(**self._calendar),
            Clock(**self._clock),
            Battery(**self._battery)
            if self.widgets_theme.show_battery
            else Spacer(**self._spacer),
            QuickExit(**self._quick_exit),
            Spacer(**self._spacer),
        ]
        self.other_widgets = [
            Spacer(**self._spacer),
            GroupBox(**self._groupbox),
            CurrentLayoutIcon(**self._current_layout_icon),
            Spacer(**self._spacer),
            WindowName(**self._window_name),
            Spacer(**self._spacer_stretch),
            Clock(**self._calendar),
            Clock(**self._clock),
            CurrentScreen(**self._current_screen),
        ]

    def _create_settings(self) -> None:
        """Creates the settings to be used by the widgets."""

        self._spacer_stretch = {**self.widgets_theme.default}
        self._spacer = {**self.widgets_theme.default, "length": 6}
        self._launcher = {
            **{**self.widgets_theme.default, **self.widgets_theme.launcher},
            "font": self.fonts_theme.symbols,
            "text": "",
            "mouse_callbacks": {mouse.LEFT: apps.open_launcher},
        }
        self._groupbox = {
            **{**self.widgets_theme.default, **self.widgets_theme.groupbox},
            "font": self.fonts_theme.symbols,
            "disable_drag": True,
        }
        self._current_layout_icon = {
            **{**self.widgets_theme.default, **self.widgets_theme.current_layout_icon}
        }
        self._window_name = {
            **{**self.widgets_theme.default, **self.widgets_theme.windowname},
            "font": self.fonts_theme.default,
            "empty_group_string": "Desktop",
            "mouse_callbacks": {mouse.MIDDLE: apps.kill_window},
        }
        self._systray = {
            **self.widgets_theme.default,
            "font": self.fonts_theme.symbols,
        }
        self._pulse_volume = {
            **{**self.widgets_theme.default, **self.widgets_theme.volume},
            "font": self.fonts_theme.symbols,
            "mouse_callbacks": {mouse.RIGHT: apps.open_volume_control()},
            "fmt": "墳 {}",
        }
        self._calendar = {
            **{**self.widgets_theme.default, **self.widgets_theme.calendar},
            "font": self.fonts_theme.symbols,
            "mouse_callbacks": {mouse.LEFT: apps.open_calendar},
            "format": " %a, %b %d",
        }
        self._clock = {
            **{**self.widgets_theme.default, **self.widgets_theme.clock},
            "font": self.fonts_theme.symbols,
            "format": " %H:%M",
        }
        self._battery = {
            **{**self.widgets_theme.default, **self.widgets_theme.battery},
            "font": self.fonts_theme.symbols,
        }
        self._quick_exit = {
            **{**self.widgets_theme.default, **self.widgets_theme.quickexit},
            "font": self.fonts_theme.symbols,
            "default_text": "",
            "countdown_format": "{}",
        }
        self._current_screen = {
            **{**self.widgets_theme.default, **self.widgets_theme.current_screen},
            "font": self.fonts_theme.default,
        }
