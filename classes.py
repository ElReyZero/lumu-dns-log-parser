import re

class DNSLogParser:

    def __init__(self, log_file:str) -> None:
        self.log_file = log_file
        self.clients = dict()
        self.hosts = dict()
        self.total_records = 0

    def process_file(self):
        with open(self.log_file, 'r') as f:
            for line in f:
                self.process_line(line)
        self.print_statistics()

    def process_line(self, line:str):
        """
        Process a line of text and extracts client IP and host name information.

        Args:
            line (str): The line of text to process.

        Returns:
            None
        """

        pattern = r'client @\w+ (\d+\.\d+\.\d+\.\d+).*\((\S+)\):'
        matches = re.findall(pattern, line)

        if matches:
            client_ip, host_name = matches[0]
            self.add_data_to_dict(self.clients, client_ip)
            self.add_data_to_dict(self.hosts, host_name)
            self.total_records += 1
        else:
            print("No match found.")

    def add_data_to_dict(self, data:dict, key:str):
        if key in data.keys():
            data[key] += 1
        else:
            data[key] = 1

    def print_statistics(self):
        """
        Prints the statistics of the DNS log parser.

        This method prints the total number of records, total number of clients, and total number of hosts.
        """
        print(f"Total records: {self.total_records}")
        print(f"Total clients: {len(self.clients)}")
        print(f"Total hosts: {len(self.hosts)}")