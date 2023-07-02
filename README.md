# TCET linux welcome

Tcet-linux-welcome is a simple welcome app written for [TCET Linux](https://github.com/tcet-opensource/tcet-linux).

The app is written using [YAD](https://github.com/v1cont/yad) and GTK-3.0.

## Installation

First make sure `yad` should be installed

```bash
sudo pacman -S yad

```

Then clone the repository 

```bash
git clone -b 4-create-welcome-app-based-on-yad https://github.com/tcet-opensource/tcet-linux-welcome.git ~/.local/share/tcet-linux-welcome
```

Note: The repo should be cloned at `~/.local/share` otherwise the app wouldn't work

### Autostart

To make the app autostart on startup for your user run the following command

```bash
cp tcet-welcome.desktop ~/.config/autostart/
```

Or just run the app and click on `Autostart` button

![image](https://github.com/tcet-opensource/tcet-linux-welcome/assets/53911515/b58ac6c9-6fd0-437f-9007-805c480ecdf6)
