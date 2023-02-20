# Import modules
from orbit import ISS, ephemeris
from skyfield.api import load
from datetime import datetime, timedelta
import csv
from sense_hat import SenseHat
import time

# Define variables
sense = SenseHat()
location = ISS.coordinates()
current = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
          [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
          [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
          [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
          [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
          [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
          [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
          [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

start_time = datetime.now()
now_time = datetime.now()

# Run the code
    
with open('data.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    header = ['Presion (mbar)','Humedad (%)','Temperatura (ºC)','Latitude (º)', 'Longitude (º)','Elevation (m)','Sunlight (T/F)', 'Timestamp']
    writer.writerow(header)
    while (now_time < start_time + timedelta(minutes=2)):
        for i in range(64):
            current[i] = [255,0,0]
            time.sleep(0.05)
            sense.set_pixels(current)
        now = datetime.now()
        humidity = sense.get_humidity()
        press = sense.get_pressure()
        temperature = sense.get_temperature()
        timenow = time
        for i in range(64):
            current[i] = [0,255,255]
            time.sleep(0.05)
            sense.set_pixels(current)
        timescale = load.timescale()
        t = timescale.now()

        hum_final = str(humidity)
        press_final = str(press)
        temp_final = str(temperature)
  
        row = [str(press_final),str(hum_final),str(temp_final),str(location.latitude),str(location.longitude),str(location.elevation.km),ISS.at(t).is_sunlit(ephemeris),now.strftime("%Y-%m-%d %H:%M:%S")]
        writer.writerow(row)
        for i in range(64):
            current[i] = [169,255,69]
            time.sleep(0.05)
            sense.set_pixels(current)
        
        now_time = datetime.now()
        f.flush()
        time.sleep(1)
    f.close()
