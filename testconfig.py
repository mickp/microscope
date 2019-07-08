#!/usr/bin/python
"""Config file for devicebase.

Import device classes, then define entries in DEVICES as:
   devices(CLASS, HOST, PORT, other_args)
"""
# Function to create record for each device.
from microscope.devices import device
# Import device modules/classes here.
#from microscope.cameras import andorsdk3
from microscope.cameras import atmcd
#from microscope.cameras import pvcam
import microscope.testsuite.devices as testdevices
import microscope.stages.linkam as linkam
#from microscope.filterwheels import aurox

DEVICES = [
    device(testdevices.TestCamera, '127.0.0.1', 8000,),
    device(testdevices.TestCamera, '127.0.0.1', 8001),
    #device(pvcam.PVCamera, '127.0.0.1', 8001),
    #device(atmcd.AndorAtmcd, '127.0.0.1', 8001),  # , uid='7197'),
    device(testdevices.TestLaser, '127.0.0.1', 8002),
    device(testdevices.TestLaser, '127.0.0.1', 8003),
    device(testdevices.TestFilterWheel, '127.0.0.1', 8004),
    device(testdevices.DummyDSP, '127.0.0.1', 8005),
    device(testdevices.DummySLM, '127.0.0.1', 8006),
    device(testdevices.TestFilterWheel, '127.0.0.1', 8007),
    device(testdevices.TestFilterWheel, '127.0.0.1', 8008,
           conf=dict(filters=[('f0', 505), ('f1',580) , ('f2', 660), None, None, None])),
    #device(aurox.Clarity, '127.0.0.1', 8009),
    #device(linkam.LinkamCMS, '127.0.0.1', 9000, uid=''),
#    device(andorsdk3.AndorSDK3, '127.0.0.1', 8002, uid='VSC-01344'),
]

