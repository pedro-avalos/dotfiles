"""Provides the widgets to be used by the bar(s)."""

from libqtile import qtile, widget

from . import compositor
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
            widget.Notify(**self._notify),
            widget.Spacer(**self._spacer_stretch),
            widget.Clock(**self._clock),
            widget.Spacer(**self._spacer_stretch),
            # XXX: Systray does not support Wayland
            widget.Systray(**self._systray)
            if compositor.name == "x11"
            else widget.StatusNotifier(**self._systray),
            widget.Spacer(**self._spacer),
            widget.Volume(**self._volume),
            # Battery indicator is optional
            widget.Battery(**self._battery)
            if self.widgets_settings.show_battery
            else widget.TextBox(**self._none),
            widget.KeyboardLayout(**self._keyboard_layout),
            widget.QuickExit(**self._quick_exit),
            widget.Spacer(**self._spacer),
        ]
        self.other_widgets = [
            widget.Spacer(**self._spacer),
            widget.GroupBox(**self._groupbox),
            widget.CurrentLayoutIcon(**self._current_layout_icon),
            widget.Spacer(**self._spacer),
            widget.Spacer(**self._spacer_stretch),
            widget.CurrentScreen(**self._current_screen),
        ]

    def _create_settings(self) -> None:
        """Creates the settings to be used by the widgets."""

        self._spacer_stretch = {**self.widgets_theme.default}
        self._spacer = {**self.widgets_theme.default, "length": 6}
        self._none = {**self.widgets_theme.default, "text": "", "length": 0}
        self._launcher = {
            **{**self.widgets_theme.icon, **self.widgets_theme.launcher},
            "font": self.fonts_theme.symbols,
            "text": "",
            "mouse_callbacks": {mouse.LEFT: self.apps.open_launcher},
        }
        self._groupbox = {
            **{**self.widgets_theme.icon, **self.widgets_theme.groupbox},
            "font": self.fonts_theme.symbols,
            "disable_drag": True,
        }
        self._current_layout_icon = {
            **{**self.widgets_theme.icon, **self.widgets_theme.current_layout_icon}
        }
        self._notify = {
            **{**self.widgets_theme.default, **self.widgets_theme.notify},
            "font": self.fonts_theme.default,
        }
        self._systray = {
            **self.widgets_theme.default,
        }
        self._volume = {
            **{**self.widgets_theme.default, **self.widgets_theme.volume},
            "font": self.fonts_theme.default,
            "mouse_callbacks": {mouse.RIGHT: self.apps.open_volume_control},
            "fmt": "奔 {}",
        }
        self._clock = {
            **{**self.widgets_theme.default, **self.widgets_theme.clock},
            "mouse_callbacks": {mouse.LEFT: self.apps.open_calendar},
            "font": self.fonts_theme.default,
            "format": "%Y/%m/%d (%a) %H:%M",
        }
        self._battery = {
            **{**self.widgets_theme.default, **self.widgets_theme.battery},
            "font": self.fonts_theme.symbols,
            "format": "{char} {percent:2.0%}",
            "update_interval": 30,
            "low_percentage": 0.2,
            "full_char": "",
            "charge_char": "",
            "discharge_char": "",
            "empty_char": "",
            "unknown_char": "",
        }
        self._keyboard_layout = {
            **{**self.widgets_theme.default},
            "font": self.fonts_theme.default,
            "configured_keyboards": ["us", "es"],
        }
        self._quick_exit = {
            **{**self.widgets_theme.icon, **self.widgets_theme.quickexit},
            "font": self.fonts_theme.symbols,
            "default_text": "",
            "countdown_format": "{}",
        }
        self._current_screen = {
            **{**self.widgets_theme.icon, **self.widgets_theme.current_screen},
            "font": self.fonts_theme.default,
        }
