#!/bin/env bash

AUTO_DIR=~/.config/autostart

if [[ ! -d $AUTO_DIR ]]; then 
    sudo mkdir $AUTO_DIR
fi

if [[ -f $AUTO_DIR/tcet-welcome.desktop ]]; then
    echo "Autostart is enabled";
    echo "Do you want to disable it?"
    bool='';
    read -rp "Press y/Y if you want to disable autostart - " bool;
    if [[ $bool == y || $bool == Y ]]; then
        sudo rm $AUTO_DIR/tcet-welcome.desktop;
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
        sudo cp /usr/share/applications/tcet-welcome.desktop $AUTO_DIR;
        echo "Autostart is enabled now"
    else
        echo "Autostart is still disabled"
    fi
fi
