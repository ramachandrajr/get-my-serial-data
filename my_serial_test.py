# Importing Required libs.
import serial as ser
from datetime import datetime
from time import strftime
import os
import csv

# This will be later used for serving
# as a serial port object.
my_ser = 0

def init_serial():
    """This function Initiates the Serial port with all the necessary requiremments in a linux machine."""
    # Making the 'my_ser' variable global from here,
    # such that any loop can access it from anywhere
    # inside this function.
    global my_ser
    # 'my_ser' becomes serial port object from here.
    my_ser = ser.Serial()
    # Set the baud rate of the serial port.
    my_ser.baudrate = 9600
    # Set the port name to be the result of 
    # 'dmesg | grep tty' get whatever serial port is
    # active from the above command.
    my_ser.port = '/dev/ttyACM0'
    # Set the timeout value such that processor rests in between.
    my_ser.timeout = 10
    # Open the serial port to get what ever data is coming from it.
    my_ser.open()
    
    # If the serial port is open and working.
    if my_ser.isOpen():
        # Print the serial port name FYI user is not aware of these settings.
        print "Your Serial port is open FYI: " + my_ser.portstr

    # Go on reading forever all the serial data being sent
    while True:
        # Read a line from serial output,
        # i.e., read until you hit the '\r\n' and store in data variable.
        data = str(my_ser.readline())
        # Get the system time from the Computer.
        time = strftime("%a, %d %b %Y %H:%M:%S")
        # Print the time along with the data.
        print "Time:", time,"||",  "Data:", data

# The real program starts here, the whole function is initiated here
try:
    # Try to initiate the whole program.
    init_serial()
except KeyboardInterrupt:
    os.system("clear")
    print "Thats it for today folks"
