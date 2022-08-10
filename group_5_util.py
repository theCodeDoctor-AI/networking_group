# -*- coding: utf-8 -*-
"""
Created on August 9 01:30:11 2022
@author: COMP216 Assignment 3 - Group 5
group_5_util.py

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
# Create temperature data

class Util: 
    def __init__(self):
        self.DAILY_AMPLITUDE = 7
        self.HOURLY_AMPLITUDE = self.DAILY_AMPLITUDE / 12

        self.initial_temperature = 16
        self.temp_change = 7.50
        self.time_series = []

        self.average_temp = 20
        self.change = 5

    def get_data(self):
        self.base = datetime.datetime.today()
        self.hours_list = [self.base + datetime.timedelta(hours = x) for x in range(8760)]

        for h in self.hours_list:
            v_timestamp = None

            noise = random.gauss(0, 1)
            if h.hour >= 6 and h.hour < 18:
                self.change += self.HOURLY_AMPLITUDE
            else:
                self.change -= self.HOURLY_AMPLITUDE
            y = self.average_temp + self.DAILY_AMPLITUDE * math.sin((math.pi * self.change) / 30) + noise

            v_timestamp = time.asctime(h.timetuple())

            data_point = {
                "Time of Creation": v_timestamp,
                "Temperature": y
            }

            self.time_series.append(data_point)

        return self.time_series
