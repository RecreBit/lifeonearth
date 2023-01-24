from skyfield.api import wgs84, load
from skyfield import api
from skyfield.framelib import itrs
import time

ts = load.timescale()
eph = load('de421.bsp')
earth, moon = eph['earth'], eph['moon']

while True:
    # Get the current date and time
    t = ts.now()

    # Get the position of the Moon at the current date and time
    position = moon.at(t)

    # Get the geocentric latitude, longitude, and distance of the Moon
    ra, dec, distance = position.radec()

    # Convert the right ascension value from hours to degrees
    ra = ra._degrees / 15

    print('------------------')
    # Print the position of the Moon in geographical coordinates
    print('Right Ascension: {:.4f} degrees'.format(ra))
    print('Declination: {:.4f} degrees'.format(dec.degrees))
    print('Distance Moon to Earth: {:.4f} km'.format(distance.km))
    print('------------------')
    print('')

    # Wait for 30 seconds before recalculating the position
    time.sleep(30)
