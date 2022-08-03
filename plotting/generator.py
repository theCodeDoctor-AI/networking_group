#%% To change the length (or frequency) of the peaks
import matplotlib.pyplot as plt
import random

def generator_3() -> int:
    return random.gauss(40, 6.0)

number_of_values = 200
y = [generator_3() for _ in range(number_of_values)]
x = [generator_3() for _ in range(number_of_values)]
plt.plot(x, y, 'r.')
plt.show()


# %% to get the peaks and valleys
value = {'base':10, 'delta': 0.15}
def generator_4(increment = True) -> float:
    if increment:
        value['base'] += value['delta']
    else:
        value['base'] -= value['delta']
    return value['base']


number_of_values = 200
y = [generator_4((x % 50) > 24) for x in range(number_of_values)]
plt.plot(y, 'g')
plt.show()

# %% To get the squiggles
import matplotlib.pyplot as plt
import random


def generator_2() -> int:
    '''
    This generator gives you a uniform random number in a 0 to 20
    '''
    return random.randint(0, 8)

number_of_values = 200
y = [generator_2() for _ in range(number_of_values)]
x = [generator_2() for _ in range(number_of_values)]
plt.plot(x, y, 'r+')
plt.show()

# %%
value = {'base':100, 'delta': 1.5}
def generator_4(increment = True) -> float:
    if increment:
        value['base'] += value['delta']
    else:
        value['base'] -= value['delta']
    return value['base']


number_of_values = 500
y = [generator_4((x % 50) > 24) + generator_2() - generator_3() for x in range(number_of_values)]
plt.plot(y, 'g')
plt.show()

# %%
