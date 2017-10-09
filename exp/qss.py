# search and return location for 31201333121132032013003220000201303302

import binascii, re, math, numpy, json, datetime

start = datetime.datetime.now()

to_find = '312013331'

len_to_find = math.trunc(math.ceil(len(to_find)/2.0))
print len_to_find
bytes_to_read = 1024 * 16
if(len_to_find > bytes_to_read):
  bytes_to_read = len_to_find

loc = 0
pos = 0
prev_chunk = ''
pos_list = []

with open('./test.file', 'rb') as file:
    byte = file.read(bytes_to_read)
    while byte:
      chunk = prev_chunk + byte
      
      check_chunk = re.split(to_find, binascii.hexlify(chunk))
      if(len(check_chunk) > 1):
        pos = (loc - 1) * bytes_to_read + len(check_chunk[0])/2
        pos_list.append(pos)

      # read next set of bytes
      loc += 1
      prev_chunk = byte
      byte = file.read(bytes_to_read)
      
    file.close()

pos_list = numpy.unique(pos_list).tolist()

out = {
        'took': str(datetime.datetime.now() - start),
        'count': len(pos_list),
        'seq': to_find,
        'length': len_to_find,
        'locations': pos_list
      } #19 626494

print json.dumps(out)

# check
#
#with open('./test.file', 'rb') as file:
#  file.seek(out['locations'][0])
#  byte = file.read(out['length'])
#  
#  print binascii.hexlify(byte)
#  
#  file.close()
