'''
    Publisher of application
'''

import paho.mqtt.client as mqtt
import random
import math
import time
import json
from util import Util


class Publisher:
    BROKER = 'mqtt.eclipseprojects.io'
    CLIENT = mqtt.Client()
    PORT = 1883  # port 1883 - unencrypted TCP

    def __init__(self, delay: float = 0.5, topic: str = 'relativeHumidity') -> None:
        self.gen = Util()
        self.client = mqtt.Client()
        self.topic = topic
        self.delay = delay

    def publish(self, times=20):
        for x in range(times):
            print(f'#{x}', end=' ')
            self.__publish()

    def __publish(self):
        Publisher.CLIENT.loop_start()
        hum_dict = self.gen.generate_data_dict()  # generate data point
        hum_json_str = json.dumps(hum_dict)  # formatted json string
        print(f'Connecting to broker: {Publisher.BROKER}')
        Publisher.CLIENT.connect(Publisher.BROKER, Publisher.PORT)
        Publisher.CLIENT.publish(
            topic=self.topic,
            payload=hum_json_str
        )
        print(f'Publishing to topic: {self.topic}\nWith payload: {hum_json_str} + to {Publisher.BROKER}')
        time.sleep(5)


pub = Publisher()
pub.publish(10)
