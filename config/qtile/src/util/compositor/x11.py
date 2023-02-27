from libqtile import hook, qtile


@hook.subscribe.client_new
def float_windows(window):
    if window.window.get_wm_type == "desktop":
        window.cmd_static(qtile.current_screen.index)
        return
    hints = window.window.get_wm_normal_hints()
    if hints and 0 < hints["max_width"] < 1920:
        window.floating = True