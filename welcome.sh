#!/bin/env bash

yad --title "Welcome To Tcet-Linux" --form --columns=3 --width=740 --height=540 --text="This is test tcet-linux Welcome app trail" --image=$HOME/Desktop/welcome/tcetlinux-logo.png  --center \
    --scale 2.0\
    --field="<b>Update</b>":fbtn "xfce4-terminal -x ./scripts/update.sh" \
    --field="<b>Github</b>":fbtn "sh ./scripts/github.sh" \
    --field="<b>Discord</b>":fbtn "sh ./scripts/discord.sh" \
    --field="<b>Update Mirror</b>":fbtn "xfce4-terminal -x ./scripts/mirror.sh" \
    --field="<b>TBD</b>":fbtn "echo "TO BE DECIDED"" \
    --field="<b>Screen Resolution</b>":fbtn "xfce4-terminal -x  './scripts/screen-resolution.sh'" \
    --button=Exit:1
