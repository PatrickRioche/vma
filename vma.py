#!/usr/bin/python
#
# USAGE :
#  vma.py
#
__version__ = 'v1.0'

debug=0

import os,sys
import RPi.GPIO as GPIO
import time

#
#   Initialisation de variable
#
sens=">"
cpt = 0

motorpin1 = 24	# GPIOO8
motorpin2 = 21	# GPIOO9
motorpin3 = 19	# GPIO10
motorpin4 = 23	# GPIO11

lookupav = ['1000','1100','0100','0110','0010','0011','0001','1001']
lookupar = ['1001','0001','0011','0010','0110','0100','1100','1000']

motorspeed = 0.005

GPIO.setmode(GPIO.BOARD)

GPIO.setup(motorpin1, GPIO.OUT)
GPIO.setup(motorpin2, GPIO.OUT)
GPIO.setup(motorpin3, GPIO.OUT)
GPIO.setup(motorpin4, GPIO.OUT)

def clock():
  for av in lookupav:
     setoutput(av)
     time.sleep(motorspeed)
  if debug : print("clock")

def anticlock():
  for ar in lookupar:
     setoutput(ar)
     time.sleep(motorspeed)
  if debug : print("anticlock")

def setoutput(phase):
  #print( phase[0], phase[1], phase[2], phase[3] )	# Print obligatoire
  GPIO.output(motorpin1,int(phase[0]))
  GPIO.output(motorpin2,int(phase[1]))
  GPIO.output(motorpin3,int(phase[2]))
  GPIO.output(motorpin4,int(phase[3]))

#
#   Documentation
#
print("VMA: "+ __version__)
print("> : incrementation")
print("< : decrementation")
print("z : goto 1")
print("m : goto 5000")
print("q : quitter")

#
#   Boucle principale
#
while True:
    print("VMA:" + sens + ":" + str(cpt))
    clavier = raw_input()
    if clavier == "q":
        break
    if clavier == ">":
        sens=">"
    if clavier == "<":
        sens="<"
    if clavier == "z":
        cpt=1
    if clavier == "m":
        cpt=5000
    if sens == ">":
        if cpt < 4999:
            cpt = cpt + 1
            clock()
        else:
            cpt = 5000
    if sens == "<":
        if cpt > 1:
            cpt = cpt - 1
            anticlock()
        else:
            cpt = 0

GPIO.cleanup()
print("Fin de programme VMA: " + __version__ )