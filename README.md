# DNS Log Parser

## Overview

This Python script is designed to parse DNS log files, providing valuable insights into the activity recorded. By analyzing the log file, the script generates reports highlighting the number of records processed, the ranking of clients (IPs) based on the number of queries, and the most queried hosts.

## Features

- Accepts a log file name as a parameter for analysis.
- Generates a summary of the processed records.
- Ranks clients based on the number of queries made.
- Identifies the most queried hosts.
- Presents rankings with both total hits and the percentage they represent from the total records analyzed.
- Sends the parsed data to the Lumu API.

## Usage

To use the script, first you'll need to install the required dependencies:

### Setup Virtual Environment and Install Requirements

To ensure a clean and isolated environment for running the DNS Log Parser, it is recommended to use a virtual environment. Follow the steps below to set up a virtual environment and install the required dependencies:

1. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

Activate the Virtual Environment:

- On Windows:
```bash
.\venv\Scripts\activate
```

- On macOS/Linux:
```bash
source venv/bin/activate
```

2. Install Dependencies:

```bash
pip install -r requirements.txt
```

Now, your virtual environment is set up, and the required dependencies are installed.

After dependencies are installed, simply run the script with the desired DNS log file as a parameter, you can also input the collector ID and API key as parameters, this will send the parsed data to the lumu API. If these parameters are not provided, the script will only generate the stats report.

```bash
python main.py -f <log_file_name> -c <collector_id> -k <api_key>
```

## Sample Output
Upon execution, the script will provide output similar to the following:

```
Total records: 16967

Client IPs Rank
---------------  ----  ------
111.90.159.121   3375  19.89%
45.231.61.2      1251  7.37%
187.45.191.2     1089  6.42%
190.217.123.244   738  4.35%
5.63.14.45        634  3.74%
---------------  ----  ------

Host Rank
--------------------------------------------  ----  ------
pizzaseo.com                                  4626  27.26%
sl                                            3408  20.09%
MNZ-efz.ms-acdc.office.com                      67  0.39%
global.asimov.events.data.trafficmanager.net    31  0.18%
www.google.com                                  30  0.18%
--------------------------------------------  ----  ------
```