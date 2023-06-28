#!/bin/env bash

if [[ -f $HOME/.config/autostart/tcet-welcome.desktop ]]; then
    echo "Autostart is enabled";
    echo "Do you want to disable it?"
    bool='';
    read -rpn "Press y/Y if you want to disable autostart" bool;
    if [[ $bool == y || $bool == Y ]]; then
        rm "$HOME"/.config/autostart/tcet-welcome.desktop;
    else
        echo "Autostart is still enabled"
    fi
else
    echo "Autostart is disabled";
    echo "Do you want to enable it?"
    bool='';
    read -rp '' bool;
    if [[ $bool == y || $bool == Y ]]; then
        cp ~/.local/share/tcet-linux-welcome/tcet-welcome.desktop "$HOME"/.config/autostart/;
    else
        echo "Autostart is still disabled"
    fi
fi
