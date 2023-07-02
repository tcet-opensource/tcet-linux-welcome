#!/bin/env bash

pkexec reflector --country "United States, France, Germany,India, Norway, Australia, Sweden" \
    --verbose \
    --sort rate \
    --protocol https,http \
    --latest 20 \
    --save /etc/pacman.d/mirrorlist
