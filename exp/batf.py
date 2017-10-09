# append at the end of file

with open('./test.file', 'ab') as file:
  # 
  # append 3 extra bytes to file
  #
  file.write(b'\xac\x00\xff')
  file.close()