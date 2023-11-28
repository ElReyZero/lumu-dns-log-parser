# DNS Log Parser

## Overview

This Python script is designed to parse DNS log files, providing valuable insights into the activity recorded. By analyzing the log file, the script generates reports highlighting the number of records processed, the ranking of clients (IPs) based on the number of queries, and the most queried hosts.

## Features

- Accepts a log file name as a parameter for analysis.
- Generates a summary of the processed records.
- Ranks clients based on the number of queries made.
- Identifies the most queried hosts.
- Presents rankings with both total hits and the percentage they represent from the total records analyzed.

## Usage

To use the script, simply run it with the desired DNS log file as a parameter:

```bash
python main.py -f <log_file_name>
```

## Sample Output
Upon execution, the script will provide output similar to the following:

```
Total Records: 1000

Client IPs Rank
------------ ---- -----
192.168.1.1  300   30%
192.168.1.2  250   25%
192.168.1.3  200   20%
-----------  ----  -----

Host Rank
---------------------  --- -----
example.com            150  15%
subdomain.example.com  120  12%
anotherhost.net        100  10%
---------------------  --- -----
```