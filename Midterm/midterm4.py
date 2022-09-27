from machine import Pin
import network
import uasyncio as asyncio
from umqtt.robust import MQTTClient
import time
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

def sub_callback_blink(topic, payload):
    # use decode instead of direct byte-array comparison
    if topic.decode() == "b6310545329/midterm/blink":
        try:
            print(payload)
            if int(payload)<11 and int(payload)>0:
                for i in range(int(payload)):
                    led_wifi.value(1)
                    sleep(0.75)
                    led_wifi.value(0)
                    sleep(0.25)
                led_wifi.value(1)
            else:
                print("Error input payload more than 10 or less than 1")
            print(payload)
        except ValueError:
            print("Invalid input")

count = 0

async def trigger():
    print(time.ticks_ms())
    while True:
       time_use = time.ticks_ms()
       await asyncio.sleep_ms(2500)
       deadline = time.ticks_ms()
       if time_use and time_use != deadline:
           await trigger_publish()
            
async def trigger_publish():
    global count
    count += 2.5
    mqtt.publish("b6310545329/midterm/uptime", str(count))
            
async def check_mqtt():
    while True:
        mqtt.check_msg()
        await asyncio.sleep_ms(50)
        
mqtt.set_callback(sub_callback_blink)
mqtt.subscribe("b6310545329/midterm/blink")
asyncio.create_task(check_mqtt())
asyncio.create_task(trigger())
asyncio.run_until_complete()

