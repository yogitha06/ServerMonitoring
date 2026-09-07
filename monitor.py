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

    if cpu > 10:
        print("ALERT: CPU usage is HIGH!")

    if ram > 10:
        print("ALERT: RAM usage is HIGH!")

    if disk > 10:
        print("ALERT: Disk usage is HIGH!")

    time.sleep(5)