#!/bin/bash
reflector --country "India, America, France, germany" \
  --sort rate \
  --protocol https \
  --latest 5 \
  --save /etc/pacman.d/mirrorlist
