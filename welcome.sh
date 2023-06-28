#!/bin/env bash

DIR=~/.local/share/tcet-linux-welcome

yad --title "Welcome" \
    --form \
    --window-icon=$DIR/assets/tcetlinux-logo.png \
    --columns=2\
    --rows=5 \
    --width=640 \
    --height=380 \
    --text="<b>Welcome To TCET-Linux</b>" \
    --image=$DIR/assets/tcetlinux-logo.png \
    --field="<b>Update this PC</b>":fbtn "bash -c '$DIR/scripts/update.sh'" \
    --field="<b>Fix Screen Resolution</b>":fbtn "xfce4-terminal -x  '$DIR/scripts/screen-resolution.sh'" \
    --field="<b>Our Discord</b>":fbtn "bash -c '$DIR/scripts/discord.sh'" \
    --field="<b>Arch Wiki</b>":fbtn "bash -c '$DIR/scripts/archwiki.sh'" \
    --field="<b>Update Mirror</b>":fbtn "xfce4-terminal -x '$DIR/scripts/mirror.sh'" \
    --field="<b>Our Github Profile</b>":fbtn "bash -c  '$DIR/scripts/github.sh'" \
    --field="<b>Arch AUR</b>":fbtn "bash -c '$DIR/scripts/aur.sh'" \
    --field="<b>About US</b>":fbtn "bash -c  '$DIR/scripts/py-about.sh'" \
    --field="<b>Autostart</b>":fbtn " xfce4-terminal -x '$DIR/scripts/autostart.sh'"\
    --button=Exit:1 \

