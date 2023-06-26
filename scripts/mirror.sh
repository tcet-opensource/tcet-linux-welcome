#!/bin/bash
reflector --country "India, United States, France, Germany, Norway, Australia, Sweden" \
  --verbose \
  --sort rate \
  --protocol https,http \
  --latest 10 \
  --save /etc/pacman.d/mirrorlist
