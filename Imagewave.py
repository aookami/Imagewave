
#The Python Imaging Library (PIL) is
#
#   Copyright © 1997-2011 by Secret Labs AB
#   Copyright © 1995-2011 by Fredrik Lundh
#
#Pillow is the friendly PIL fork. It is
#
#   Copyright © 2010-2017 by Alex Clark and contributors
#
#
#




from __future__ import print_function
import os, sys
from PIL import Image
from numpy import random
from time import gmtime, strftime
fcalled = "f"

def contrast(imf, offset):
  global fcalled
  "this makes the contrast hard"
  fcalled =  fcalled+"contrast"+str(offset)
  imc = imf
  size = imo.size
  width, height = size
  for x in range(1, width-1):
    for y in range(1, height-1):
      r, g, b = imc.getpixel((x, y))
      if r > 125:
	r = r*(1+offset)
      else:
	r = r*(1-offset)
      if g > 125:
	g = g*(1+offset)
      else:
	g = g*(1-offset)
      if b > 125:
	b = b*(1+offset)
      else:
	b = b*(1-offset)
      imf.putpixel((x,y), (int(r),int(g),int(b)))
  print("donecontrast")
      
def blur((imf)):
  global fcalled
  fcalled = fcalled+"blur"
  imb = imf
  size = imo.size
  width, height = size
  for x in range(1, width-1):
    for y in range(1, height-1):
      r1, g1, b1 = imb.getpixel((x-1, y-1))
      r2, g2, b2 = imb.getpixel((x-1, y+1))
      r3, g3, b3 = imb.getpixel((x-1, y))
      r4, g4, b4 = imb.getpixel((x+1, y-1))
      r5, g5, b5 = imb.getpixel((x+1, y+1))
      r6, g6, b6 = imb.getpixel((x+1, y))
      r7, g7, b7 = imb.getpixel((x, y+1))
      r8, g8, b8 = imb.getpixel((x, y-1))
      rt = (r1+r2+r3+r4+r5+r6+r7+r8)/8
      gt = (g1+g2+g3+g4+g5+g6+g7+g8)/8
      bt = (b1+b2+b3+b4+b5+b6+b7+b8)/8
      imf.putpixel((x,y), (int(rt),int(gt),int(bt)))
  print("doneblur")
      
def addRGB(imf, value):
  global fcalled
  fcalled = fcalled+"addRGB"+str(value)
  size = imf.size
  width, height = size
  for x in range(1, width-1):
    for y in range(1, height-1):
      r, g, b = imf.getpixel((x, y))
      r = r+value
      g = g+value
      b = b+value
      imf.putpixel((x,y), (int(r),int(g),int(b)))
  print("doneaddRGB")
def biggerelsemid(imf):
  global fcalled
  
  size = imf.size
  width, height = size
  
  for x in range(1, width-1):
    for y in range(1, height-1):
      r, g, b = imf.getpixel((x, y))
      
      if r >= g and r >= b:
	g = 125
	b = 125
      elif g >=r and g>=b:
	b = 125
	r = 125
      elif b >=r and b>=g:
	r = 125
	g = 125
      imf.putpixel((x,y), (int(r),int(g),int(b)))  
  fcalled = fcalled+"biggerelsemid"
  print("donebiggerelsemid")
  
  
  
  
  
  
  
    
imo = Image.open("Amelie-0567.jpg")
im = imo

biggerelsemid(im)
blur(im)
im.save(strftime("%Y%m%d%H%M%S", gmtime())+fcalled+"amelie.jpeg")