#!/usr/bin/env python3

# Nous utilisons la telecommande pour controler les 2 moteurs
# Boutons rouge: moteur de gauche
# Boutons bleu:  moteur de droite
# Les leds montrent la direction du mouvement

from time import sleep
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
import sys
import rpyc

def telecommand():
    conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
    ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely
    
    # lmotor: moteur de gauche  rmotor: moteur de droite
    lmotor = ev3.LargeMotor('outB')
    rmotor = ev3.LargeMotor('outC')
    assert lmotor.connected, "Connecter le moteur gauche sur outB"
    assert rmotor.connected, "Connecter le moteur droite sur outC"

    ev3.Sound.speak('Hey').wait()

    ir = ev3.InfraredSensor()  #distance et telecommande
    assert ir.connected, "Connecter svp le senseur infrarouge a un des ports"

    # Connect remote control
    rc = ev3.RemoteControl();
    assert rc.connected, "Remote control does not work"

    # Initialize button handler
    #button = Button()   # not working so disabled

    # Turn leds off
    ev3.Leds.all_off()

    def tourne(moteur, led_group, direction):
        conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
        ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely
        def on_press(state):
            conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
            ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely
            if state:
                moteur.run_forever(speed_sp=600*direction)
            else:
                # sinon stop
                print('processus 3')
                moteur.stop(stop_action='brake')
                print('processus 4')
                

        return on_press

    # Assigne un event handler a chaque bouton
    rc.on_red_up    = tourne(lmotor, Leds.LEFT,   1)
    rc.on_red_down  = tourne(lmotor, Leds.LEFT,  -1)
    rc.on_blue_up   = tourne(rmotor, Leds.RIGHT,  1)
    rc.on_blue_down = tourne(rmotor, Leds.RIGHT, -1)

    # Boucle de travail
    while True:
        ir.mode = 'IR-REMOTE'  # mode telecommande
        rc.process()
        sleep(0.01)
        
        ir.mode = 'IR-PROX'	   # mode distance
        cur_distance = ir.value()

        
        if cur_distance >= 0 and cur_distance <= 8:
            lmotor.stop(stop_action='brake')
            rmotor.stop(stop_action='brake')
                    
            ev3.Sound.beep()
            sleep(1.0)
                            
            sys.exit(0)
