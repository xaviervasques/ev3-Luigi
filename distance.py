#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from time       import sleep
import sys
import rpyc
import random

def beeps( nb ):  #plusieurs bips
    conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
    ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely
    for i in range (0,nb):
        ev3.Sound.beep()
        sleep(.2)


def distance():

    conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
    ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely

    m1 = ev3.LargeMotor('outB')
    assert m1.connected, "Connecter un large motor sur outB"
    m2 = ev3.LargeMotor('outC')
    assert m2.connected, "Connecter un large motor sur outC"
    m3 = ev3.MediumMotor('outA')
    
    
    m3.run_to_rel_pos(position_sp=-45, speed_sp=100, stop_action="brake")
    m3.wait_while('running')
    m3.run_to_rel_pos(position_sp=45, speed_sp=100, stop_action="brake")
    m3.wait_while('running')
    m3.run_to_rel_pos(position_sp=45, speed_sp=100, stop_action="brake")
    m3.wait_while('running')
    m3.run_to_rel_pos(position_sp=-45, speed_sp=100, stop_action="brake")
    m3.wait_while('running')

    beeps(1)

    ir = ev3.InfraredSensor()
    assert ir.connected, "Connecter svp le senseur infrarouge a un des ports"
    
    # Connect remote control
    rc = ev3.RemoteControl();
    assert rc.connected, "Remote control does not work"

    #Mettre le senseur infrarouge en mode de proximite
    ir.mode = 'IR-PROX'
    
    cl = ev3.ColorSensor()
    assert cl.connected, "Connecter svp le senseur de couleur a un des ports"

    # Mettre le senseur en mode RGB
    cl.mode='RGB-RAW'

    cur_distance = ir.value()
    # print "Distance %d cur_distance de depart" % cur_distance

    m1.run_forever(speed_sp = 0)
    m2.run_forever(speed_sp = 0)
    
    # Turn leds off
    ev3.Leds.all_off()
    
    def stop_luigi():
    
        conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
        ev3 = conn.modules['ev3dev.ev3']# import ev3dev.ev3 remotely
    
        ev3.Sound.beep().wait()
    
        m1.run_forever(speed_sp = 0)
        
        m2.run_forever(speed_sp = 0)
    
    
    while ir.value() > 2  : # While no button is pressed.
        

        cur_distance = ir.value()
        while ir.value() > 50  : # While no button is pressed.
            cur_distance = ir.value()
            m1.run_forever(speed_sp = 300 - 2000/(cur_distance + 3))
            m2.run_forever(speed_sp = 300 - 2000/(cur_distance + 3))


        m1.run_forever(speed_sp = 0)
        m2.run_forever(speed_sp = 0)
        m1.run_forever(speed_sp = -300)
        m2.run_forever(speed_sp = -300)


        
        if random.randint(0, 1) == 0:
            ev3.Sound.speak('Ou la la la la')
        else:
            ev3.Sound.speak('Oops')

        if random.randint(0, 1) == 0:
            m2.run_timed(speed_sp=500)
        else:
            m1.run_timed(speed_sp=500)

        sleep(1.5)
        
        sleep(0.6)


    ev3.Sound.beep().wait()
    m1.run_forever(speed_sp = 0)
    m2.run_forever(speed_sp = 0)

    beeps(2)
    sleep(1)



