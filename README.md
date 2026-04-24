# SOC Honeypot Pipeline

A production-grade, end-to-end Security Operations Centre (SOC) pipeline built for real-world threat detection and automated incident response.

## Architecture
## Components

| Component | Role | Version |
|---|---|---|
| OpenCanary | Honeypot — captures real attacker TTPs | 0.9.7 |
| Wazuh | SIEM — log analysis, alerting, correlation | 4.9.2 |
| Shuffle | SOAR — automated alert enrichment and routing | Latest |
| TheHive | Incident Response — case management | 5.5.14 |

## What It Does

1. OpenCanary runs fake SSH, FTP, HTTP and Telnet services
2. Real attackers interact with the honeypot within minutes of deployment
3. Wazuh agent ships honeypot logs to the Wazuh manager
4. Custom Wazuh rules fire at level 12-15 for honeypot interactions
5. Wazuh triggers Shuffle via webhook on every level 7+ alert
6. Shuffle workflow processes and enriches the alert
7. TheHive automatically receives an alert and creates an incident case

## Real Threat Intelligence Captured

Within 3 minutes of deployment this pipeline captured real SSH brute force attacks including:
- Attacker IPs from multiple countries
- Real credentials being attempted (usernames and passwords)
- Attack timing and frequency patterns
- SSH client fingerprints (libssh2, OpenSSH for Windows)

## Stack

- **OpenCanary** - Honeypot (SSH, FTP, HTTP, Telnet)
- **Wazuh 4.9.2** - SIEM with custom detection rules
- **Shuffle** - SOAR automation platform
- **TheHive 5.5** - Incident Response & Case Management

## Quick Start

### 1. Deploy Honeypot
```bash
pip install opencanary
cp configs/opencanary.conf /etc/opencanaryd/
systemctl start opencanary
```

### 2. Configure Wazuh Rules
```bash
cp rules/local_rules.xml /var/ossec/etc/rules/
systemctl restart wazuh-manager
```

### 3. Deploy TheHive Integration
```bash
cp integrations/custom-thehive* /var/ossec/integrations/
chmod 750 /var/ossec/integrations/custom-thehive*
```

### 4. Deploy Shuffle
```bash
git clone https://github.com/Shuffle/Shuffle
cd Shuffle && docker compose up -d
```

## Author

Favour Nmosi — Cybersecurity Engineer
Global Talent Visa Portfolio Project
GitHub: https://github.com/agunna99
