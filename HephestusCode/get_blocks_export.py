import pixy
from ctypes import *
from pixy import *
from networktables import NetworkTables
import ntcore
from networktables.util import ntproperty
import logging

# This is adapted from the robotpy example code and the Pixycam code 
#for the Pixy2.  Their code uses the Python SWIG get blocks example building or moving the library is necessary for the imports.#

import logging

logging.basicConfig(level=logging.DEBUG)
NetworkTables.initialize(server='192.168.1.132')

print ("Pixy2 Python SWIG Example -- Get Blocks")

pixy.init ()
pixy.change_prog ("color_connected_components")

class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint),
    ("m_x", c_uint),
    ("m_y", c_uint),
    ("m_width", c_uint),
    ("m_height", c_uint),
    ("m_angle", c_uint),
    ("m_index", c_uint),
    ("m_age", c_uint) ]
class Client(object):
    '''Connect to the Network table and setup properties'''

    Object = ntproperty("/hephestus/object_data", 'N/A')
    target_type = ntproperty("/hephestus/target_type", 'N/A')
    target_size = ntproperty("/hephestus/target_size", 00.00)
    target_offset = ntproperty("/hephestus/target_offset", 00.00)


c = Client()
blocks = BlockArray(100)
frame = 0
pixy.set_lamp (1, 0)

while 1:
  count = pixy.ccc_get_blocks (100, blocks)

  if count > 0:
    print ('frame %3d:' % (frame))
    frame = frame + 1
    for index in range (0, count):
      print ('[BLOCK: SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].m_signature, blocks[index].m_x, blocks[index].m_y, blocks[index].m_width, blocks[index].m_height))
      c.Object = ("Get_Blocks", [blocks[index].m_signature, blocks[index].m_x, blocks[index].m_y, blocks[index].m_width, blocks[index].m_height])
      #sd.putString('Block', blocks[index].m_x, "Target Offset", ((blocks[index].m_x) - 157.5))
      targetOffset = ((blocks[index].m_x) - 157.5)
      if blocks[index].m_signature == 1:
        c.target_type = 'Cargo Found'
      c.target_size = ((blocks[index].m_width * blocks[index].m_height)/2)
      c.target_offset = targetOffset


      '''Put this in the drive code...
      targetOffset = sd.getString('target offset', 0)

      if targetOffset != 0:
        X = maxVelocity - targetOffset
      

        '''
