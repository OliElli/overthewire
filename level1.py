#!/usr/bin/env python

import struct
import telnetlib
import time

print ('Connecting...')
tn = telnetlib.Telnet('vortex.labs.overthewire.org', 5842)
output = tn.read_some()                         # Grab the data
         
total = 0
for i in [output[i:i+4] for i in range(0, len(output), 4)]:     # Split into bytes
    total += struct.unpack_from('<I',i)[0]                      # Add integer value to total
result = struct.pack('<I',(total & 0xffffffff))                 # Pack result into little endian bytes

tn.write(result)
time.sleep(1)
print (tn.read_some().decode('ascii'))
