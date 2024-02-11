#!/bin/env bash
TERM=""

case $XDG_CURRENT_DESKTOP in "GNOME") TERM=kgx;;
"XFCE") TERM=xfce4-terminal;;
*) yad --image="dialog-question" --title "Alert" --text "Can't recongnize desktop environment" --button="yad-ok:0";;
esac

$TERM -e "pkexec pacman --noconfirm -Syyu"

