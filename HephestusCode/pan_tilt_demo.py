  GNU nano 2.7.4                                    File: pan_tilt_demo.py                                    Modified

      print 'Frame %3d:' % (Frame)

      # Display all the blocks in the frame #
      for Index in range (0, Count):
        Display_Block (Index, Blocks[Index])

      # Find an acceptable block to lock on to #
      if Blocks[0].m_age > MINIMUM_BLOCK_AGE_TO_LOCK:
        Locked_Block_Index = Blocks[0].m_index;
        Locked_On_Block    = True
  else:
    Reset ()

