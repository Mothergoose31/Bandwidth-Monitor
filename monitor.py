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
# 1 kilobyte = 1024 bytes
#1 Byte = 8 Bit 1 Kilobyte = 1,024 Bytes
#1 Megabyte = 1,048,576 Bytes 
#1 Gigabyte = 1,073,741,824 Bytes

    if number > 1024*1024*1024:
        number = number/(1024*1024*1024)*8
        number = str(number) + 'Gigabytes'
    elif number > 1024*1024:
        number = number/(1024*1024)*8
        number = str(number) + 'Megabytes'
    elif number > 1024:
        number = number/1024*8
        number = str(number) + 'Kilobytes'
    else:
        number = str(number) + 'Bytes'

def printStat(val):
    print(convertToBits(val))
