#!/bin/env bash

yad --title "Welcome To Tcet-Linux" --form --columns=3 --width=740 --height=540 --text="This is test tcet-linux Welcome app trail" --image=$HOME/Desktop/welcome/tcetlinux-logo.png  --center \
    --scale 2.0\
    --field="<b>Update</b>":fbtn "gnome-terminal -- sh ./scripts/update.sh" \
    --field="<b>Github</b>":fbtn "sh ./scripts/github.sh" \
    --field="<b>Discord</b>":fbtn "sh ./scripts/discord.sh" \
    --field="<b>Update Mirror</b>":fbtn "gnome-terminal -- sh ./scripts/mirror.sh" \
    --field="<b>Github</b>":fbtn "konsole --noclose -e sh './scripts/drivers'" \
    --field="<b>Discord</b>":fbtn "konsole --noclose -e sh './scripts/flatpakz'" \
    --button=Exit:1
