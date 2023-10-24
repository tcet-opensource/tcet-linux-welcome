#!/usr/bin/bash

NINSTANCES=$(ps aux | grep python\ $HOME/.local/share/tcet-welcome/scripts/install.py | wc -l )
target="1"

if [ "$NINSTANCES" = "$target" ]
then
  bash -c "python ~/.local/share/tcet-welcome/scripts/install.py"
fi

# Check if the Python script is installed
if [ ! -f $HOME/.local/share/tect-welcome/scripts/install.py ];
then
    echo "The Python script is not installed. Please install it and run this script again."
    exit 1
fi
