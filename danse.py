import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
import rpyc
from time import sleep
from random import randint

# Install aplay (sudo apt-get install alsa-base alsa-utils) in Luigi OS

import wave
import contextlib

from time import sleep

def danse():
    
    conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
    ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely
    
    m1 = ev3.LargeMotor('outB')
    assert m1.connected, "Connecter un large motor sur outB"
    m2 = ev3.LargeMotor('outC')
    assert m2.connected, "Connecter un large motor sur outC"
    m3 = ev3.MediumMotor('outA')
    
    #Sound.set_volume(100, channel=None)
    
    file_wav = 'Music/Jain_Makeba.wav'
    #ev3.Sound.play(file_wav)

    with contextlib.closing(wave.open(file_wav,'r')) as f:
        frames = f.getnframes()
        print(frames)
        rate = f.getframerate()
        print(rate)
        duration = frames / float(rate)
    print(duration)

    seconds = lambda n: (sleep(1) or i if i else i for i in range(n+1))
    for i in seconds(int(duration)):              # une itération toutes les secondes
        print("time: %ds" % i)
        num_speed = randint(300,600)
        num_speed_1 = randint(500,900)
        num_speed_2 = randint(500,900)
        right_left = randint(0,1)
        neg_pos = randint(0,1)
        m3.run_to_rel_pos(position_sp=20, speed_sp=num_speed, stop_action="brake")
        m3.run_to_rel_pos(position_sp=-20, speed_sp=num_speed, stop_action="brake")
        m3.run_to_rel_pos(position_sp=20, speed_sp=num_speed, stop_action="brake")
        m3.run_to_rel_pos(position_sp=-20, speed_sp=num_speed, stop_action="brake")
        if right_left == 1:
            if neg_pos == 1:
                m1.run_forever(speed_sp=num_speed_1)
                #m1.stop()
                m2.run_forever(speed_sp=-num_speed_2)
                #m2.stop()
                m1.run_forever(speed_sp=-num_speed_1)
                #m1.stop()
                m2.run_forever(speed_sp=num_speed_2)
                #m2.stop()
            else:
                m1.run_forever(speed_sp=-num_speed_1)
                #m1.stop()
                m2.run_forever(speed_sp=num_speed_2)
                #m2.stop()
                m1.run_forever(speed_sp=num_speed_1)
                #m1.stop()
                m2.run_forever(speed_sp=-num_speed_2)
                #m2.stop()
        else:
            if neg_pos == 1:
                m2.run_forever(speed_sp=num_speed_2)
                #m2.stop()
                m1.run_forever(speed_sp=-num_speed_1)
                #m1.stop()
                m2.run_forever(speed_sp=-num_speed_2)
                #m2.stop()
                m1.run_forever(speed_sp=num_speed_1)
                #m1.stop()
            else:
                m2.run_forever(speed_sp=-num_speed_2)
                #m2.stop()
                m1.run_forever(speed_sp=num_speed_1)
                #m1.stop()
                m2.run_forever(speed_sp=num_speed_2)
                #m2.stop()
                m1.run_forever(speed_sp=-num_speed_1)
                #m1.stop()

