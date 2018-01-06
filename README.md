# ev3-Luigi
# Lego Mindstorms EV3 Robot
# Programming the Lego Mindstorms EV3 robot

The Lego Mindstorms EV3 robot is a very popular robot that is usually programmed using an icon-based programming system. You can also use ev3dev (www.ev3dev.org) which is a Debian Linux-based OS that runs on several compatible platforms including the Lego Mindstorms EV3 and Raspberry Pi-powered BrickPi. 

With a Linux inside, you can program how you want to program. The EV3 with a Linux computer inside can there be programmed using different programming languages such as Python, C++ or Java. With my 7 years old daughter as product owner and project manager, and myself as doer, we used Python to control sensors and motors of the robot. With some programming skills, it’s quite easy and fun to practice robotics, Internet of Thing and Artificial Intelligence using EV3.

1. The product owner asked to speak with the robot. His name is Luigi! (chatbot.py)

https://www.youtube.com/watch?v=tYnWZpo9_S8&t=1s

The chatbot has been developed using ChatterBot, a Python library using a selection of machine learning algorithms to produce different types of responses and MongoDB to store statements and dialogues. You can find more information about this chatbot in Github: https://github.com/xaviervasques/TheBigBangTheory_Chat

2. Object Tracking and recognition … or rather “Mr. Strong” Tracking and Recognition (camera.py)

https://www.youtube.com/watch?v=AOQj0PS4WyE

We installed a CMUcam5 Pixy camera (left Luigi’s hand). Pixy is a partnership between the Carnegie Mellon Robotics Institute and Charmed Labs. Pixy is a fully open source embedded camera that has a dual core ARM processor, USB/I2C/UART/SPI communication, and built-in computer vision algorithms. We programmed Luigi to only recognize “Mr Strong”. 

3. Luigi Dancing ! (danse.py)

https://www.youtube.com/watch?v=yxKm2C_Vi-8

The product owner also requested Luigi to Dance. We developed some random movements that we can adapt depending on the song. 

4. Luigi is on a course. (telecommand.py)

https://www.youtube.com/watch?v=cgIZxQiOUmY

5. Luigi detects obstacles (distance.py)

https://www.youtube.com/watch?v=C-lMbf8aKzE&t=6s

References:
http://www.ev3dev.org/
https://sites.google.com/site/ev3python/learn_ev3_python/remote-control
http://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/motors.html
http://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/rpyc.html

# EV3 Configuration

You cannot run heavy programs within lego's brick
The best is really to run the program remotly (local machine, cloud ...) and send instructions to the robot through a network (Wifi)
This is the approach I took

First you have to setup the development environnement
Follow the steps in http://www.ev3dev.org/docs/getting-started/
You will download the ev3-dev environnement and Etcher application to flash the SD card + configure wifi with a donger
Connect to Luigi through ssh : ssh robot@ev3dev.local and password is "maker"
To power off Luigi via command line: "sudo poweroff"
Install RPyC on EV3 and local computer
nstall RPyC to run the program locally and execute remotly. Follow: http://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/rpyc.html
run the rpyc_server.sh from EV3
Then, you can run the program locally
I use python 3

# Local computer

Install pip3
Install virtualenv
sudo pip3 install virtualenv
virtualenv ENV # Where ENV is a directory to place the new environnement (ENV/lib/, ENV/include/, And the packages will live under ENV/lib/pythonX.X/site-packages/, ENV/bin where all the executables are)
source bin/activate # This resides in ENV/bin/ (To undo just run deactivate command)
sudo apt-get install python3-pip

# Install ev3 environnement locally
sudo pip3 install python-ev3dev

# Install ChatterBot
pip3 uninstall chatterbot
pip3 install --upgrade setuptools
pip3 install git+git://github.com/gunthercox/ChatterBot.git@master

# Install MongoDB 
On MacOS (For others OS see: https://docs.mongodb.com/manual/installation/
brew install mongodb
brew install mongodb --with-openssl
mkdir -p data_chatbot/db # Set permissions

# Install espeak
On Mac:
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
brew install espeak
export PATH=$PATH:/usr/local/bin/

# run mongodb
mongod --dbpath <path to data directory>
mongod --dbpath <path to data directory>
