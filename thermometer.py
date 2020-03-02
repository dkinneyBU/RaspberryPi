#!/usr/bin/python
from sense_hat import SenseHat
import time
import sys

sense = SenseHat()
sense.set_rotation(180)
sense.clear()
red = (255, 0, 0)

try:
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = abs(x)
        y = abs(y)
        z = abs(z)

        temp = sense.get_temperature()
        temp = 1.8 * round(temp, 1)  + 12
        temp = round(temp, 1)
        print(" Temperature F",temp)

        humidity = sense.get_humidity()
        humidity = round(humidity, 1)
        print(" Humidity :",humidity)

        pressure = sense.get_pressure()
        pressure = round(pressure, 1)
        print(" Pressure:",pressure)

        if x > 1 or y > 1 or z > 1:
            sense.show_message("PUT ME DOWN!", red)
        else:
            sense.show_message("T..." + str(temp) + "F  H... "
            + str(humidity) + " Pr... "
            + str(pressure), scroll_speed=(0.15),
            text_colour=[75,0,130],
            back_colour= [0,0,0])
        time.sleep(60)
        sense.show_message("Welcome to the machine, David...",
                           text_colour=[0,100,0])
        time.sleep(15)
except KeyboardInterrupt:
    pass

sense.clear()
