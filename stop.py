import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from time       import sleep
import sys
import rpyc
import random

conn = rpyc.classic.connect('ev3dev.local') # host name or IP address conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotelyf the EV3
ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely
m1 = ev3.LargeMotor('outB')
assert m1.connected, "Connecter un large motor sur outB"
m2 = ev3.LargeMotor('outC')
assert m2.connected, "Connecter un large motor sur outC"
m3 = ev3.MediumMotor('outA')

m1.run_forever(speed_sp = 0)
m2.run_forever(speed_sp = 0)
