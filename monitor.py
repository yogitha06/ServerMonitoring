import psutil
import time

while True:

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print("-----------------------------")
    print("     SERVER MONITORING")
    print("-----------------------------")

    print("CPU Usage  :", cpu, "%")
    print("RAM Usage  :", ram, "%")
    print("Disk Usage :", disk, "%")

    if cpu > 80:
        print("WARNING: CPU usage is HIGH!")

    if ram > 80:
        print("WARNING: RAM usage is HIGH!")

    if disk > 80:
        print("WARNING: Disk usage is HIGH!")

    time.sleep(5)