#!/usr/bin/env python

from decimal import Decimal
import io
import pprint
import telnetlib
import time

pp = pprint.PrettyPrinter(indent=2)
total = 0

# Get input from telnet:
print ('Connecting...')
tn = telnetlib.Telnet('vortex.labs.overthewire.org', 5842)

output = tn.read_some()                          # Grab the data    
output_bytes = output.hex()                     # Convert to hex  
output_list = [output_bytes[i:i+8] for i in range(0,len(output_bytes), 8)]      
                                                # Convert hex string into a list split on bytes
for i in output_list[:4]:                       # Iterate first 4 bytes
    # print(int(i, 16))                           # print the decimal value of the byte
    # print(Decimal(int(i, 16)))
    total = total + Decimal(int(i, 16))

print('Total: ' + str(total))
output = str(total) + '\n'

tn.write(str(total).encode('ascii') + b'\n')
time.sleep(1)
print (tn.read_some().decode('ascii'))