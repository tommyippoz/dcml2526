# REQUIREMENT: Monitor that reads free (RAM) memory every 1 second
import csv
import time
from time import sleep
import psutil


def get_current_time_ms():
    """
    This is meant to return a timestamp in ms
    :return: integer timestamp in ms
    """
    return int(time.time()*1000)


stored_values = []
i = 0
while i < 5:
    start_timestamp = get_current_time_ms()
    #print(start_timestamp)
    mem_data_read = psutil.net_io_counters(nowrap=False)
    stored_values.append(mem_data_read)
    i = i + 1
    before_sleep_timestamp = get_current_time_ms()
    #sleep(1)
    sleep((1000-(before_sleep_timestamp-start_timestamp))/1000)

# open the file in the write mode
with open('my_monitor_data.csv', 'w', newline='') as f_desc:
    # create the csv writer
    writer = csv.writer(f_desc)
    # write a row to the csv file
    writer.writerow(["sent","recv"])
    for item in stored_values:
        writer.writerow([item.bytes_sent, item.bytes_recv])
# This is the code we built in DCML lecture of Wednesday, Oct 8th.
# Please note that this still has bugs and has to be updated



