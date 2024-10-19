# qtile

This is my qtile configuration.

## Requirements

Some of the requirements are optional depending on whether you will use my
configuration for xorg or wayland.

| Package                  | Required in Xorg | Required in Wayland | Note                       |
| ------------------------ | :--------------: | :-----------------: | -------------------------- |
| `qtile`                  |        ✅        |         ✅          |                            |
| `pywlroots`              |                  |         ✅          |                            |
| `python3-dbus-next`      |        ✅        |         ✅          |                            |
| `python3-xdg`            |        ✅        |         ✅          |                            |
| `fonts-ibm-plex`         |        ✅        |         ✅          | Default font               |
| IBM Plex Mono            |        ✅        |         ✅          | Default icons fonts        |
| `kitty`                  |        ✅        |         ✅          | Terminal                   |
| `light-locker`           |        ✅        |         ✅          | Lock screen functionality  |
| `rofi`                   |        ✅        |                     | Application launcher       |
| `wofi`                   |                  |         ✅          | Application launcher       |
| `xfce4-screenshooter`    |        ✅        |         ✅          | Screenshots utility        |
| `xfce4-clipman`          |        ✅        |         ✅          | Clipboard utility          |
| `pamixer`                |        ✅        |         ✅          | Volume management utility  |
| `pavucontrol`            |        ✅        |         ✅          | Volume management GUI      |
| `gnome-keyring`          |        ✅        |         ✅          | Keyring                    |
| `network-manager-applet` |        ✅        |         ✅          | Network management utility |
| `blueman`                |        ✅        |         ✅          | Bluetooth utility          |
| `dunst`                  |        ✅        |         ✅          | Notifications daemon       |
| `redshift`               |        ✅        |                     | Blue light filter          |
| `gammastep`              |                  |         ✅          | Blue light filter          |
| `picom`                  |        ✅        |                     | X11 compositor             |

## Keybindings

| Keybinding          | Action                               |
| ------------------- | ------------------------------------ |
| `SUPER+CTRL+Q`      | Close focused window                 |
| `SUPER+F`           | Toggle fullscreen for focused window |
| `SUPER+SPACE`       | Toggle floating for focused window   |
| `SUPER+SHIFT+SPACE` | Move all floating windows to front   |
| `SUPER+H`           | Traverse left                        |
| `SUPER+J`           | Traverse down                        |
| `SUPER+K`           | Traverse up                          |
| `SUPER+L`           | Traverse right                       |
| `SUPER+SHIFT+H`     | Shuffle left                         |
| `SUPER+SHIFT+J`     | Shuffle down                         |
| `SUPER+SHIFT+K`     | Shuffle up                           |
| `SUPER+SHIFT+L`     | Shuffle right                        |
| `SUPER+SHIFT+Z`     | Swap focused window to main (xmonad) |
| `SUPER+ALT+H`       | Grow left                            |
| `SUPER+ALT+J`       | Grow down                            |
| `SUPER+ALT+K`       | Grow up                              |
| `SUPER+ALT+L`       | Grow right                           |
| `SUPER+ALT+N`       | Reset size                           |
| `SUPER+ESC`         | Reload qtile configuration           |
| `SUPER+SHIFT+ESC`   | Restart qtile                        |
| `SUPER+CTRL+ESC`    | Shutdown qtile                       |
| `SUPER+TAB`         | Next layout                          |
| `SUPER+SHIFT+TAB`   | Previous layout                      |
| `SUPER+ENTER`       | Spawn terminal                       |
| `SUPER+R`           | Spawn launcher                       |
| `SUPER+CTRL+L`      | Lock screen                          |
| `SUPER+PRINT`       | Take screenshot                      |
| `SUPER+ALT+PRINT`   | Take fullscreen screenshot           |
| `SUPER+[1,9]`       | Change to group [1,9]                |
| `SUPER+SHIFT+[1,9]` | Move window to group [1,9]           |
