#convert atcg to numeric and reverse
from re import search

#data_in = '1020310230102002130230021020300301203010231'
#data_in = 'acgatcgatcgatcgatctatcgatcgatttcgatcagtcgta'
data_in = 'CAGATCAGTACAGAAGCTAGTAAGCAGATAATACGATACAGTC'

def getLib():
  return {
    "0": ["A", "a"],
    "1": ["C", "c"],
    "2": ["G", "g"],
    "3": ["T", "t"]
  }

def getReverseLib():
  lib = getLib()
  revLib = {}
  
  for chk in lib:
    for let in lib[chk]:
      revLib[let] = [chk]
      
  return revLib

def dataTypeConversion(data_in):
  data_out = ''
  
  #numeric to readable
  if search('[0-9]', data_in):
    lib = getLib()
  #readable to numeric
  else:
    lib = getReverseLib()
    
  for char in data_in:
    data_out += lib[char][0]
    
  return data_out

data_out = dataTypeConversion(data_in)
print data_out
