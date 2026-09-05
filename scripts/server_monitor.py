import psutil

print("===== LINUX SERVER MONITOR =====")

# CPU
cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu}%")

# Memory
memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}%")

# Disk
disk = psutil.disk_usage("/")
print(f"Disk Usage: {disk.percent}%")

# Alerts
if cpu > 80:
    print("WARNING: High CPU usage!")

if memory.percent > 80:
    print("WARNING: High Memory usage!")

if disk.percent > 80:
    print("WARNING: High Disk usage!")

print("==============================")
