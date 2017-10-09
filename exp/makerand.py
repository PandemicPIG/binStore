#write 1Mb of random data to file
import random

file_loc = './test.file'

max_val = 1024 * 1024

for i in range(0,max_val) :
  
  random.seed(i)
  byte = random.getrandbits(2)
  
  random.seed(max_val%(i+1))
  sec_byte = random.getrandbits(2)
  
  hex_eq = hex(byte)[2:-1]
  hex_sec = hex(sec_byte)[2:-1]
  
  if (len(hex_eq) < 2): hex_eq = hex_eq + '' + hex_sec
  file = open(file_loc, 'ab')
  file.write(eval('b\'\\x' + hex_eq + '\''))
  file.close()