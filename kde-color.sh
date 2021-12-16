#!/bin/sh

# Set window border colors in Qubes dom0 (KDE)
# tasket@github.com

colors[0]="black 0,0,0"
colors[1]="gray 127,131,127"
colors[2]="purple 114,67,120"
colors[3]="blue 14,77,162"
colors[4]="green 64,145,64"
colors[5]="yellow 190,164,70"
colors[6]="orange 166,82,20"
colors[7]="red 166,55,59"

kcpath=~/.local/share/qubes-kde
mkdir -p $kcpath

for i in {0..7}; do 

  read name tuple <<<${colors[i]}
  #echo "$i $name and then $tuple"

  echo "
[Colors:Window]
BackgroundNormal=$tuple
[WM]
activeBackground=$tuple
inactiveBackground=$tuple
" >$kcpath/$name'.colors'

done
