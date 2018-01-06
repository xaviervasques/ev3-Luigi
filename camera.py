import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
import rpyc

def camera():
    conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
    ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely
    
    def limit_speed(speed):
        conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
        ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely

        """ Limit speed in range [-900,900] """
        if speed > 900:
            speed = 900
        elif speed < -900:
            speed = -900
        return speed

    # Connect Pixy camera and set mode
    pixy = ev3.Sensor(address = INPUT_3)
    assert pixy.connected, "Error while connecting Pixy camera"
    pixy.mode = 'SIG1'

    # Connect TouchSensor (to stop script)
    ts = ev3.TouchSensor(INPUT_1)
    assert ts.connected, "Error while connecting TouchSensor"

    # Connect LargeMotors
    rmotor = ev3.LargeMotor(OUTPUT_C)
    assert rmotor.connected, "Error while connecting right motor"
    lmotor = ev3.LargeMotor(OUTPUT_B)
    assert lmotor.connected, "Error while connecting left motor"

    # Defining constants
    X_REF = 128  # X-coordinate of referencepoint
    Y_REF = 150  # Y-coordinate of referencepoint
    
    KP = 0.1 # Proportional constant PID-controller
    KI = 0.01    # Integral constant PID-controller
    KD = 0.005   # Derivative constant PID-controller
    GAIN = 10    # Gain for motorspeed

    # Initializing PID variables
    integral_x = 0
    derivative_x = 0
    last_dx = 0
    integral_y = 0
    derivative_y = 0
    last_dy = 0

    while not ts.value():
        if pixy.value(0) > 0:
            ev3.Sound.speak('I see it, I am following !')
            x = pixy.value(1)             # X-centroid of largest SIG1-object
            y = pixy.value(2)             # Y-centroid of largest SIG1-object
            dx = X_REF - x                # Error in reference to X_REF
            integral_x = integral_x + dx  # Calculate integral for PID
            derivative_x = dx - last_dx   # Calculate derivative for PID
            speed_x = KP*dx + KI*integral_x + KD*derivative_x  # Speed in X-direction
            dy = Y_REF - y       # Error in reference to Y_REF
            integral_y = integral_y + dy  # Calculate integral for PID
            derivative_y = dy - last_dy   # Calculate derivative for PID
            speed_y = KP*dy + KI*integral_y + KD*derivative_y  # Speed in Y-direction
            # Calculate motorspeed out of speed_x and speed_y
            lmotor.run_forever(speed_sp = limit_speed(GAIN*(speed_y - speed_x)))
            rmotor.run_forever(speed_sp = limit_speed(GAIN*(speed_y + speed_x)))
            

            last_dx = dx     # Set last error for x
            last_dy = dy     # Set last error for y
        else:
            rmotor.stop()    # SIG1 not detected, stop motors
            lmotor.stop()

    # End of script, stop motors
    rmotor.stop()
    lmotor.stop()
