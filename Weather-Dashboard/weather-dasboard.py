from machine import Pin, ADC, I2C
import network
import kidbright as kb
from umqtt.robust import MQTTClient
import time
import json
from time import sleep
from config import (
    WIFI_SSID, WIFI_PASS,
    MQTT_BROKER, MQTT_USER, MQTT_PASS
)

led_wifi = Pin(2, Pin.OUT)
led_wifi.value(1)  # turn the red led off
led_iot = Pin(12, Pin.OUT)
led_iot.value(1)   # turn the green led off

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(WIFI_SSID, WIFI_PASS)

while not wlan.isconnected():
    time.sleep(0.5)
led_wifi.value(0)  # turn the red led on

mqtt = MQTTClient(client_id="",
                  server=MQTT_BROKER,
                  user=MQTT_USER,
                  password=MQTT_PASS)
mqtt.connect()
led_iot.value(0)   # turn the green led on

kb.init()
# ldr = ADC(Pin(36))
# i2c = I2C(1, sda=Pin(4), scl=Pin(5))

while True:
    #i2c.scan()
    #i2c.writeto(77, bytearray(0))
    #data = i2c.readfrom(77, 2)

    # x = data[0]
    # y = data[1]
    # w = x*256 + y
    #temp_cel = ((data[0]*256)+data[1])/128
    sent_data = {
        'light': kb.light(),
        'temperature': kb.temperature()
        }
    mqtt.publish("b6310545329/sensors", json.dumps(sent_data))
    time.sleep(10)
            


            




