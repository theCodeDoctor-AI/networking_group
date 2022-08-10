# -*- coding: utf-8 -*-
"""
    Utility script for MQTT application
    Houses Util functions for publisher
        
    College: Centennial College
    Program: Software Engineering Technology - Artificial Intelligence
    Term: Summer 2022
    Course: COMP 216 - Networking for Software Developers

    Created on Fri 5 Aug 2022
    @author: COMP216 Assignment 3 - Group 5
    group_5_util.py

    Members:
    Ankit Mehra    - 301154845
    Bruno Morgado  - 301154898
    Mark Randall   - 301178066
    Ronald Saenz   - 301218602

    Publisher – Value generation
        This must be implemented in a class in a separate file. (Just import the filename without the py extension in the file where you want to use the logic).
        The design should preferably be such that it is easy to use (multiple variation started by just specifying different arguments when starting).

    Publisher – Value generation – Pattern 
        The value generation should show a basic pattern, such as a sine wave, with momentary fluctuations.
"""

import random
import time
import datetime
import math

# util.py
# Create temperature and humidity data

class Util: 
    def __init__(self) -> None:
        self.DAILY_AMPLITUDE = 7
        self.HOURLY_AMPLITUDE = self.DAILY_AMPLITUDE / 12

        self.initial_temperature = 16
        self.temp_change = 7.50
        self.time_series = []

        self.average_temp = 20
        self.change = 5

        self.start_id = 11
        self.base = 57

    def generateHumidityData(self) -> dict:
        """Returns a data dictionary containing a timestamp as well as a relative humidity value"""
        self.start_id += 1
        noise = random.randint(-42, 42)  # To keep humidty in the range of 14 to 100%

        # base = random.randint(20, 90)           # generate random humiduty value between 10-90
        humidity = math.sin(self.base) + self.base + noise

        humidity_dict = {
            'id': self.start_id,
            'timestamp': time.asctime(),
            'humidity': humidity
        }

        return humidity_dict

    def generateTemperatureData(self) -> list:
        """Returns a data array containing a timestamp as well as a relative temperature value"""

        self.start_id += 1
        self.base = datetime.datetime.today()
        self.hours_list = [self.base + datetime.timedelta(hours = x) for x in range(8760)]

        for h in self.hours_list:

            noise = random.gauss(0, 1)
            if h.hour >= 6 and h.hour < 18:
                self.change += self.HOURLY_AMPLITUDE
            else:
                self.change -= self.HOURLY_AMPLITUDE
            temperature = self.average_temp + self.DAILY_AMPLITUDE * math.sin((math.pi * self.change) / 30) + noise

            v_timestamp = time.asctime(h.timetuple())

            data_point = {
                'id': self.start_id,
                'timestamp': v_timestamp,
                "temperature": temperature
            }

            self.time_series.append(data_point)

        return self.time_series
