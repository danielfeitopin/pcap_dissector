import csv
import pyshark
from .config import MAX_ROWS


def process_pcap(input_file: str, fields: list[str], output_file: str, max_rows: int = MAX_ROWS) -> None:

    # Open PCAP for reading
    cap = pyshark.FileCapture(input_file, keep_packets=False)  # Select PCAP

    # Open CSV for writing
    with open(output_file, 'w', newline='') as f:

        csvwriter = csv.writer(f)  # Get CSV writer
        csvwriter.writerow(fields)  # Write CSV header

        # Iterate over each packet
        counter: int = 0 # Number of read packets
        for packet in cap:
            row = []
            for field in fields:
                try:
                    layer_name, attr = field.split('.', 1)
                    if layer_name == "frame_info":
                        value = packet.frame_info.get(attr)
                    else:
                        value = packet[layer_name].get(attr)
                    row.append(value if value is not None else "")
                except (KeyError, AttributeError):
                    #print("Error") # DEBUG
                    row.append("")
            counter += 1
            print(f"\rWriting row {counter}", end='')
            csvwriter.writerow(row)

            if counter == max_rows:
                break

        print(" Done!")
