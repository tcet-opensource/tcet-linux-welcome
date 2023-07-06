#!/usr/bin/bash

NINSTANCES=$(ps aux | grep python\ $HOME/.local/share/tcet-welcome/scripts/about.py | wc -l )
target="1"

if [ "$NINSTANCES" = "$target" ]
then
  bash -c "python ~/.local/share/tcet-welcome/scripts/about.py"
fi
