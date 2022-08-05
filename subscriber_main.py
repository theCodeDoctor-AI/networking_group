from pyexpat.errors import messages
import paho.mqtt.client as mqtt
import json
import time
import sys
import threading
from tkinter import Tk, Canvas, Frame, BOTH, W, Button, Label

# Subscriber.py

# brokers
onlineBroker = "mqtt.eclipseprojects.io"
localBroker = "localhost"
topic = "relative-Humidity"

# create client
client = mqtt.Client()

DATA_COUNT = 40
data = []  # to store the received data


# decode and print the message when received
def on_message(client, userdata, message):
    data = message.payload.decode("utf-8")
    rec_obj = json.loads(data)
    updated_time = rec_obj["timestamp"]
    data.append(rec_obj["humidity"])  # append new data to the queue
    print(f'Message received:  {updated_time}\nHumidity Data:{data[-1]}')
    print("data: ", data)
    if len(data) >= DATA_COUNT:  # if data is full, pop the first one
        data.pop(0)


def run_forever() -> None:
    try:
        print("Press CTRL+C to disconnect")
        client.loop_forever()
        # client.loop_start()
    except:
        print("Disconnecting from broker")
    client.disconnect()


def start_client() -> None:
    client.on_message = on_message
    # connect to broker
    # print(client.connect (broker, 1883))
    if client.connect(onlineBroker, 1883) == 0:

        client.subscribe(topic)
        print(f'Subscribing to {onlineBroker}')
        time.sleep(2)
        # run_forever()
    else:
        print("Could not connect to MQTT broker")
        sys.exit(-1)

    run_forever()
    # client.loop_start()
    # client.disconnect()


if __name__ == "__main__":
    start_client()
