#!/bin/python2

import os
import shutil
import subprocess
from time import time

# Error if not Qubes 3.x
p = subprocess.check_call(["grep","-i","release 3","/etc/qubes-release"])

hours = 12 # Hours between snapshots
snnum = 4  # Number of snapshots to retain
sndir = "/Snapshots" # Directory containting snapshots


if not os.path.isdir(sndir):
  os.mkdir(sndir)

if os.path.isdir(sndir+"/root1"):
  dt = os.popen("/usr/sbin/btrfs subvolume show "+sndir+"/root1 " +
                "|grep 'Creation time:' |cut -f 4 |date -f - +%s").readline()
  # datetime.strptime(dt,"%Y-%m-%d %H:%M:%S %z")
  ctime = int(dt)

  if ( int(time()) - ctime ) < ( hours *60 *60 -1 ):
    exit(0)

  res = os.system("/usr/sbin/btrfs subvolume list -o "+sndir+" |grep "+sndir+"/root"+str(snnum))
  if res < 256:
    os.system("/usr/sbin/btrfs subvolume delete -c "+sndir+"/root"+str(snnum))

  print "Renaming:"
  for i in reversed(range(1, snnum)):
    if os.path.isdir(sndir+"/root"+str(i)):
      shutil.move(sndir+"/root"+str(i), sndir+"/root"+str(i+1))

#exit(0)
os.system("/usr/sbin/btrfs subvolume snapshot -r / "+sndir+"/root1")

