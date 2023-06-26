#!/bin/env bash

yad --title "Welcome To Tcet-Linux" \
    --form \
    --columns=2\
    --width=640 \
    --height=380 \
    --text="This is test tcet-linux Welcome app trial" \
    --image=./assets/tcetlinux-logo.png \
    --field="<b>Update the PC</b>":fbtn "bash -c './scripts/update.sh'" \
    --field="<b>Our Github Profile</b>":fbtn "bash -c  './scripts/github.sh'" \
    --field="<b>Our Discord</b>":fbtn "bash -c './scripts/discord.sh'" \
    --field="<b>Update Mirror</b>":fbtn "xfce4-terminal -x './scripts/mirror.sh'" \
    --field="<b>Arch Wiki</b>":fbtn "bash -c './scripts/archwiki.sh'" \
    --field="<b>Screen Resolution</b>":fbtn "xfce4-terminal -x  './scripts/screen-resolution.sh'" \
    --button=Exit:1