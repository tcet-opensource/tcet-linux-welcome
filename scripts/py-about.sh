#!/usr/bin/bash

NINSTANCES=$(ps aux | grep python\ $HOME/.local/share/tcet-linux-welcome/scripts/about.py | wc -l )
target="1"

if [ "$NINSTANCES" = "$target" ]
then
  bash -c "python ~/.local/share/tcet-linux-welcome/scripts/about.py"
fi
