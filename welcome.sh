#!/bin/env bash

yad --title "Welcome To Tcet-Linux" --form --columns=2 --width=640 --height=300 --text="This is test tcet-linux Welcome app trail" --image=./assets/tcetlinux-logo.png --center \
    --field="<b>Update</b>":fbtn "bash -c './scripts/update.sh'" \
    --field="<b>Github</b>":fbtn "bash -c  './scripts/github.sh'" \
    --field="<b>Discord</b>":fbtn "bash -c './scripts/discord.sh'" \
    --field="<b>Update Mirror</b>":fbtn "xfce4-terminal -x './scripts/mirror.sh'" \
    --field="<b>TBD</b>":fbtn "echo 'TO BE DECIDED'" \
    --field="<b>Screen Resolution</b>":fbtn "xfce4-terminal -x  './scripts/screen-resolution.sh'" \
    --button=Exit:1
