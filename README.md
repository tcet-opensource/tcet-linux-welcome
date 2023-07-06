# TCET linux welcome

Tcet-linux-welcome is a simple welcome app specifically written for [TCET Linux](https://github.com/tcet-opensource/tcet-linux) but it can be used for any Arch based distro or Arch Linux itself.

The app is written using [YAD](https://github.com/v1cont/yad) and GTK-3.0.

## Installation

First make sure `yad` should be installed

```bash
sudo pacman -S yad
```

Then clone the repository

<!--- This will need to be changed in future, like we can link to tar.zst  -->
```bash
git clone https://github.com/tcet-opensource/tcet-linux-welcome.git ~/.local/share/tcet-linux-welcome -b 4-create-welcome-app-based-on-yad && cd ~/.local/share/tcet-linux-welcome && cp -r tcet-welcome ~/.local/share/ && sudo cp welcome /usr/bin
```

Note: The repo should be cloned at `~/.local/share` otherwise the app wouldn't work

### Autostart

To make the app autostart on startup for your user run the following command

```bash
cp tcet-welcome.desktop ~/.config/autostart/
```

Or just run the app and click on `Autostart` button

### Preview

![main-page](https://github.com/tcet-opensource/tcet-linux-welcome/assets/53911515/b21c977c-0ed5-4dab-8e6e-8d51ba232919)

![about-us](https://github.com/tcet-opensource/tcet-linux-welcome/assets/53911515/1ea631dd-b7fa-4b22-99ff-fb10f6f1e7fb)

