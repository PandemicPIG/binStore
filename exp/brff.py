# read from file one chunk at the time

import binascii

bytes_to_read = 1

with open('./test.file', 'rb') as file:
    byte = file.read(bytes_to_read)
    while byte:
        
        # do stuff with byte
        print binascii.hexlify(byte)
        
#        if (binascii.hexlify(byte) == 'ac'):
#          file.close()
#          break
        
        # read next set of bytes
        byte = file.read(bytes_to_read)
      
    file.close()