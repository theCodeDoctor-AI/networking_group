"""
    Utility script for MQTT application
    Houses Util functions for publisher
    
    Created on Fri 5 Aug 2022
    @author: COMP216 Assignment 3 - Group 5
    util.py

    Ankit Mehra    - 301154845
    Bruno Morgado  - 301154898
    Mark Randall   - 301178066
"""

import random
import math
import time
import datetime

class Util:

    def __init__(self) -> None:
        self.start_id = 11
        self.base = 57

    def generate_humid_data(self) -> dict:
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
    
    def generate_temp_data(self):

        DAILY_AMPLITUDE = 7

        HOURLY_AMPLITUDE = DAILY_AMPLITUDE / 12

        timestamp = None

        base = datetime.datetime.today()
        hours_list = [base + datetime.timedelta(hours = x) for x in range(8760)]
        time_series = []

        average_temp = 21
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


if __name__ == '__main__':
    # for i in range(100):
    #     print(generate_data_dict())

    # print(int(time.asctime()[-7:-5]) / 7.5)
    new_list = []
    print(new_list.pop())
