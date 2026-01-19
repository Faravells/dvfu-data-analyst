import random
import time

temperature = 10.25 #градусы
humidity = 60.35 #проценты
pressure = 790.45 #мм.рт.ст.
windSpeed = 20.75 #км/ч
while True:
    temperature += round(random.uniform(-0.05, 0.05), 2)
    humidity += round(random.uniform(-0.05, 0.05), 2)
    pressure += round(random.uniform(-0.05, 0.05), 2)
    windSpeed += round(random.uniform(-0.1, 0.1), 2)
    time.sleep(1)
