"""
    Publisher of application
    Should have installed mosquitto for local host
    https://mosquitto.org/download/
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

    def publish(self, times=20):
        x = 0
        if self.client.connect(Publisher.ONLINEBROKER, Publisher.PORT) == 0:  # default port is 1883
            print(f'Connected to broker: {Publisher.ONLINEBROKER}')
            self.client.loop_start()
            while True:
                x += 1
                print(f'#{x}', end=' ')
                self.__publish()
        else:
            print("Could not connect to MQTT broker")  # if not able to connect
            sys.exit(-1)

    def __publish(self):
        # formatted json string
        hum_dict = self.gen.generate_data_dict()  # generate data point
        hum_json_str = json.dumps(hum_dict)
        self.client.publish(
            topic=self.topic,
            payload=hum_json_str)
        print(f'Publishing to topic: {self.topic}\nWith payload: {hum_json_str}')
        time.sleep(2)
        


def main():
    pub = Publisher()
    pub.publish()


if __name__ == "__main__":
    main()
