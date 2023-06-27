#!/usr/bin/bash

NINSTANCES=$(ps aux | grep 'python ./scripts/about.py'|wc -l )
target="1"

if [ "$NINSTANCES" = "$target" ]
then
  bash -c "python ./scripts/about.py"
fi