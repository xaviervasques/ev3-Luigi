import ev3dev.ev3 as ev3
from chatterbot import ChatBot
import rpyc
import chatbot
import distance
import telecommand
import camera
import danse

conn = rpyc.classic.connect('ev3dev.local') # host name or IP address of the EV3
ev3 = conn.modules['ev3dev.ev3']

#chatbot.chatbot()
#telecommand.telecommand()
distance.distance()
#camera.camera()
#danse.danse()



