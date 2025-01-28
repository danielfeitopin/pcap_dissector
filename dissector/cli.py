import argparse
from argparse import ArgumentParser

def create_parser() -> ArgumentParser:
    parser = argparse.ArgumentParser(prog='python -m dissector', description='PCAP Dissector CLI')
    parser.add_argument('-i', '--pcap-input', type=str, required=True, help='Path to the input PCAP file')
    parser.add_argument('-o', '--csv-output', type=str, required=True, help='Path to the output CSV file')
    return parser

ARGPARSER: ArgumentParser = create_parser()
ARGS: dict = {"-i": "pcap_input", "-o": "csv_output"}