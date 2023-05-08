# qtile

This is my qtile configuration.

## Requirements

Some of the requirements are optional depending on whether you will use my
configuration for xorg or wayland.

- `xorg` &/or `wayland`
- `qtile`
- `python-pywlroots` (wayland)
- `python-dbus-next`
- `python-pyxdg`
- FONTS:
    - `ttf-ibm-plex`
    - `ttf-ibmplex-mono-nerd`
- TERMINAL: `kitty`
- LOCKER: `light-locker`
- LAUNCHER: `rofi` (xorg) &/or `wofi` (wayland)
- SCREENSHOTS: `xfce4-screenshooter`
- VOLUME:
    - `pamixer`
    - `pavucontrol`
- STARTUP:
    - `gnome-keyring`
    - `network-manager-applet`
    - `blueman`
    - `dunst`
    - `emacs`
    - `redshift` (xorg) &/or `gammastep` (wayland)
    - `picom` (xorg)
    - `xfce4-clipman-plugin`

## Keybindings

| Keybinding        | Action                               |
|-------------------|--------------------------------------|
| SUPER+CTRL+Q      | Close focused window                 |
| SUPER+F           | Toggle fullscreen for focused window |
| SUPER+SPACE       | Toggle floating for focused window   |
| SUPER+SHIFT+SPACE | Move all floating windows to front   |
| SUPER+H           | Traverse left                        |
| SUPER+J           | Traverse down                        |
| SUPER+K           | Traverse up                          |
| SUPER+L           | Traverse right                       |
| SUPER+SHIFT+H     | Shuffle left                         |
| SUPER+SHIFT+J     | Shuffle down                         |
| SUPER+SHIFT+K     | Shuffle up                           |
| SUPER+SHIFT+L     | Shuffle right                        |
| SUPER+SHIFT+Z     | Swap focused window to main (xmonad) |
| SUPER+ALT+J       | Grow left                            |
| SUPER+ALT+J       | Grow down                            |
| SUPER+ALT+K       | Grow up                              |
| SUPER+ALT+L       | Grow right                           |
| SUPER+ALT+N       | Reset size                           |
| SUPER+ESC         | Reload qtile configuration           |
| SUPER+SHIFT+ESC   | Restart qtile                        |
| SUPER+CTRL+ESC    | Shutdown qtile                       |
| SUPER+TAB         | Next layout                          |
| SUPER+SHIFT+TAB   | Previous layout                      |
| SUPER+ENTER       | Spawn terminal                       |
| SUPER+R           | Spawn launcher                       |
| SUPER+CTRL+L      | Lock screen                          |
| SUPER+PRINT       | Take screenshot                      |
| SUPER+ALT+PRINT   | Take fullscreen screenshot           |
| SUPER+[1,9]       | Change to group [1,9]                |
| SUPER+SHIFT+[1,9] | Move window to group [1,9]           |
