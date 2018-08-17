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
time.sleep(4)
output = tn.read_some()                         # Grab the data
pp.pprint(output)
output_bytes = output.hex()                     # Convert to hex
pp.pprint(output_bytes)
output_list = [output_bytes[i:i+8] for i in range(0,len(output_bytes), 8)]      
                                                # Convert hex string into a list split on bytes
print('output_list:')
pp.pprint(output_list)
for i in output_list[:4]:                       # Iterate first 4 bytes
    print(int(i, 16))                           # print the decimal value of the byte
    # total = total + Decimal(int(i, 16))
    total += Decimal(int(i, 16))

print('Total: ' + str(total))
output = str(total) + '\n'

tn.write(str(total).encode('ascii') + b'\n')
time.sleep(1)
print (tn.read_some().decode('ascii'))