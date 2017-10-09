#write to file (ovewrite or create new file)

file = open('./test.file', 'wb')
# 
# write 3 bytes to file
# 00100001 00100111 00111111
#    2   1    2   7    3   F
#
file.write(b'\x21\x27\x3f')
file.close()