CREATE DATABASE IF NOT EXISTS weather_station;
USE weather_station;
CREATE TABLE IF NOT EXISTS weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT(4,2) NOT NULL,
    humidity FLOAT(5,2) NOT NULL,
    pressure FLOAT(5,2) NOT NULL,
    wind_speed FLOAT(4,2) NOT NULL
);
