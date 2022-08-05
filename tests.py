import time
import datetime
import random
import math


# obj = time.localtime()

# print(obj)
# print(obj.tm_sec)
# print(obj.tm_hour)

# series = [gauss(0.0, 0.05) for i in range (86400)]

# series = Series(series)

# print(series.max())

DAILY_AMPLITUDE = 10

HOURLY_AMPLITUDE = DAILY_AMPLITUDE / 12

# while(True):
#     # noise = random.randint(-100,100) / 500
#     noise = random.gauss(0, 0.05)
#     # timestamp = time.asctime()
#     local_time = time.localtime()
#     # hour = local_time.tm_hour
#     minute = local_time.tm_min
#     second = local_time.tm_sec
#     timestamp = time.asctime(local_time)
#     # x = (int(timestamp[-7:-5]) / 7.5) -4  # generate a number from -4 to 4



#     # hour_in_seconds = hour * 60 * 60
#     # minute_in_seconds = minut4e * 60
#     # minutes_in_seconds = minute * 60
#     # Minute temperature oscilation of 0.006944444444444444 (from 16 to 26 celsius daily)
#     # Print the hourly oscilation every second
#     hourly_temp_oscilation = DAILY_TEMP_OSCILATION / 24
        
#     # x = (hour_in_minutes + minute) * temp_second_oscilation + 16
#     x = second

#     print(temp_second_oscilation)
#     print(f'X = {x}')

#     # y = math.sin(x) * 1.5 + 18 + noise
#     # temp_minute_oscilation = temp_second_oscilation * 60
#     y = temp_second_oscilation * math.sin(x) + 16 + noise

#     print(f'Y = {y}')
#     print(f'Noise: {noise}')
#     time.sleep(1)


days = [d for d in range(1,31)]
hours = [h for h in range(0,24)]


# timestamp = time.asctime()
local_time = time.localtime()

# base = datetime.datetime.today()
# days_list = [base + datetime.timedelta(days = float(x)) for x in range(365)]

base = datetime.datetime.today()
hours_list = [base + datetime.timedelta(hours = x) for x in range(8760)]

# print(hours_list)
# print(hours_list[0].hour)

average_temp = 21
change = 5

for h in hours_list:
    noise = random.gauss(0, 1)
    print(f'Hour: {h.hour}')
    if h.hour >= 6 and h.hour < 18:
        change += HOURLY_AMPLITUDE
    else:
        change -= HOURLY_AMPLITUDE
    print(f'Change: {change}')
    y = average_temp + DAILY_AMPLITUDE * math.sin((math.pi * change) / 30) + noise
    print(f'Y: {y}')
    time.sleep(2)