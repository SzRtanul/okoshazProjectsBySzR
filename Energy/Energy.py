#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image
import pybricks.nxtdevices
class Energy:
     
     def __init__(self):
          self.energymeter=0
          self.km = Motor(Port.A)
     
     def getUsedEnergy(self):
          pass
     
     def getInEnergy(self):
          pass
     
     def storedEnergy(self):
          pass
     def main(self):
          print("Ez fut.")
          #self.km.speed(1000000, 1000000)
          while(True):
               self.km.run(9999999)