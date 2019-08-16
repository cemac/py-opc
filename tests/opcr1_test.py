import unittest
from time import sleep
from opc import OPCR1
from opc.exceptions import SpiConnectionError, FirmwareVersionError
from usbiss.spi import SPI

interval = 1

spi = SPI("/dev/ttyACM0",mode=1, max_speed_hz=500000)

alpha = OPCR1(spi)



alpha.on()
sleep(10)

print("Read info string")
print(alpha.read_info_string())

print("Read serial number")
print(alpha.sn())

print("Read firmware")
print(alpha.read_firmware())


print("Read config")
print(alpha.read_config())


print("Read Histogram")
print(alpha.histogram())

sleep(10)
print("Read PM")
print(alpha.pm())


alpha.off()
