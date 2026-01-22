import random
import time
import mysql.connector
import os

temperature = 10.25 #градусы
humidity = 60.35 #проценты
pressure = 760.45 #мм.рт.ст.
windSpeed = 20.75 #км/ч

connection = None
try:
    connection = mysql.connector.connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'),
                                         database=os.getenv('DB_NAME'), port=os.getenv('DB_PORT'))
    print("Генератор данных подключен к базе данных")
except mysql.connector.Error as e:
    print(f"Генератор данных не подключен к базе данных: {e}")
while True:
    sql = f"INSERT INTO weather (temperature, humidity, pressure, wind_speed) VALUES ({temperature}, {humidity}, {pressure}, {windSpeed})"
    if connection is not None:
        try:
            connection.cursor().execute(sql)
            connection.commit()
            print(f"Записаны данные: температура = {temperature}, влажность = {humidity}, давление = {pressure}, скорость ветра = {windSpeed}")
        except mysql.connector.Error as e:
            print(f"Не удалось вставить данные в базу данных: {e}")
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
