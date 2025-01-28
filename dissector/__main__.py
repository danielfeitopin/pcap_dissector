import pyshark
from pathlib import Path
from . import process_pcap
from .config import MAKE_OUTPUT_DIR
from .fields import get_fields


def main_cli() -> None:

    from .cli import ARGPARSER, ARGS

    args = ARGPARSER.parse_args()

    INPUT_FILE: Path = Path(getattr(args, ARGS["-i"]))
    OUTPUT_FILE: Path = Path(getattr(args, ARGS["-o"]))
    OUTPUT_DIR: Path = OUTPUT_FILE.parent

    # Ensure the input file exists
    if not INPUT_FILE.is_file():
        raise FileNotFoundError(f"Input file {INPUT_FILE} not found")

    # Ensure the output directory exists
    if not OUTPUT_DIR.is_dir():
        if MAKE_OUTPUT_DIR:
            print(f"Creating directory {OUTPUT_DIR}")
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        else:
            raise FileNotFoundError(f"Output directory {OUTPUT_DIR} not found")

    FIELDS: list[str] = get_fields()

    cap = pyshark.FileCapture(INPUT_FILE)  # Select PCAP
    process_pcap(cap, FIELDS, OUTPUT_FILE)  # Get data


if __name__ == "__main__":

    try:
        main_cli()
        print("Done!")
    except KeyboardInterrupt:
        print("Exiting...")
