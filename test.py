import rpyc
conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']      # import ev3dev.ev3 remotely
#m = ev3.LargeMotor('outA')
#m=ev3.Motor('outA')
#m.run_timed(time_sp=1000, speed_sp=600)
m = ev3.LargeMotor('outC')
m.run_timed(time_sp=3000, speed_sp=500)
#m = ev3.LargeMotor('outB')
#m.run_timed(time_sp=3000, speed_sp=500)
ev3.Sound.speak('Welcome to the E V 3 dev project!').wait()
