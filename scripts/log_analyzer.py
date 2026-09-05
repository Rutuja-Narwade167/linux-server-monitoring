info = 0
warning = 0
error = 0
error_details = []

with open("logs/application.log", "r") as file:
    for line in file:
        if "INFO" in line:
            info += 1
        elif "WARNING" in line:
            warning += 1
        elif "ERROR" in line:
            error += 1
            error_details.append(line.strip())

report = f"""===== APPLICATION LOG REPORT =====

INFO messages: {info}
WARNING messages: {warning}
ERROR messages: {error}

----- ERROR DETAILS -----
"""

for line in error_details:
    report += line + "\n"

report += "\n===== END OF REPORT =====\n"

print(report)

with open("reports/report.txt", "w") as file:
    file.write(report)

print("Report saved successfully!")
