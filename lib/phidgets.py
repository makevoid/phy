#!/usr/bin/env python

# requirements: libphidget & PhidgetPython
# apt-get install libphidgets-dev python-phidgets (?)


from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *

import os
import sys
import time
import urllib
import urlparse
import time



interfaceKit = InterfaceKit()
interfaceKit.openPhidget()
try:
  interfaceKit.waitForAttach(10000)
except:
  interfaceKit.closePhidget()
  print "Cannot connect to Phidgets!"
  sys.exit(1)


def state():
  return interfaceKit.getOutputState(0)
  
def get_state():
  print "state open: "+str(interfaceKit.getOutputState(0))

def open():
  interfaceKit.setOutputState(0,1)

def close():
  interfaceKit.setOutputState(0,0)

def open_momentary():
  print "opening..."
  open()
  time.sleep(1)
  close()
  
get_state()
open_momentary()
get_state()

interfaceKit.closePhidget()
