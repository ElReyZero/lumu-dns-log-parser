import os
import argparse
from classes import DNSLogParser

parser = argparse.ArgumentParser(description='Simple DNS Log Parser')
parser.add_argument('-f', '--file', help='Path of the DNS Log File to parse', required=True)

def process_file(file_path):
    print(f"Processing file: {file_path}")
    parser = DNSLogParser(file_path)
    parser.process_file()


if __name__ == "__main__":
    args = parser.parse_args()
    if os.path.isfile(args.file):
        process_file(args.file)
    else:
        print(f"File {args.file} was not found")