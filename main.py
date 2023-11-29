# Python core imports
import os
import argparse
from uuid import UUID

# Local imports
from parser.dns_parser import DNSLogParser
from parser.network import send_data_to_api

parser = argparse.ArgumentParser(description='Simple DNS Log Parser')
parser.add_argument('-f', '--file', help='Path of the DNS Log File to parse', required=True)
parser.add_argument('-c', '--collector', help='Collector ID to send data to')
parser.add_argument('-k', '--key', help='Client Key to send data to')

def main(args, file_path):
    print("Starting DNS Log Parser...\n")
    parser = DNSLogParser(file_path)
    parser.process_file()
    if args.collector and args.key:
        try:
            UUID(args.collector)
            UUID(args.key)
        except ValueError:
            print("Collector ID or Client Key is not valid, cannot send data to API.")
            return
        print("\nSending data to API, please wait...")
        send_data_to_api(parser.data, args.collector, args.key)
        print("Data sent to API successfully!")

if __name__ == "__main__":
    args = parser.parse_args()
    if os.path.isfile(args.file):
        main(args, args.file)
    else:
        print(f"File {args.file} was not found")