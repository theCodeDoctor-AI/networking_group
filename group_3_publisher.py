# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 01:30:11 2022
@author: COMP216 Assignment 5 - Group 3
group_3_publisher.py
"""

import json
import paho.mqtt.client as mqtt
import random
import time
import datetime
import math

#util.py

# Create temperature data
def create_data():

    DAILY_AMPLITUDE = 7

    HOURLY_AMPLITUDE = DAILY_AMPLITUDE / 12

    timestamp = None

    base = datetime.datetime.today()
    hours_list = [base + datetime.timedelta(hours = x) for x in range(8760)]

    initial_temperature = 16
    temp_change = 7.50
    time_series = []

    average_temp = 20
    change = 5

    for h in hours_list:
        noise = random.gauss(0, 1)
        if h.hour >= 6 and h.hour < 18:
            change += HOURLY_AMPLITUDE
        else:
            change -= HOURLY_AMPLITUDE
        y = average_temp + DAILY_AMPLITUDE * math.sin((math.pi * change) / 30) + noise

        timestamp = time.asctime(h.timetuple())

        data_point = {
            "Time of Creation": timestamp,
            "Temperature": y
        }

        time_series.append(data_point)

    return time_series

broker = "mqtt.eclipseprojects.io"

client = mqtt.Client()

print("Connected to the Broker", broker)

client.connect(broker, 1883)

client.loop_start()

while True:
    time_series = create_data()
    for series in time_series:
        dict_str = json.dumps(series)
        client.publish("TorontoTemp", payload=dict_str)
        print('Publishing data: ' + str(dict_str) + ' to Networking COMP216 group ? TorontoTemp')
        time.sleep(1)

client.loop_stop()
client.disconnect()