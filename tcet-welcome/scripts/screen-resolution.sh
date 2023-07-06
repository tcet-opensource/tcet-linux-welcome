#!/bin/env bash
 
# get no of displays connected
 
NDISPLAYS=$(xrandr | grep " connected" |wc -l) 
 
if [ -f /etc/profile.d/monitor.sh ];then
	sudo bash -c 'rm /etc/profile.d/monitor.sh ; touch /etc/profile.d/monitor.sh;chmod 742 /etc/profile.d/monitor.sh'
else
    sudo bash -c ' touch /etc/profile.d/monitor.sh ; chmod 742 /etc/profile.d/monitor.sh'
fi
 
for i in $(seq 1 $NDISPLAYS)
do
    # Get list of displays 
    tempDispList=$(xrandr | grep " connected" | cut -d " " -f 1 )
    tempDisp=$(echo $tempDispList| cut -d " " -f "$i")
 
    echo $tempDisp
 
    # Change resolution of individual displays
    xrandr --output $tempDisp --mode 1920x1080
    echo "xrandr --output $tempDisp --mode 1920x1080" >> /etc/profile.d/monitor.sh
 
done
 
#change permissions of the startup script
sudo chmod 755 /etc/profile.d/monitor.sh