'''
    Publisher of application
'''

import paho.mqtt.client as mqtt
import random
import math
import time
import json
from util import generate_data_dict

BROKER = 'mqtt.eclipseprojects.io'
CLIENT = mqtt.Client()
PORT = 1883         # port 1883 - unencrypted TCP
TOPIC = 'relativeHumidity'

print(f'Connecting to broker: {BROKER}')
CLIENT.connect(BROKER, PORT)  

CLIENT.loop_start()
while True:
    hum_dict = generate_data_dict()     # generate data point
    hum_json_str = json.dumps(hum_dict) # formated json string
    
    CLIENT.publish(
        topic = TOPIC,
        payload = hum_json_str
    )

    print(f'Publishing to topic: {TOPIC}\nWith payload: {hum_json_str} + to {BROKER}')
    time.sleep(5)

