'''
    Subscriber for humidity application
'''
import paho.mqtt.client as mqtt
import tkinter as tk
import time
import json
from queue import Queue

BROKER = 'mqtt.eclipseprojects.io'
CLIENT = mqtt.Client()

incoming_data = Queue() # custom queue class to hold the data

class Display(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title('Networking Project')
        self.geometry('450x350')
        self.configure(padx=7, pady=5)
        
        # Create Frame
        frame = tk.Frame(self)
        frame.configure(background='lightyellow', padx=10, pady=14)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        ## Dynamic resizing of widgets within Frame
        frame.columnconfigure(tuple(range(10)), weight=1)
        frame.rowconfigure(tuple(range(10)), weight=1)

        ## Grid placement of widgets
        # Frame
        frame.grid(column=0, row=0, sticky='news')

if __name__ == '__main__':
    display = Display()
    display.mainloop()


