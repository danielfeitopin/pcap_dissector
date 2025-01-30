# Pcap Dissector

<div align="center">

***Pcap dissector tool made with `pyshark`.***

[![Python](https://img.shields.io/badge/Python-black?logo=python&logoColor=white&labelColor=grey&color=%233776AB)](<#> "Python")
[![tshark](https://img.shields.io/badge/tshark-white?logo=wireshark&logoColor=white&label=%20&labelColor=grey&color=%23D86329)](<#> "tshark")

[![License](<https://img.shields.io/github/license/danielfeitopin/pcap_dissector>)](<LICENSE> "License")
[![GitHub issues](https://img.shields.io/github/issues/danielfeitopin/pcap_dissector)](<https://github.com/danielfeitopin/pcap_dissector> "Issues")
[![GitHub stars](https://img.shields.io/github/stars/danielfeitopin/pcap_dissector)](<https://github.com/danielfeitopin/pcap_dissector/stargazers> "Stars")

</div>

## Table of Contents

- [Pcap Dissector](#pcap-dissector)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [CLI Mode](#cli-mode)
      - [Help](#help)
    - [Web mode](#web-mode)
    - [Docker mode](#docker-mode)
  - [Acknowledgements](#acknowledgements)

## Prerequisites

### Installation

Ensure `tshark` is installed:

```sh
sudo apt install tshark
```

Install Python dependencies from the provided `requirements.txt`:

```sh
pip install -r requirements.txt
```

## Usage

### CLI Mode

Modify [`dissector/config.py`](<dissector/config.py>) and run the `dissector` package as a Python module:

```sh
python3 -m dissector -i path/to/file.pcap -o path/to/file.csv
```

#### Help

A help menu is provided:

```shell
python3 -m dissector -h
```

```
usage: python -m dissector [-h] -i PCAP_INPUT -o CSV_OUTPUT

PCAP Dissector CLI

options:
  -h, --help                              show this help message and exit
  -i PCAP_INPUT, --pcap-input PCAP_INPUT  Path to the input PCAP file
  -o CSV_OUTPUT, --csv-output CSV_OUTPUT  Path to the output CSV file
```

### Web mode

A very simple web interface is provided:

```sh
python3 -m gunicorn -w 2 -b 0.0.0.0 webapp:app
```

### Docker mode

Build docker image from the provided Dockerfile:

```sh
docker build -t dissector .
```

Run the docker container:

```sh
docker run -p "8000:8000" --name dissector dissector
```

Access to the web interface through the binded port: <http://localhost:8000>.

## Acknowledgements

Based on @joseAveleira's work: <https://github.com/joseAveleira/Dissector>.