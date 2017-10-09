#write 1Mb of random data to file
import random

file_loc = './'
file_name = 'test'
file_ext = '.data'

file_count = 10
max_val_per_file = 1024 * 1024

max_val = max_val_per_file * file_count

for i in range(0,max_val) :
  file_version = '_' + str(i/(max_val/file_count))
  target_file = file_loc + file_name + file_version + file_ext
  
  random.seed(i)
  byte = random.getrandbits(2)
  
  random.seed(max_val%(i+1))
  sec_byte = random.getrandbits(2)
  
  hex_eq = hex(byte)[2:-1]
  hex_sec = hex(sec_byte)[2:-1]
  
  if (len(hex_eq) < 2): hex_eq = hex_eq + '' + hex_sec
  file = open(target_file, 'ab')
  file.write(eval('b\'\\x' + hex_eq + '\''))
  file.close()
  
print 'job done'