#!/bin/bash python

import psutil
from datetime import datetime
import time
import configparser
import json


class first:
    """return information about natwork and mamory"""
    def network():
        tmp = psutil.net_io_counters().bytes_sent
        return (tmp)

    def vmemory():
        tmp = psutil.virtual_memory().total
        return (tmp)

    def swap():
        tmp = psutil.swap_memory().used
        return (tmp)


i = n = 0

config = configparser.ConfigParser()
config.read("config.ini")
timetosleep = int(config.get("settings", "time"))
reportformat = config.get("settings", "type")
count = int(config.get("settings", "count"))

if count != 0:
    i += 1

report = open("systemstatus." + reportformat, "w")

while i <= count:
    n += 1
    if count != 0:
        i += 1

    if reportformat == "txt":
        temp = "Snapshot " + str(n) + "; " +\
            datetime.now().strftime('%d.%m %H:%M:%S') + "; " + \
            str(psutil.cpu_percent(interval=1)) + "; " +\
            str(first.vmemory()) + "; " + \
            str(first.swap()) + "; " + \
            str(psutil.disk_io_counters().read_count) + "; " +\
            str(psutil.net_io_counters().bytes_sent) + "\n" +\
            str(first.network()) + "\n"
        report.write(temp)
        print(temp)
        time.sleep(timetosleep * 60)

    if reportformat == "json":
        temp = json.dumps({
            "Snapshot number": str(n),
            "Carrent Time": str(datetime.now().strftime('%d.%m %H:%M:%S')),
            "% CPU load": str(psutil.cpu_percent(interval=1)),
            "Memory total": str(first.vmemory()),
            "Swap memory": str(first.swap()),
            "Disk IO": str(psutil.disk_io_counters().read_count),
            "Networks bites send": str(first.network())}, indent=4)
        report.write(temp)
        time.sleep(timetosleep * 60)

report.close()
