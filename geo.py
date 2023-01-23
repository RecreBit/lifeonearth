from skyfield.api import load
import time

print('y')

# Load the necessary data for astronomical calculations
data = load('de421.bsp')

print('x')

# Define the TLE data for the ISS
line1 = '1 25544U 98067A   20336.01571228  .00001452  00000-0  30374-4 0  9990'
line2 = '2 25544  51.6431  31.1234 0017142  94.9079  47.5682 15.53916173076329'

print('xx?')

# Create the satellite object using the TLE data
iss = data.satellites[line1, line2]

while True:
    # Get the current date and time
    current_time = data.now()

    # Calculate the position of the ISS at the current date and time
    print("got here")
    position, velocity = iss.at(current_time).position.km
    print("yes")
    # Print the position in the format (x, y, z)
    print(position)

    # Wait for 30 seconds before recalculating the position
    time.sleep(30)
