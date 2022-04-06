from serial import Serial
from pynmeagps import NMEAReader

stream = Serial('COM6', 9600, timeout=3)

nmr = NMEAReader(stream)
(raw_data, parsed_data) = nmr.read()
print(parsed_data)

stream.close()