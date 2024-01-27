#!/usr/bin/bash

case $XDG_CURRENT_DESKTOP in "GNOME") bash -c 'gnome-control-center display';;
"XFCE") bash -c 'xfce4-display-settings';;
*) yad --image="dialog-question" --title "Alert" --text "Can't recongnize desktop environment" --button="yad-ok:0";;
esac