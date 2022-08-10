# -*- coding: utf-8 -*-
"""
    Publisher script for MQTT application
    Houses functions for publisher

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

    Publisher
        The publisher will generate one data value at a time to send to the broker at regular intervals indefinitely.
        The data value must be semi-random with a pattern. 
        For example, think of the outdoor temperature around your home: it goes up during the day and down during the night, 
        but still has some momentary fluctuations – it’s never a perfect wave. 
        This is to be implemented as a CLI application. – CLI QUESTIONS 

    Publisher – Value generation
        This must be implemented in a class in a separate file. (Just import the filename without the py extension in the file where you want to use the logic).
        The design should preferably be such that it is easy to use (multiple variation started by just specifying different arguments when starting).

    Publisher – Value generation – Pattern 
        The value generation should show a basic pattern, such as a sine wave, with momentary fluctuations.

    Publisher – Packaging the above values
        The above value must be tagged with at least a time stamp and packaged as a JSON object before transmission. 
        You decide what other features you need to encapsulate in your package.

    Publisher – Sending data to broker
        You must first connect to the broker. To do this, make use of the cloud-hosted MQTT broker at mqtt.eclipseproject.io.
        You will send the above packaged data to the broker under an agreed topic, for example “COMP216Sec001Group1”.
"""
import json
import paho.mqtt.client as mqtt
import time
import sys
from group_5_util import Util

#publisher.py

class Publisher:
    def __init__(self, delay=1, broker="mqtt.eclipseprojects.io", port=1883, topic="COMP216Sec001Group5"):
        try:
            self.gen = Util()
            self.client = mqtt.Client()

            self.broker = broker
            self.port = port
            self.topic = topic
            self.delay = delay
        except Exception as e:
            print(f"Exception to initialize the Publisher: {e}")

    def publish(self, flag='temperature'):
        try:
            x = 0
            # Publisher – Connection to the broker
            if self.client.connect(self.broker, self.port) == 0:
                print(f'Connected to the Broker {self.broker}')
                self.client.loop_start()

                # indefinitely
                while True:
                    x += 1
                    print(f'#{x}', end=' ')
                    if flag == "humidity":
                        self.__publishHumidity()
                    else:
                        self.__publishTemperature()

                self.client.loop_stop()
                self.client.disconnect()    
            else:
                print("Could not connect to MQTT broker")  # if not able to connect
                sys.exit(-1)

        except Exception as e:
            print(f"Exception to connect and publish the message to the Broker: {e}")

    def __publishHumidity(self):
        try:
            # Publisher – Value generation
            # Publisher – Value generation – Pattern 
            hum_dict = self.gen.generateHumidityData() # generate data point
            
            # Publisher – Packaging the above values
            hum_json_str = json.dumps(hum_dict)
            
            # Publisher – Sending data to broker
            self.client.publish(
                topic=self.topic,
                payload=hum_json_str)
            print(f'Publishing to topic: {self.topic}\nWith payload: {hum_json_str}')
            time.sleep(self.delay)
        except Exception as e:
            print(f"Exception to publish and encode the message to the Broker: {e}")

    def __publishTemperature(self):
        try:
            # Publisher – Value generation
            # Publisher – Value generation – Pattern 
            data_time_series = self.gen.generateTemperatureData()
            
            for series in data_time_series:
                # Publisher – Packaging the above values
                temp_json_str = json.dumps(series)

                # Publisher – Sending data to broker
                self.client.publish(self.topic, payload=temp_json_str)
                print(f'Publishing to topic: {self.topic}\nWith payload: {temp_json_str}')
                time.sleep(self.delay)
        except Exception as e:
            print(f"Exception to publish and encode the message to the Broker: {e}")

def main():
    try:
        # Publisher
        pub = Publisher()
        #pub.publish("humidity")
        pub.publish()
    except Exception as e:
        print(f"Exception with the Publisher: {e}")

if __name__ == "__main__":
    main()
