# read at location

import binascii

bytes_to_read = 19
location = 626494

with open('./test.file', 'rb') as file:
  file.seek(location)
  byte = file.read(bytes_to_read)
  print binascii.hexlify(byte)
  
  file.close()