import time

from dht import DHT22
from machine import I2C, Pin

import ssd1306

# Make sure Debug LED is off
led_pin = Pin(2, Pin.OUT)
led_pin.value(0)

dht22 = DHT22(Pin(18))
i2c = I2C(sda=Pin(21), scl=Pin(22))

display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.poweron()

while True:
    dht22.measure()
    temperature = dht22.temperature()
    humidity = dht22.humidity()
    display.fill(0)
    display.text(f"Temp [C]: {temperature}", 0, 16)
    display.text(f"RHum [%]: {humidity}", 0, 40)
    display.show()
    time.sleep(2)
