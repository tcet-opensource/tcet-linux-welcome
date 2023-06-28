#!/bin/env bash

if [[ ! -d $HOME/.config/autostart ]]; then 
    mkdir "$HOME"/.config/autostart
fi

if [[ -f $HOME/.config/autostart/tcet-welcome.desktop ]]; then
    echo "Autostart is enabled";
    echo "Do you want to disable it?"
    bool='';
    read -rp "Press y/Y if you want to disable autostart - " bool;
    if [[ $bool == y || $bool == Y ]]; then
        rm "$HOME"/.config/autostart/tcet-welcome.desktop;
        echo "Autostart is disabled now"
    else
        echo "Autostart is still enabled"
    fi
else
    echo "Autostart is disabled";
    echo "Do you want to enable it?"
    bool='';
    read -rp "Press y/Y if you want to enable autostart - " bool;
    if [[ $bool == y || $bool == Y ]]; then
        cp ~/.local/share/tcet-linux-welcome/tcet-welcome.desktop "$HOME"/.config/autostart/;
        echo "Autostart is enabled now"
    else
        echo "Autostart is still disabled"
    fi
fi
