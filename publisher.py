"""
Created on Fri 5 Aug 2022
@author: COMP216 Assignment 3 - Group 5
publisher.py

Ankit Mehra    - 301154845
Bruno Morgado  - 301154898
Mark Randall   - 301178066
"""

import paho.mqtt.client as mqtt
import sys
import time
import json
from util import Util


class Publisher:
    ONLINEBROKER = 'mqtt.eclipseprojects.io'
    LOCALBROKER = "localhost"  # have to install
    PORT = 1883  # port 1883 - unencrypted TCP --- this is a default

    def __init__(self, delay: float = 0.5, topic: str = 'relative-Humidity') -> None:
        self.gen = Util()
        self.client = mqtt.Client()
        self.topic = topic
        self.delay = delay

    def publish(self):
        x = 0
        if self.client.connect(Publisher.ONLINEBROKER, Publisher.PORT) == 0:  # default port is 1883
            print(f'Connected to broker: {Publisher.ONLINEBROKER}')
            self.client.loop_start()
            while True:
                x += 1
                print(f'#{x}', end=' ')
                self.__publishTemprature()
        else:
            print("Could not connect to MQTT broker")  # if not able to connect
            sys.exit(-1)

    def __publishHumidity(self):
        # formatted json string
        hum_dict = self.gen.generate_humid_data() # generate data point
        hum_json_str = json.dumps(hum_dict)
        self.client.publish(
            topic=self.topic,
            payload=hum_json_str)
        print(f'Publishing to topic: {self.topic}\nWith payload: {hum_json_str}')
        time.sleep(2)
      
    def __publishTemprature(self):  
        # while True:
        time_series = self.gen.generate_temp_data()
        for series in time_series:
            dict_str = json.dumps(series)
        self.client.publish("TorontoTemp", payload=dict_str)
        print('Publishing data: ' + str(dict_str) + ' to Networking COMP216 Group 5 TorontoTemp')
        time.sleep(1)

def main():
    pub = Publisher('TorontoTemp')
    pub.publish()


if __name__ == "__main__":
    main()
