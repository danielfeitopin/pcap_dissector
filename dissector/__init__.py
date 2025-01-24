import csv
from pyshark import FileCapture
from .config import MAX_ROWS


def dump_to_csv(cap: FileCapture, fields: list[str], csv_file: str) -> list:

    # Open CSV for writing
    with open(csv_file, 'w', newline='') as f:

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
            print(f"Writing row {counter}")
            print(f"{'-'*20}")
            csvwriter.writerow(row)

            if counter == MAX_ROWS:
                break
