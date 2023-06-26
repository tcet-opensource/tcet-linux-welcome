#!/bin/env bash

# get no of displays connected

NDISPLAYS=$(xrandr | grep " connected" |wc -l) 

for i in $(seq 1 $NDISPLAYS)
do
    # Get list of displays 
    tempDispList=$(xrandr | grep " connected" | cut -d " " -f 1 )

        
    tempDisp=$(echo $tempDispList| cut -d " " -f "$i")

    echo $tempDisp

    # Change resolution of individual displays
    xrandr --output $tempDisp --mode 1920x1080
    
done
