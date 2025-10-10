# Very simple example of network monitoring with pyshark
import csv

import pyshark

CSV_FILENAME = "pyshark_log.csv"


def write_dict_to_csv(filename, dict_item, is_first_time):
    """
    This function writes a dictionary as a row of a CSV file
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


first_time = True
capture = pyshark.LiveCapture(interface='Wi-Fi')
for packet in capture:
    packet_dict = {}
    packet_dict["length"] = packet.length
    packet_dict["layer"] = packet.highest_layer
    packet_dict["timestamp"] = packet.sniff_timestamp
    packet_dict["ip_src"] = packet.ip.src
    packet_dict["ip_dst"] = packet.ip.dst
    write_dict_to_csv(CSV_FILENAME, packet_dict, first_time)
    first_time = False