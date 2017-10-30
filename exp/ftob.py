from lib import convert

input_file = './sequence.fasta'

with open(input_file, 'r') as file:
  line = file.readline()
  location = 1
  while (location < 100):
    
    if (line[0] == '>'):
      print('name: ' + line)
    elif (line == '\n'):
      pass
    else:
      print([location, convert.dataTypeConversion(line[:-1])])
    
    line = file.readline()
    location += 1