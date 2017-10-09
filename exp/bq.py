# search and return location for 31201333121132032013003220000201303302

import binascii, re

to_find = '31201333121132032013003220000201303302'

bytes_to_read = len(to_find)/2
loc = 0
pos = 0
prev_chunk = '';

with open('./test.file', 'rb') as file:
    byte = file.read(bytes_to_read)
    while byte:

        if(len(prev_chunk) > 0):
          chunk = prev_chunk + byte
        else:
          chunk = byte
          
        check_chunk = re.split(to_find, binascii.hexlify(chunk))
        if(len(check_chunk) > 1):
          pos = (loc -1) * bytes_to_read + len(check_chunk[0])/2
          print [bytes_to_read, pos] #19 626494
          break
#        if (binascii.hexlify(byte) == 'ac'):
#          file.close()
#          break
        
        # read next set of bytes
        prev_chunk = byte
        loc += 1
        byte = file.read(bytes_to_read)
      
    file.close()