import pyshark
from .config import PCAP_FILE, CSV_FILE

# Load fields
from .fields import FRAME_INFO_FIELDS, STACK_FIELDS, MQTT_FIELDS
fields: list[str] = []
fields += FRAME_INFO_FIELDS
fields += STACK_FIELDS
fields += MQTT_FIELDS

# Ensure paths exist
PCAP_FILE.mkdir(parents=True, exist_ok=True)
CSV_FILE.mkdir(parents=True, exist_ok=True)

cap = pyshark.FileCapture(PCAP_FILE) # Select PCAP

# DEBUG
#print(fields)
# packet = cap[0]
# print(packet)
# print(packet.frame_info)
# print(packet.frame_info.get('time_delta'))

from . import dump_to_csv
dump_to_csv(cap, fields, CSV_FILE) # Get data

print("Done!")