#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image
from pybricks.nxtdevices import EnergyMeter
import threading
class Energy:
     
     def __init__(self):
          self.intervall = 0
          self.filename = "default.txt"
          self.mentesmegy = False
          #self.t1 = threading.Thread(target=self.mentesiCiklus)
          self.energymeter = EnergyMeter(Port.S1)
          self.fajl = DataLog('Bemenet(mV)', 'Bemenet(mA)', 'Bemenet(mW)', 'Kimenet(mV)', 'Kimenet(mA)', 'Kimenet(mW)', 'Tárolt energia(J)', name='energylog', timestamp=True, extension='csv', append=True)
          
     
     def getUsedEnergy(self):
          return self.energymeter.output()
     
     def getInEnergy(self):
          return self.energymeter.input()
     
     def getStoredEnergy(self):
          return self.energymeter.storage()
     
     def setMentIntervallum(self, intervall: int):
          self.intervall = intervall
          
     def setFilename(self, filename: str):
          self.filename = filename
          
     def idoszakonkentMentInditasa(self, ment: bool):
          self.mentesmegy=ment
          #if(ment):
               #self.t1.start()
               
     def mentesiCiklus(self):
          while(self.mentesmegy):
               print("Ezt kiirja")
               
     def program(self):
          print("Bemenet, Kimenet, Tárolt energia")
          while(True):
               inp = self.getInEnergy()
               outp = self.getUsedEnergy()
               self.fajl.log(inp[0], inp[1], inp[2], outp[0], outp[1], outp[2], self.getStoredEnergy()) 
               print(str(self.getInEnergy()) + " " + str(self.getUsedEnergy()) + " " + str(self.getStoredEnergy()))
               wait(1000)
          