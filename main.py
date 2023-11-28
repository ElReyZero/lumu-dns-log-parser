import os
import argparse

parser = argparse.ArgumentParser(description='Simple DNS Log Parser')
parser.add_argument('-f', '--file', help='Path of the DNS Log File to parse', required=True)


def process_file(file_path):
    print(f"Processing file: {file_path}")
    with open(file_path, 'r') as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    args = parser.parse_args()
    if os.path.isfile(args.file):
        process_file(args.file)
    else:
        print(f"File {args.file} was not found")