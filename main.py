# Import modules
from skyfield.api import wgs84, load
from skyfield import api
from skyfield.framelib import itrs
import datetime
from sense_hat import SenseHat
import time

# Define variables
ts = load.timescale()
sense = SenseHat()
eph = load('de421.bsp')
earth, moon = eph['earth'], eph['moon']

# Run the code
while True:
    now = datetime.datetime.now()
    humidity = sense.get_humidity()
    press = sense.get_pressure()
    temperature = sense.get_temperature()
    timenow = time
    
    # Get the current date and time
    t = ts.now()

    # Get the position of the Moon at the current date and time
    position = moon.at(t)

    # Get the geocentric latitude, longitude, and distance of the Moon
    ra, dec, distance = position.radec()

    # Convert the right ascension value from hours to degrees
    ra = ra._degrees / 15
    writevar = "Pressure: " + str(press) + " | Humidity: " + str(humidity) + " | Temperature: " + str(temperature) + " | Timestamp: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n"
    header = ['Declination', 'Right Ascension', 'Timestamp']
    row = ['{:.4f}'.format(dec.degrees), '{:.4f}'.format(ra), now.strftime("%Y-%m-%d %H:%M:%S")]
    writer = csv.writer(f)
    writer.writerow(header)
    
    with open('data.csv', 'a', newline='') as f:
        writer.writerow(row)

    # Wait for 30 seconds before redoing everything
    time.sleep(30)

