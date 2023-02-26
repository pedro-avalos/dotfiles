from libqtile import hook
from libqtile.backend.base import Window
from libqtile.log_utils import logger


@hook.subscribe.client_new
def float_windows(window):
    if type(window) is Window:
        state = window.surface.toplevel._ptr.current
        if 0 < state.max_width < 1920:
            window.floating = True
        else:
            logger.debug(
                (window.name, window.get_wm_class(), (state.min_width, state.max_width))
            )
