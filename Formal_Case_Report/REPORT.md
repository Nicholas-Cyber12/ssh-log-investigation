Nicholas Mabaso
Aspiring Cybersecurity Analyst
🔒 LinkedIn (optional)
📚 Currently completing the Google Cybersecurity Certificate

---

#### `REPORT.md`
# Security Incident Report: SSH Brute-Force Investigation

## Incident Summary

- **User Affected:** charles.ngwenya  
- **Log Source:** auth.logs (Linux SSHD)
- **Date of Events:** July 17  
- **Source IP:** 196.54.102.19  
- **Summary:** A brute-force attack was detected against the user `charles.ngwenya` from a single IP address, resulting in 6 failed login attempts followed by 1 successful login.

---

## Findings

| Category             | Details                          |
|----------------------|----------------------------------|
| Total Failed Attempts| 6                                |
| Successful Logins    | 1                                |
| Source IPs Involved  | 1 unique IP (see below)          |
| IP Address           | 196.54.102.19                    |
| Possible Threat      | Brute-force attack using SSH     |

---

## Log Analysis

### Failed Attempts:

Jul 17 03:20:11 HR-SERVER-01 sshd[3012]: Failed password for charles.ngwenya from 196.54.102.19 port 50015 ssh2
Jul 17 03:20:45 HR-SERVER-01 sshd[3013]: Failed password for charles.ngwenya from 196.54.102.19 port 50016 ssh2
Jul 17 03:21:11 HR-SERVER-01 sshd[3014]: Failed password for charles.ngwenya from 196.54.102.19 port 50017 ssh2
Jul 17 03:21:55 HR-SERVER-01 sshd[3015]: Failed password for charles.ngwenya from 196.54.102.19 port 50018 ssh2
Jul 17 03:22:01 HR-SERVER-01 sshd[3016]: Failed password for charles.ngwenya from 196.54.102.19 port 50019 ssh2
Jul 17 03:23:59 HR-SERVER-01 sshd[3017]: Failed password for charles.ngwenya from 196.54.102.19 port 50020 ssh2

### Successful Attempt:

Jul 17 03:26:20 HR-SERVER-01 sshd[3018]: Accepted password for charles.ngwenya from 196.54.102.19 port 50021 ssh2

---

## Threat Level: **High**

- **Brute-force confirmed**: 6 consecutive failures followed by success.
- **Same IP used**: 196.54.102.19 attempted 7 times.
- **Compromise likely**: Account access was gained.

---

## Recommendations

1. **Reset password** for user `charles.ngwenya` immediately.
2. **Block IP** `196.54.102.19` via firewall or intrusion prevention system (IPS).
3. **Implement Fail2Ban** or similar SSH protection tool.
4. **Enable Multi-Factor Authentication (MFA)** where possible.
5. **Audit all login activity** across the system for lateral movement.
6. **Educate users** about strong password policies.

---

## Outcome

Report generated and exported via Python automation. CSV summaries attached for SOC reference.

---

Report by: **Nicholas Mabaso**  
Cybersecurity Analyst (Trainee)  
