import GNSS.get_NMEA_msg as gps_get
from serial import Serial


GNSSPort = Serial('COM6', 9600, timeout=3)

GNSS_msg = gps_get.NMEA_message(GNSSPort)
print (GNSS_msg["raw_data"])
print (GNSS_msg["parsed_data"])

GNSSPort.close()