import serial
import pynmea2
def parseGPS(std):
    if std.find(b'GGA') > 0:
        msg = pynmea2.parse(std.decode('utf-8'))
        print("Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" %(msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,msg.altitude_units))
serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
while True:
    std = serialPort.readline()
    parseGPS(std)
