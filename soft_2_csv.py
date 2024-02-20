import argparse
import pickle
from load_soft import load_soft


def parse_args():
    """grab input and output file location"""
    parser = argparse.ArgumentParser(description="Command line tool to convert soft file from GEO to a sample sheet")
    
    # Add positional arguments
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    # Add optional arguments
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")

    return parser.parse_args()

def main():
    args = parse_args()
    lines = load_soft(args.input_file)
    
if __name__ == "__main__":
    main()

