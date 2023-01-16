"""Provides the widgets to be used by the bar(s)."""

from libqtile import widget

from .apps import Apps
from .io import mouse
from .settings import WidgetsSettings
from .theme import FontsTheme, WidgetsTheme


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
        fonts_theme: FontsTheme,
        widgets_theme: WidgetsTheme,
        widgets_settings: WidgetsSettings,
        apps: Apps,
    ) -> None:

        self.fonts_theme: FontsTheme = fonts_theme
        self.widgets_theme: WidgetsTheme = widgets_theme
        self.widgets_settings: WidgetsSettings = widgets_settings
        self.apps: Apps = apps
        self._create_settings()
        self.main_widgets = [
            widget.Spacer(**self._spacer),
            widget.TextBox(**self._launcher),
            widget.Spacer(**self._spacer),
            widget.GroupBox(**self._groupbox),
            widget.CurrentLayoutIcon(**self._current_layout_icon),
            widget.Spacer(**self._spacer),
            widget.WindowName(**self._window_name),
            widget.Spacer(**self._spacer_stretch),
            widget.Systray(**self._systray),
            widget.Spacer(**self._spacer),
            widget.TextBox(**self._volume_icon),
            widget.PulseVolume(**self._pulse_volume),
            widget.TextBox(**self._calendar_icon),
            widget.Clock(**self._calendar),
            widget.TextBox(**self._clock_icon),
            widget.Clock(**self._clock),
            widget.Battery(**self._battery)
            if self.widgets_settings.show_battery
            else widget.Spacer(**self._spacer),
            widget.QuickExit(**self._quick_exit),
            widget.Spacer(**self._spacer),
        ]
        self.other_widgets = [
            widget.Spacer(**self._spacer),
            widget.GroupBox(**self._groupbox),
            widget.CurrentLayoutIcon(**self._current_layout_icon),
            widget.Spacer(**self._spacer),
            widget.WindowName(**self._window_name),
            widget.Spacer(**self._spacer_stretch),
            widget.CurrentScreen(**self._current_screen),
        ]

    def _create_settings(self) -> None:
        """Creates the settings to be used by the widgets."""

        self._spacer_stretch = {**self.widgets_theme.default}
        self._spacer = {**self.widgets_theme.default, "length": 6}
        self._launcher = {
            **{**self.widgets_theme.default, **self.widgets_theme.launcher},
            "font": self.fonts_theme.symbols,
            "text": "",
            "mouse_callbacks": {mouse.LEFT: self.apps.open_launcher},
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
            "mouse_callbacks": {mouse.MIDDLE: self.apps.kill_window},
        }
        self._systray = {
            **self.widgets_theme.default,
            "font": self.fonts_theme.symbols,
        }
        self._volume_icon = {
            **{**self.widgets_theme.default, **self.widgets_theme.volume},
            "font": self.fonts_theme.symbols,
            "mouse_callbacks": {mouse.RIGHT: self.apps.open_volume_control},
            "text": "墳",
        }
        self._pulse_volume = {
            **{**self.widgets_theme.default, **self.widgets_theme.volume},
            "font": self.fonts_theme.default,
            "mouse_callbacks": {mouse.RIGHT: self.apps.open_volume_control},
        }
        self._calendar_icon = {
            **{**self.widgets_theme.default, **self.widgets_theme.calendar},
            "font": self.fonts_theme.symbols,
            "mouse_callbacks": {mouse.LEFT: self.apps.open_calendar},
            "text": "",
        }
        self._calendar = {
            **{**self.widgets_theme.default, **self.widgets_theme.calendar},
            "font": self.fonts_theme.default,
            "mouse_callbacks": {mouse.LEFT: self.apps.open_calendar},
            "format": "%a, %b %d",
        }
        self._clock_icon = {
            **{**self.widgets_theme.default, **self.widgets_theme.clock},
            "font": self.fonts_theme.symbols,
            "text": "",
        }
        self._clock = {
            **{**self.widgets_theme.default, **self.widgets_theme.clock},
            "font": self.fonts_theme.default,
            "format": "%H:%M",
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
