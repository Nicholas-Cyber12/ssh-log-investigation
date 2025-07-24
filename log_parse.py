import re
from collections import defaultdict

log_file = 'auth.logs'
user = 'charles.ngwenya'

failed_attempts = 0
successful_logins = 0
import csv
from collections import defaultdict

log_file = 'auth.logs'
user = 'charles.ngwenya'

failed_attempts = 0
successful_logins = 0
source_ips = defaultdict(int)

with open(log_file, 'r') as f:
    for line in f:
        if f"Failed password for {user}" in line:
            failed_attempts += 1
            ip_match = re.search(r'from ([\d\.]+)', line)
            if ip_match:
                ip = ip_match.group(1)
                source_ips[ip] += 1
        elif f"Accepted password for {user}" in line:
            successful_logins += 1
            ip_match = re.search(r'from ([\d\.]+)', line)
            if ip_match:
                ip = ip_match.group(1)
                source_ips[ip] += 1

# Print to terminal
print(f"User: {user}")
print(f"Failed login attempts: {failed_attempts}")
print(f"Successful logins: {successful_logins}")
print("Source IPs involved and count:")
for ip, count in source_ips.items():
    print(f"  {ip}: {count} times")

# Export to CSV
csv_filename = 'login_summary.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['User', 'Failed Attempts', 'Successful Logins'])
    writer.writerow([user, failed_attempts, successful_logins])
    writer.writerow([])  # blank row
    writer.writerow(['Source IP', 'Attempt Count'])
    for ip, count in source_ips.items():
        writer.writerow([ip, count])

print(f"\nCSV report saved as '{csv_filename}' ")
