'''
    Utility script for MQTT application
    Houses Util functions for publisher
    
    Monthly Relative humidity for toronto varies roughly from a minimum of 14% 
    to a maximun of 100%. Therefore a base value of 57% i.e a average of min and
    max humidity can be assumed.
    Source:- https://toronto.weatherstats.ca/charts/relative_humidity-monthly.html
'''

import random
import math
import time

class Util:
    
    def __init__(self) -> None:
        self.start_id = 11
        self.base = 57
    

    def generate_data_dict(self)->dict:
        '''Returns a data dictionary containing a timestamp as well as a relative humidity value'''
        self.start_id += 1
        noise = random.randint(-42, 42)   # so that humidty remains in the range of 14 to 100%
        
        # base = random.randint(20, 90)           # generate random humiduty value between 10-90
        humidity = math.sin(self.base) + self.base + noise

        humidity_dict = {
            'id': self.start_id,
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