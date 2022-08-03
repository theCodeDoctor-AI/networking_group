#%%
import random
import matplotlib.pyplot as plt


class Plotting():
    '''Simple class that generates values and plots.'''

    def __init__(self, min: int, max: int, measurement: str):
        '''
        min         -> minimum acceptable value
        max         -> maximum acceptable value
        measurement -> string representing the values being measured        
        '''
        self.max = max
        self.min = min
        self.measurement = measurement
        self.range = max - min
        self.mid = max + min / 2

    def __generate_base(self) -> float:
        '''Generate list of random numbers for x values in range 0-1'''
        return random.uniform(0, 1)

    def __mutate_base(self) -> float:
        '''Generate values within accepted range'''
        m = self.range
        x = self.__generate_base()
        c = 1
        y = m * (x + c)
        return y

    def __generate_y(self, increment: bool = True) -> float:
        '''Generate the y values in an increasing/decreasing wave pattern.'''
        values = {'base_y': self.max, 'increment': 2}
        if increment:
            values['base_y'] += values['increment']
        else:
            values['base_y'] -= values['increment']
        return values['base_y']

    def __noise(self, mu: int, sigma: int) -> float:
        '''Generate noise to add to the y values'''
        return random.gauss(mu, sigma)


    def plot_values(self, total: int, mu: int, sigma: float, figsize: tuple) -> None:
        '''Plot values. total = numbner of data points.'''
        y = [self.__generate_y((x % self.mid) > (self.mid / 2)) + self.__noise(mu, sigma) for x in range(total)]
        plt.figure(figsize = figsize)
        plt.plot(y, 'g')
        plt.title(
            f'{self.measurement.title()} values on line graph', 
            fontsize = 15, 
            fontweight = 'bold'
            )
        plt.xlabel('x values', fontsize = 12)
        plt.ylabel(f'{self.measurement.title()} values', fontsize = 12)
        plt.show()

#%%
plotting = Plotting(min = 40, max = 70, measurement = 'humidity')
plotting.plot_values(1140, 3, 1.5, (16, 12))

        

# %%
