#!/usr/bin/env python3

import sys

from unifying import *

if len(sys.argv) < 2:
  print ("Usage: sudo ./logitech-usb-backup.py [firmware-backup.bin] [infopage.bin]")
  sys.exit(1)

dongle = None

path = sys.argv[1]
with open(path, 'wb') as f:

  data = []

  # Instantiate the dongle
  dongle = unifying_dongle()

  for x in range(0x800):
    addr = 16 * x
    h = addr // 256
    l = addr & 255
    response = dongle.send_command(0x21, 0x09, 0x0200, 0x0000, b"\x10" + bytes([h]) + bytes([l]) + b"\x10\x00" + b"\x00"*27)
    data += response[4:20]

  for value in data:
    f.write(bytes([value]))

path = sys.argv[2]
with open(path, 'wb') as f:

  data = []

  for x in range(0xfe0, 0x1000):
    addr = 16 * x
    h = addr // 256
    l = addr & 255
    response = dongle.send_command(0x21, 0x09, 0x0200, 0x0000, b"\x10" + bytes([h]) + bytes([l]) + b"\x10\x00" + b"\x00"*27)
    data += response[4:20]

  for value in data:
    f.write(bytes([value]))

# restart dongle
#response = dongle.send_command(0x21, 0x09, 0x0200, 0x0000, b"\x70" + b"\x00"*31)
