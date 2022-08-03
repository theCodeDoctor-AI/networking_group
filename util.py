'''
    Utility script for MQTT application
    Houses Util functions for publisher
'''
import random
import math
import time

def generate_data_dict():
    '''Returns a data dictionary containing a timestamp as well as a relative humidity value'''
    noise = random.randint(-100, 100) / 250
       
    base = random.randint(20, 90)           # generate random humiduty value between 10-90
    humidity = math.sin(base) + base + noise

    humidity_dict = {
        'timestamp': time.asctime(),
        'humidity': humidity
    }    

    return humidity_dict



if __name__ == '__main__':
    # for i in range(100):
    #     print(generate_data_dict())

    # print(int(time.asctime()[-7:-5]) / 7.5)
    list = []
    print(list.pop())