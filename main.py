# REQUIREMENT: Monitor that reads free (RAM) memory every 1 second

from time import sleep
import psutil

stored_values = []
i = 0
while i < 10:
    mem_data_read = psutil.virtual_memory()
    stored_values.append(mem_data_read)
    print(mem_data_read.percent)
    sleep(1)
    i = i + 1

# This is the code we built in DCML lecture of Wednesday, Oct 8th.
# Please note that this still has bugs and has to be updated



