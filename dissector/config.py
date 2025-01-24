from pathlib import Path

MAX_ROWS: int = 1e4

# PCAP input files
PCAP_FOLDER: Path = Path('pcapFiles')
PCAP_FILE: Path = PCAP_FOLDER / 'test.pcap'

# CSV output files
CSV_FOLDER: Path = Path('csvFiles')
CSV_FILE: Path = CSV_FOLDER / 'output.csv'