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
git clone https://github.com/tcet-opensource/tcet-linux-welcome.git ~/.local/share/tcet-linux-welcome
```

Note: The repo should be cloned at `~/.local/share` otherwise the app wouldn't work

### Autostart

To make the app autostart on startup for your user run the following command

```bash
cp tcet-welcome.desktop ~/.config/autostart/
```

Or just run the app and click on `Autostart` button

### Preview

![tcet-wl](https://github.com/tcet-opensource/tcet-linux-welcome/assets/53911515/224d4a3f-d130-4b34-8023-ea0d5e3ee456)

![tcet-about-us](https://github.com/tcet-opensource/tcet-linux-welcome/assets/53911515/f4400501-9fac-4759-a4bb-c2908b178d4c)

