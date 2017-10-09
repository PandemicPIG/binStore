from os import path
from os import stat
from binascii import hexlify
from re import split
from math import trunc, ceil
from numpy import unique
from json import dumps
from datetime import datetime

start = datetime.now()

file_count = 0
file_data = []

to_find = '31201333120'
len_to_find = trunc(ceil(len(to_find)/2.0))

bytes_to_read = 1024 * 16 #read chunks of 16kb
if(len_to_find > bytes_to_read):
  bytes_to_read = len_to_find
  
prev_chunk = '';
pos_list = []

data_location = './'
data_name = 'test_'
data_extension = '.data'

while path.isfile(data_location + data_name + str(file_count) + data_extension):
  file_data.append({
    'index': file_count,
    'size': stat(data_location + data_name + str(file_count) + data_extension).st_size
  })
  file_count += 1
  
for fileIndex in file_data:
  loc = 0
  pos = 0
  with open(data_location + data_name + str(fileIndex["index"]) + data_extension, 'rb') as file:
    byte = file.read(bytes_to_read)
    while byte:
        chunk = prev_chunk + byte
        
        check_chunk = split(to_find, hexlify(chunk))
        
        if(len(check_chunk) > 1):
          pos = (loc -1) * bytes_to_read + len(check_chunk[0])/2
          pos_list.append({
            'loc': pos, 
            'file': data_location + data_name + str(fileIndex["index"])
          })
          
        # read next set of bytes
        prev_chunk = byte
        loc += 1
        byte = file.read(bytes_to_read)
      
    file.close()
    
pos_list = unique(pos_list).tolist()

out = {
        'took': str(datetime.now() - start),
        'count': len(pos_list),
        'seq': to_find,
        'length': len_to_find,
        'locations': pos_list
      }

print dumps(out)