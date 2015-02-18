#!/usr/bin/env python
# coding: latin-1

# Load the XLoBorg library
import XLoBorg

# Tell the library to disable diagnostic printouts
XLoBorg.printFunction = XLoBorg.NoPrint

# Start the XLoBorg module (sets up devices)
XLoBorg.Init()

# Read and display the raw magnetometer readings
print '%+06d,%+06d,%+06d' % XLoBorg.ReadCompassRaw()
