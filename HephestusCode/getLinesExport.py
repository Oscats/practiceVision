from __future__ import print_function
import pixy
from ctypes import *
from pixy import *
import sys
from networktables import NetworkTables
from networktables.util import ntproperty
import logging

logging.basicConfig(level=logging.DEBUG)
NetworkTables.initialize(server='192.168.1.132')

# pixy2 Python SWIG get line features example #

get_all_features = True

print("Pixy2 Python SWIG Example -- Get Line Features")

pixy.init ()
pixy.change_prog ("line")

class Vector (Structure):
  _fields_ = [
    ("m_x0", c_uint),
    ("m_y0", c_uint),
    ("m_x1", c_uint),
    ("m_y1", c_uint),
    ("m_index", c_uint),
    ("m_flags", c_uint) ]

class IntersectionLine (Structure):
  _fields_ = [
    ("m_index", c_uint),
    ("m_reserved", c_uint),
    ("m_angle", c_uint) ]

class Client(object):
    '''Connect to the Network table and setup properties'''

    Inter = ntproperty("/hephestus/Intersection", 'N/A')


    Vect = ntproperty("/hephestus/Vector", 'N/A')
    luminary = ntproperty("/hephestus/lights", False)

class Lights:
  pixy.change_prog ("video")

  turnOn = pixy.set_lamp (1, 0)
  turnOff = pixy.set_lamp (0, 0)


c = Client()

vectors = VectorArray(100)
intersections = IntersectionArray(100)
barcodes = BarcodeArray(100)
frame = 0

while 1:
  if c.luminary == True:
    Lights.turnOn
  else:
    Lights.turnOff
  if get_all_features:
    line_get_all_features ()
  else:
    line_get_main_features ()
  i_count = line_get_intersections (100, intersections)
  v_count = line_get_vectors (100, vectors)
  b_count = line_get_barcodes(100, barcodes)
  if i_count > 0 or v_count > 0 or b_count > 0:
    print('frame %3d:' % (frame))
    frame = frame + 1
    for index in range (0, i_count):
      vect0 = ('[INTERSECTION: X=%d Y=%d BRANCHES=%d]' % (intersections[index].m_x, intersections[index].m_y, intersections[index].m_n))
      print(vect0)
      c.Inter = vect0
      # for lineIndex in range (0, intersections[index].m_n):
        # print('  [LINE: INDEX=%d ANGLE=%d]' % (intersections[index].getLineIndex(lineIndex), intersections[index].getLineAngle(lineIndex)))
    for index in range (0, v_count):
      vect1 = ('[VECTOR: INDEX=%d X0=%d Y0=%d X1=%d Y1=%d]' % (vectors[index].m_index, vectors[index].m_x0, vectors[index].m_y0, vectors[index].m_x1, vectors[index].m_y1))
      print(vect1)
      c.Vect = vect1
    # for index in range (0, b_count):
      # print('[BARCODE: X=%d Y=%d CODE=%d]' % (barcodes[index].m_x, barcodes[index].m_y, barcodes[index].m_code))