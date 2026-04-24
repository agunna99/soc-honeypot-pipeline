# SOC Honeypot Pipeline

A production-grade, end-to-end Security Operations Centre (SOC) pipeline built for real-world threat detection and automated incident response.

## Architecture
## Components

| Component | Role | Server |
|---|---|---|
| OpenCanary | Honeypot — captures real attacker TTPs | 164.92.125.22 |
| Wazuh | SIEM — log analysis, alerting, correlation | 146.190.133.43 |
| Shuffle | SOAR — automated alert enrichment and routing | 146.190.133.43 |
| TheHive | Incident Response — case management | 143.198.164.142 |

## What It Does

1. OpenCanary runs fake SSH, FTP, HTTP and Telnet services
2. Real attackers interact with the honeypot within minutes of deployment
3. Wazuh agent ships honeypot logs to the Wazuh manager
4. Custom Wazuh rules fire at level 12-15 for honeypot interactions
5. Wazuh triggers Shuffle via webhook on every level 7+ alert
6. Shuffle workflow processes and enriches the alert
7. TheHive automatically receives an alert and creates an incident case

## Real Threat Intelligence Captured

This pipeline has captured real SSH brute force attacks including:
- Attacker IPs from multiple countries
- Real credentials being attempted
- Attack timing and frequency patterns
- SSH client fingerprints

## Stack

- **OpenCanary** - Honeypot
- **Wazuh 4.9.2** - SIEM
- **Shuffle** - SOAR
- **TheHive 5.5** - Incident Response

## Author

Favour Nmosi — Cybersecurity Engineer
Global Talent Visa Portfolio Project
GitHub: https://github.com/agunna99
