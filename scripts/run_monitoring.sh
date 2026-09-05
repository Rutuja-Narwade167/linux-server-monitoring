#!/bin/bash

echo "===== SERVER MONITORING ====="
python3 scripts/server_monitor.py

echo ""
echo "===== APPLICATION LOG ANALYSIS ====="
python3 scripts/log_analyzer.py

echo ""
echo "Monitoring completed successfully."
