import psutil
import time 

def Bandwidth():
    value = 0
    while True:
        network = psutil.net_io_counters(pernic = True)
        newValue = network['lo'].bytes_sent + network['lo'].bytes_recieved

        if value:
            return  convertToBits(value)

        value = newValue
        return(convertToBits(value))
def convertToBits(number):
    
