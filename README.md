# SSH Log Investigation – Brute Force Detection (Python)

This project simulates a real-world SOC (Security Operations Center) scenario to investigate failed and successful SSH login attempts using Python log parsing.

---

## Scenario Summary

The user `charles.ngwenya` had **6 failed SSH login attempts** followed by **1 successful login** — all from the same IP: `196.54.102.19`.

This pattern strongly suggests a **brute-force attack** that eventually led to a successful login.

---

## Files Included

| File               | Description                                      |
|--------------------|--------------------------------------------------|
| `auth.logs`        | Sample SSH log file                              |
| `log_parse.py`     | Python script to parse logs and export CSV       |
| `login_summary.csv`| Report with failed/success counts and source IPs |
| `REPORT.md`        | Written case report for portfolio/showcase use   |

---

## Skills Demonstrated

- Log Analysis with Regex
- Python Automation for Threat Detection
- Brute-force Detection Logic
- CSV Reporting
- Terminal usage (Git Bash/Linux)

---

## How to Run

1. Ensure Python is installed.
2. Clone this repo or download the files.
3. Run the script:
```bash
python log_parse.py
