import csv
from datetime import datetime
from time import sleep
import psutil
import time

# Library for getting indicators -> https://psutil.readthedocs.io/en/latest/

# ENV vars
CSV_FILENAME = "my_first_dataset.csv"


def current_milli_time() -> int:
    """
    This function returns the current time in milliseconds
    :return:
    """
    return round(time.time() * 1000)


def read_data() -> dict:
    """
    This function reads data from the system
    :return: a dictionary
    """
    data_dict = {"time": current_milli_time(), "datetime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    cpu_probe(data_dict)
    vm_probe(data_dict)
    return data_dict


def cpu_probe(data_dict:dict):
    """
    This function reads CPU data from the system and uses it to update a dict
    """
    cpu_t = psutil.cpu_times()
    data_dict["idle_time"] = cpu_t.idle
    data_dict["usr_time"] = cpu_t.user
    data_dict["interrupt_time"] = cpu_t.interrupt


def vm_probe(data_dict:dict):
    """
    This function reads VM data from the system and uses it to update a dict
    """
    vm_data = psutil.virtual_memory()
    data_dict["mem_total"] = vm_data.total
    data_dict["mem_available"] = vm_data.available
    data_dict["mem_percent"] = vm_data.percent


def write_dict_to_csv(filename, dict_item, is_first_time):
    """
    This function writes a dictionary as a row of a CSV file
    :param filename: name where to save file to
    :param dict_item: dict to save
    :param is_first_time: if true, writes header and overrides existing file
    :return:
    """
    if is_first_time:
        f = open(filename, 'w', newline="")
    else:
        f = open(filename, 'a', newline="")
    w = csv.DictWriter(f, dict_item.keys())
    if is_first_time:
        w.writeheader()
    w.writerow(dict_item)
    f.close()


if __name__ == "__main__":
    """
    Main of the monitor
    """
    is_first_time = True
    while True:
        start_t = current_milli_time()
        # Monitors PSUtil data
        monit_data = read_data()
        print(monit_data)
        sleep_ms = 1000 + current_milli_time() - start_t
        sleep(sleep_ms/1000)
        write_dict_to_csv(CSV_FILENAME, monit_data, is_first_time)
        is_first_time = False
