import paho.mqtt.client as mqtt
import json
import time
import sys


class SubscriberSansGui:
    ONLINE_BROKER = 'mqtt.eclipseprojects.io'
    LOCAL_BROKER = 'localhost'
    PORT = 1883  # port 1883 - unencrypted TCP 
    data = []

    def __init__(self, topic: str = 'relative-Humidity') -> None:
        self.topic = topic
        self.client = mqtt.Client()

    def subscribe(self) -> None:
        self.client.on_message = self.on_message
        if self.client.connect(SubscriberSansGui.ONLINE_BROKER, SubscriberSansGui.PORT) == 0:
            self.client.subscribe('relative-Humidity')
            print(f'Subscriber listening to : {self.topic}\n on {self.ONLINE_BROKER}')
        else:
            print("Could not connect to MQTT broker")
            sys.exit(-1)
        time.sleep(5)

        self.block()

    def on_message(client, userdata, message):  # handler for on_message
        rec_data = message.payload.decode("utf-8")
        rec_obj = json.load(rec_data)
        topic = rec_obj['topic']
        time_sent = rec_obj['timestamp']
        humidity = rec_obj['humidity']
        print(f'Topic:{topic} \nData sending Time:{time_sent}\nHumidity:{humidity}')

    def block(self) -> None:
        try:
            print("Press CTRL+C to disconnect")
            self.client.loop_forever()
        except:
            print("Disconnecting from broker")
        # self.client.disconnect()


def main():
    sub = SubscriberSansGui()
    sub.subscribe()
    sub.block()


if __name__ == "__main__":
    main()
