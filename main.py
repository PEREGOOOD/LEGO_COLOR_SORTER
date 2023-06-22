#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#DECLARE THE COLOR AND TOUCH SENSORS
color_sen = ColorSensor(port = Port.S1)
touch_sen = TouchSensor(port = Port.S2)

#DECLARE BOTH MOTORS FOR THE PUSH BLOCK AND FOR THE CONVEYOR BELT MOVEMENT
rot = Motor(port = Port.A, positive_direction=Direction.CLOCKWISE,gears=None)
push =  Motor(port = Port.B,positive_direction=Direction.CLOCKWISE,gears=None)
colors = []

# Write your program here.
ev3.speaker.beep()

#STABLISH THE POSITION 0 FOR THE CONVEYOR (MOTOR IN PORT A)
def initialize():
    while not touch_sen.pressed(): 
        rot.run(-100)       #MOVE THE MOTOR A UNTIL THE BLOCK COLLECTER TOUCHES THE SENSOR
    rot.run(0)                      
    rot.reset_angle(0)

#READING THE COLORS PILLED IN THE BLOCK COLLECTOR
def read_colors():
    while len(colors)< 8:   
        if Button.CENTER in ev3.buttons.pressed():
            break
        time.sleep(0.5)
        if color_sen.color() != None:
            if  color_sen.color() != Color.BLACK:
                if color_sen.color() != Color.WHITE:            
                    if color_sen.color() != Color.BROWN:
                        colors.append(color_sen.color())    #READ THE COLORS EXCEPT BLACK, WHITE AND BROWN (TO AVOIT LECTURE ERRORS)
                        ev3.speaker.beep()                  #DO TILL THE COLORS IN THE LIST ARE < 8
        print(colors)
        
#LEAVE THE BLOCKS INTO THE RESPECTIVE CONTAINER
def distribute():
    for col in colors:      #STABLISH A SPECIFIC POSITION FOR THE MOTOR IN EVERY COLOR AND ACTIVATING THE PUSH MOTOR TO THROW THE BLOCK
        if col == Color.BLUE:
            ev3.speaker.say("blue")
            rot.run_target(250,10,then=Stop.HOLD, wait=True)
        elif col == Color.GREEN:
            ev3.speaker.say("green")
            rot.run_target(250,132,then=Stop.HOLD, wait=True)
        elif col ==  Color.YELLOW:
            ev3.speaker.say("yellow")
            rot.run_target(250,360,then=Stop.HOLD, wait=True)
        elif col ==  Color.RED:
            ev3.speaker.say("red")
            rot.run_target(250,530,then=Stop.HOLD, wait=True)
        push.run_target(1000,-90,then=Stop.HOLD, wait=True)
        push.run_target(1000,0,then=Stop.HOLD,wait=True)
    rot.run_target(250,0,then=Stop.HOLD, wait=True)

initialize()
read_colors()
distribute()








