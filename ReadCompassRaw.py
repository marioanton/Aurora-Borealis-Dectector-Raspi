#!/usr/bin/env python
# coding: latin-1
import optparse
import signal
import re
import subprocess
import urllib2
import os
import sys
import urllib
import re
import io
from subprocess import call
from StringIO import StringIO

# Load the XLoBorg library
import XLoBorg
import math
# Tell the library to disable diagnostic printouts
XLoBorg.printFunction = XLoBorg.NoPrint

# Start the XLoBorg module (sets up devices)
XLoBorg.Init()
values =  str(XLoBorg.ReadCompassRaw())
x, y, z = values.split(' ', 3)
x = x.replace(',', '')
x = x.replace('(', '')
#x = x.replace('-', '')
y = y.replace(',', '')
z = z.replace(')', '')

kp = (math.sqrt((int(x) * int(x)) + (int(y) * int(y)) + (int(z) * int(z))))
COLOR = "green"
# converted to Xymon
LINE = ""
BB = "/usr/lib/hobbit/client/bin/bb"
BBDISP = "192.168.0.198"
MACHINE = "rasp"
from datetime import date, datetime, timedelta
d = datetime.now()
P1 = "\"status+25h " + MACHINE + ".kp " + COLOR + d.strftime(" %a %b %d %H:%M:%S %Z %Y") + " - \n" + LINE + "\nkp: " + str(kp) + "\""
LL = BB + " " + BBDISP + " " + P1
print '%s' % (LL)
os.system(LL)
