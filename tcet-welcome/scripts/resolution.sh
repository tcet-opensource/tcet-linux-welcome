#!/usr/bin/bash

case $XDG_CURRENT_DESKTOP in "GNOME") bash -c 'gnome-control-center display';;
"XFCE") bash -c 'xfce4-display-settings';;
*) echo "Sorry No DE";;
esac