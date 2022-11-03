# # gives a single float value
# print(psutil.cpu_percent(interval=1))
# # you can have the percentage of used RAM
# print("RAM%: "+ str(psutil.virtual_memory().percent))
# #tuple with disk space
# lel = psutil.disk_usage('/')
# # print(lel[3])

import psutil, threading

cpu_array = ["0.0"]
ram_array = ["0.0"]
pog_array = ["intro"]

def matrixSetup():
    while True:
        cpuGettter = str(psutil.cpu_percent(interval=1)+4)
        cpu_array.append(cpuGettter)
        ram = str(psutil.virtual_memory().percent)
        ram_array.append(ram)

def threadMatrix():
    a = threading.Thread(target=matrixSetup)
    a.setDaemon(True)
    a.start()

def getDiskFS():
    disk = psutil.disk_usage('/')

    free_space_converter = str(disk[2]-19000000000)
    free_space = free_space_converter[0:3]

    return free_space+"gb"

def getDiskP():
    free_space = float(getDiskFS()[0:3])
    usage_calculation = 100-((100*free_space)/930)
    usage_converted = str(usage_calculation)

    return usage_converted[0:4]+"%"