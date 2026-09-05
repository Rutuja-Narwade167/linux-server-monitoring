# Linux Server Monitoring & Application Log Analyzer

## Project Overview

This project is a Linux server monitoring and application log analysis tool developed using Python and Shell Scripting.

It monitors basic server resources such as CPU, memory, and disk usage and analyzes application logs to identify INFO, WARNING, and ERROR messages.

## Features

- Monitor CPU usage
- Monitor memory usage
- Monitor disk usage
- Analyze application logs
- Count INFO, WARNING, and ERROR messages
- Display error details
- Generate monitoring reports
- Automate monitoring using Shell Script

## Technologies Used

- Linux
- Amazon Linux 2023
- Python 3
- Shell Scripting
- Git
- GitHub
- psutil

## Project Structure

```text
linux-monitoring-project/
│
├── logs/
│   └── application.log
│
├── reports/
│   └── report.txt
│
└── scripts/
    ├── server_monitor.py
    ├── log_analyzer.py
    └── run_monitoring.sh

How to Run
1. Run Server Monitoring
python3 scripts/server_monitor.py
This displays CPU, memory, and disk usage.
2. Run Log Analyzer
python3 scripts/log_analyzer.py
This analyzes the application log and counts INFO, WARNING, and ERROR messages.
3. Run Complete Monitoring
./scripts/run_monitoring.sh
This runs server monitoring and application log analysis together and generates a report.
4. View Generated Report
cat reports/report.txt
Sample Output
===== LINUX SERVER MONITOR =====
CPU Usage: 0.5%
Memory Usage: 37.3%
Disk Usage: 29.2%
Sample Log Analysis
===== APPLICATION LOG ANALYZER =====
INFO messages: 5
WARNING messages: 2
ERROR messages: 3
Purpose
This project demonstrates practical Linux server monitoring, application log analysis, Python scripting, Shell scripting, troubleshooting, automation, and Git/GitHub skills useful for Application Support and Production Support roles.
Author
Rutuja Narwade
