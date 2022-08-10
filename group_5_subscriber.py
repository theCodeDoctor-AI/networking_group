# -*- coding: utf-8 -*-
"""
        
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

    Subscriber
        The subscriber accept data from the broker and process it. It will decode the data and decide how to process it.
        This is to be implemented as a GUI application. -- tkinter

    Subscriber – Receiving data from the broker
        You will listen to messages from the broker under an agreed topic.
        You will decode the message and decide how to handle the data.

    Subscriber – Handling the data and absence of or wrong data
        This is where you decide how to keep track of the data, and if you are going for bonus marks, 
        this is also where you have to decide what is out of range data. 
        You also have to be able to detect missing transmissions and handle those gracefully.
        Make sure to only keep track of a certain amount of data, not all data that is received by the subscriber. 
        If you keep track of all the data, your application may eventually run out of memory to keep the data in and crash.

    Subscriber – User interface
        Make an application using the tkinter GUI framework.
        Use a graph to display the data the application has received and will receive in the future.
"""
import paho.mqtt.client as mqtt
import json
import time
import threading
from tkinter import Tk, Canvas, Frame, BOTH, W, Button, Label

# Subscriber.py
class Subscriber:
    def __init__(self, delay=2, broker="mqtt.eclipseprojects.io", port=1883, topic="COMP216Sec001Group5", graph_width=1200, graph_height=850, line_width=1):
        try:
            self.client = mqtt.Client()
            self.client.on_message = self.on_message

            self.broker = broker
            self.port = port
            self.topic = topic
            self.delay = delay

            self.POINT_COUNT = 72
            self.data_list = []  # to store the received data

            self.GRAPH_WIDTH = graph_width
            self.GRAPH_HEIGHT = graph_height
            self.LINE_WIDTH = line_width
        except Exception as e:
            print(f"Exception to initialize the Subscriber: {e}")

    def on_connect(self, client, userdata, flags, rc):
        print ("Connected with result code " + str (rc))

    # decode and print the message when received
    def on_message(self, client, userdata, message):
        try:
            data = message.payload.decode("utf-8")
            obj = json.loads(data)
            updated_time = obj["timestamp"]
            self.data_list.append(obj["temperature"])  # append new data to the queue

            print('message received: ', updated_time, self.data_list[-1])
            print("data_list: ", self.data_list)

            if len (self.data_list) >= self.POINT_COUNT:  # if data is full, pop the first one
                self.data_list.pop(0)
        except Exception as e:
            print(f"Exception to decode the message: {e}")

    def start_client(self):
        try:
            # Subscriber – Connection to the broker
            print(f'Connected to the Broker {self.broker}')
            self.client.connect(self.broker, self.port)
            
            # Subscriber – Subscribing to the topic
            print(f'Subscribing to the topic {self.topic}')
            self.client.subscribe(self.topic)

            time.sleep(self.delay)

            #self.client.loop_forever()
            self.client.loop_start()  # use loop_start() to start a new thread
        except Exception as e:
            print(f"Exception to start the subscriber: {e}")

    def plot(self):
        try:
            # Subscriber – Plotting
            print(f'Starting to plot')
        
            # GUI Display with Tkinter
            display = DynamicDisplay(self, self.GRAPH_WIDTH, self.GRAPH_HEIGHT, self.LINE_WIDTH)
            display.mainloop()
        except Exception as e:
            print(f"Exception to plot the graph with data of the subscriber: {e}")

    def close(self):
        try:
            self.client.loop_stop()
            self.client.disconnect()
        except Exception as e:
            print(f"Exception to close the subscriber: {e}")


class DynamicDisplay(Tk):
    lines = []

    def __init__(self, sub=None, graph_width=1200, graph_height=850, line_width=1):
        try:
            Tk.__init__(self)

            # Connection with Subscriber
            self.sub = sub

            # GUI Display
            self.GRAPH_WIDTH = graph_width
            self.GRAPH_HEIGHT = graph_height
            self.LINE_WIDTH = line_width
            self.LINE_SIZE = (self.GRAPH_WIDTH - 50) / self.sub.POINT_COUNT
            
            self.title('Assignment 3 - Group 5')
            self.createPanel()
            self.initUI()
            self.update()

            self.geometry(f'{self.GRAPH_WIDTH + 50}x{self.GRAPH_HEIGHT + 100}+300+300')
            self.protocol("WM_DELETE_WINDOW", self.on_closing)
        except Exception as e:
            print(f"Exception to initialize DynamicDisplay: {e}")

    # Create Panel with the dimensions
    def createPanel(self):
        self.container = Frame(self)
        self.container.place(
            relx=0,              ##distance from left of parent
            rely=0,              #distance from top of parent
            relwidth=1,           #width of the widget (relative to parent)
            relheight=1) 

    def initUI(self, parent=None):
        try:
            if not parent: parent = self.container

            self.canvas = Canvas(parent, width=900, height=400, bg='#FFF8B3') #Canvas(self, bg='#FFF8B3')
            self.canvas.create_text(30, 30, anchor=W, font='Arial', text='Indoor Temperature Monitor')
            self.canvas.pack(fill=BOTH, expand=1)

            # draw the graph lines and measurements
            # x & y axis
            self.canvas.create_line(25 - self.LINE_WIDTH / 2, 20, 25 - self.LINE_WIDTH / 2, self.GRAPH_HEIGHT)
            self.canvas.create_line(25 - self.LINE_WIDTH / 2, self.GRAPH_HEIGHT, self.GRAPH_WIDTH + 25, self.GRAPH_HEIGHT)

            # measurement labels
            temperature_degrees = 17
            graph_width_decrease = 30
            graph_height_decrease = 30
            for i in range(11):
                temperature_degrees = temperature_degrees + i
                graph_height_decrease += 50

                Label(text=f'{temperature_degrees}\xb0C', bg='#FFF8B3', font=('Arial', 10)).place (x=self.GRAPH_WIDTH - graph_width_decrease, y=self.GRAPH_HEIGHT - graph_height_decrease)

            # guiding lines
            graph_start = 25
            graph_width_decrease = 35
            graph_height_decrease = 30
            for i in range(11):
                graph_height_decrease += 50

                self.canvas.create_line(graph_start, self.GRAPH_HEIGHT - graph_height_decrease, self.GRAPH_WIDTH - graph_width_decrease, self.GRAPH_HEIGHT - graph_height_decrease, fill='#cfcfcf')

            # initialize the data lines
            for i in range(self.sub.POINT_COUNT):
                self.lines.append(self.canvas.create_line (0, 0, 0, 0, fill='#184c8f', width=2))
            self.canvas.pack(fill=BOTH, expand=1)
            self.update()

            # start button
            start_button = Button(text='Start', width=20, command=lambda: self.startBtn())
            start_button.place(x=self.GRAPH_WIDTH - 550, y=self.GRAPH_HEIGHT + 35)

            # stop button
            stop_button = Button(text='Stop', width=20, command=lambda: self.stopBtn())
            stop_button.place(x=self.GRAPH_WIDTH - 350, y=self.GRAPH_HEIGHT + 35)

            # exit button
            exit_button = Button(text='Exit', width=20, command=lambda: self.on_closing())
            exit_button.place(x=self.GRAPH_WIDTH - 150, y=self.GRAPH_HEIGHT + 35)
        except Exception as e:
            print(f"Exception to init Graph UI: {e}")

    # redraw the lines with values in data_list
    def value_change(self):
        try:
            while True:
                for i, line in enumerate(self.lines):
                    if (i >= len(self.sub.data_list) - 1):
                        break
                    else:
                        # this is the y coordinates of point i and i+1
                        # *80 is a scale to match the measurement guiding lines
                        y1 = self.GRAPH_HEIGHT - (self.sub.data_list[i] - 16) * 50
                        y2 = self.GRAPH_HEIGHT - (self.sub.data_list[i + 1] - 16) * 50
                        self.canvas.coords(line, 25 + (i + 1) * self.LINE_SIZE, y2, 25 + i * self.LINE_SIZE, y1)
                # print(data_list[self.sub.POINT_COUNT-1])
                self.update()
                time.sleep(1)
        except Exception as e:
            print(f"Exception to update values: {e}")

    def startBtn(self):
        try:
            # Start the subscriber
            self.sub.start_client()

            # Start the threading
            self.start = threading.Thread(target=self.value_change())
            self.start.setDaemon(True)
        except Exception as e:
            print(f"Exception to start the Thread: {e}")

    def stopBtn(self):
        try:
            # Close the subscriber
            self.sub.close()
        except Exception as e:
            print(f"Exception to stop the Thread: {e}")

    def on_closing(self):
        try:
            # Close the subscriber
            self.sub.close()
            # Destroy the GUI
            self.destroy()
        except Exception as e:
            print(f"Exception to close the GUI: {e}")

def main():
    try:
        # Connection with Subscriber
        sub = Subscriber(graph_width=1000, graph_height=550, line_width=1)
        #sub.start_client()
        sub.plot()
    except Exception as e:
        print(f"Exception with the Subscriber: {e}")

if __name__ == "__main__":
    main()
