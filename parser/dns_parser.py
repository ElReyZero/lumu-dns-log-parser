# Python imports
from collections import Counter
from datetime import datetime
import re

# Third party imports
from tabulate import tabulate

class DNSLogParser:

    def __init__(self, log_file:str) -> None:
        self.log_file = log_file
        self.clients = dict()
        self.hosts = dict()
        self.data = list()
        self.total_records = 0

    def process_file(self):
        """
        Process the log file line by line and call the process_line method for each line.
        Finally, calls the process_statistics method.
        """
        with open(self.log_file, 'r') as f:
            for line in f:
                self.process_line(line)
        self.process_statistics()

    def process_line(self, line:str):
        """
        Process a line of text and extracts client IP and host name information.

        Args:
            line (str): The line of text to process.

        Returns:
            None
        """

        pattern = r'(\d{1,2}-[a-zA-Z]+-\d{4} \d{2}:\d{2}:\d{2}.\d{3}) queries: info: client @\w+ (\d+\.\d+\.\d+\.\d+).*\((\S+)\): query: (\S+) IN (\S+)'
        matches = re.findall(pattern, line)

        if matches:
            timestamp, client_ip, client_name, host_name, query_type = matches[0]
            self.add_data_to_dict(self.clients, client_ip)
            self.add_data_to_dict(self.hosts, host_name)
            self.total_records += 1
            formatted_timestamp = datetime.strptime(timestamp, "%d-%b-%Y %H:%M:%S.%f").isoformat()
            self.data.append({"timestamp": formatted_timestamp, "name": host_name, "client_ip": client_ip, "client_name": client_name,  "type": query_type})
        else:
            print("No match found.")

    def add_data_to_dict(self, data:dict, key:str):
        if key in data.keys():
            data[key] += 1
        else:
            data[key] = 1

    def process_statistics(self):
        """
        Process the statistics for the DNS log parser.

        This method calculates the top clients and top hosts based on the frequency of occurrence in the log data.
        It also calculates the percentage of records each client and host represents.

        Returns:
            None
        """
        top_clients = list(Counter(self.clients).most_common(5))
        top_hosts = list(Counter(self.hosts).most_common(5))

        for i in range(5):
            top_clients[i] = [top_clients[i][0], top_clients[i][1], f"{round((top_clients[i][1]/self.total_records)*100, 2)}%"]
            top_hosts[i] = [top_hosts[i][0], top_hosts[i][1], f"{round((top_hosts[i][1]/self.total_records)*100, 2)}%"]

        self.print_statistics(top_clients, top_hosts)

    def print_statistics(self, top_clients: list, top_hosts: list):
        """
        Print statistics of the DNS log parser.

        Args:
            top_clients (list): List of top client IPs.
            top_hosts (list): List of top host IPs.

        Returns:
            None
        """
        print("Parsed File Statistics:")
        print(f"Total records: {self.total_records}\n")
        print("Client IPs Rank")
        print(tabulate(top_clients))
        print("\nHost Rank")
        print(tabulate(top_hosts))