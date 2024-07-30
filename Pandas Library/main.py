import csv
with open("weather_data.csv") as weather:
    weather_today = csv.reader(weather)

import pandas