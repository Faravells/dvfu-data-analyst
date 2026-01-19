import random
import time

temperature = 10.25 #градусы
humidity = 60.35 #проценты
pressure = 760.45 #мм.рт.ст.
windSpeed = 20.75 #км/ч
while True:
    temperature = round(temperature + random.uniform(-0.05, 0.05), 2)
    if temperature > 15:
        temperature -= 0.1
    if temperature < 5:
        temperature += 0.1
    humidity = round(humidity + random.uniform(-0.05, 0.05), 2)
    if humidity > 100:
        humidity -= 0.1
    if humidity < 0:
        humidity += 0.1
    pressure = round(pressure + random.uniform(-0.05, 0.05), 2)
    if pressure > 790:
        pressure -= 0.1
    if pressure < 720:
        pressure += 0.1
    windSpeed = round(windSpeed + random.uniform(-0.1, 0.1), 2)
    if windSpeed > 50:
        windSpeed -= 0.2
    if windSpeed < 0:
        windSpeed += 0.2
    time.sleep(1)
