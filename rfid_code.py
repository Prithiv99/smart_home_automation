import mfrc522
import machine
import utime

sck = machine.Pin(14, machine.Pin.OUT)
mosi = machine.Pin(13, machine.Pin.OUT)
miso = machine.Pin(12, machine.Pin.IN)
rst = machine.Pin(4, machine.Pin.OUT)
cs = machine.Pin(5, machine.Pin.OUT)

from machine import SoftSPI
spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
spi.init()
rdr = mfrc522.MFRC522(spi=spi, gpioRst=4, gpioCs=5)

print("Place card")

while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            card_id = "UID: 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print(card_id)
    
    utime.sleep_ms(500)
