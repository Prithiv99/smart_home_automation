import machine
import dht
import time
import network
import BlynkLib

# Wi-Fi Configuration
WIFI_SSID = "" #your ssid
WIFI_PASSWORD = "" #your password

# Blynk Configuration
BLYNK_AUTH_TOKEN = "" #your blynk token

# Pin Configuration
dht_pin = machine.Pin(5, machine.Pin.IN)   # DHT22 sensor pin (GPIO5)
pir_pin = machine.Pin(4, machine.Pin.IN)    # PIR sensor pin (GPIO4)
trig_pin = machine.Pin(12, machine.Pin.OUT) # Ultrasonic sensor trigger pin (GPIO12)
echo_pin = machine.Pin(14, machine.Pin.IN)  # Ultrasonic sensor echo pin (GPIO14)
gas_pin = machine.ADC(0)                     # Gas sensor pin (A0)

# Initialize DHT22 sensor
dht_sensor = dht.DHT22(dht_pin)

# Function to read temperature and humidity from DHT22 sensor
def read_dht_sensor():
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    return temperature, humidity

# Function to read PIR sensor
def read_pir_sensor():
    return pir_pin.value()

# Function to read ultrasonic sensor
def read_ultrasonic_sensor():
    trig_pin.on()
    time.sleep_us(10)
    trig_pin.off()
    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration / 58
    return distance

# Function to read gas sensor
def read_gas_sensor():
    gas_value = gas_pin.read()
    return gas_value

# Connect to Wi-Fi
def connect_wifi():
    station = network.WLAN(network.STA_IF)
    if station.isconnected():
        print("Already connected to Wi-Fi")
        return
    station.active(True)
    station.connect(WIFI_SSID, WIFI_PASSWORD)
    while not station.isconnected():
        pass
    print("Wi-Fi connected:", station.ifconfig())

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# Main loop
while True:
    blynk.run()
    
    temperature, humidity = read_dht_sensor()
    pir_status = read_pir_sensor()
    distance = read_ultrasonic_sensor()
    gas_value = read_gas_sensor()
    
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    
    if pir_pin.value() == 1:
        pir_status="Motion detected"
        print("Motion detected!")
    else:
        pir_status="No motion detected"
        print("No motion detected")
    print("Distance:", distance, "cm")
    
    print("Gas value:", gas_value)
    
    blynk.virtual_write(0, temperature)
    blynk.virtual_write(1, humidity)
    blynk.virtual_write(2, pir_status)
    blynk.virtual_write(3, distance)
    blynk.virtual_write(4, gas_value)
    
    time.sleep(2)  # Delay between sensor readings