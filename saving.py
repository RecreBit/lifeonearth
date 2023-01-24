import time
import datetime
now = datetime.datetime.now()

press = "18 k/P"
humidity = "32%"
var3 = "algo"
geo = "5464785684n 3475389743s"
timenow = time
writevar = "Pressure is: " + press + " / Humidity is: " + humidity + " / This random var is: " + var3 + " / We are at: " + geo + " / Time is: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n"
with open('data.txt', "a") as f:
    f.write(writevar)

