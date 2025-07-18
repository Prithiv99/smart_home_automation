# Smart Home Automation 

This is a MicroPython-based Smart Home Automation system using ESP8266/ESP32, integrated with Blynk IoT platform for real-time monitoring and control.

##  Features

- Temperature & Humidity Monitoring (DHT22)
- Motion Detection (PIR Sensor)
- Distance Measurement (Ultrasonic Sensor - HC-SR04)
- Gas Leakage Detection (MQ sensor)
- RFID for gate entry
- Remote Monitoring using Blynk IoT Dashboard


## Hardware Used

- ESP8266 / ESP32
- DHT22 Sensor
- PIR Sensor
- HC-SR04 Ultrasonic Sensor
- Gas Sensor (MQ series)
- Buzzer, Servo Motor, and optional RFID

## Blynk Integration

Update the following in `smart_home_automation.py`:
```python
WIFI_SSID = "your_wifi_ssid"
WIFI_PASSWORD = "your_wifi_password"
BLYNK_AUTH_TOKEN = "your_blynk_token"

