#!/usr/bin/env python3
import sys
import json
import requests
import warnings
warnings.filterwarnings("ignore")

THEHIVE_URL = "http://143.198.164.142:9000"
THEHIVE_API_KEY = "5fYnSpYloZSyRDq+SlRbC6UrTUeWG+Fg"

def create_alert(alert_file):
    with open(alert_file) as f:
        alert = json.load(f)

    rule_id = alert.get("rule", {}).get("id", "unknown")
    rule_desc = alert.get("rule", {}).get("description", "Wazuh Alert")
    rule_level = alert.get("rule", {}).get("level", 0)
    agent_name = alert.get("agent", {}).get("name", "unknown")
    timestamp = alert.get("timestamp", "")

    severity = 1
    if rule_level >= 10:
        severity = 3
    elif rule_level >= 7:
        severity = 2

    payload = {
        "title": f"[Wazuh] {rule_desc}",
        "description": f"Rule ID: {rule_id}\nAgent: {agent_name}\nLevel: {rule_level}\nTimestamp: {timestamp}\n\nFull alert:\n{json.dumps(alert, indent=2)}",
        "type": "wazuh",
        "source": "wazuh",
        "sourceRef": f"wazuh-{rule_id}-{timestamp}",
        "severity": severity,
        "tags": ["wazuh", f"rule-{rule_id}", agent_name]
    }

    headers = {
        "Authorization": f"Bearer {THEHIVE_API_KEY}",
        "Content-Type": "application/json"
    }

    requests.post(
        f"{THEHIVE_URL}/api/v1/alert",
        headers=headers,
        json=payload,
        verify=False
    )

if __name__ == "__main__":
    create_alert(sys.argv[1])
    sys.exit(0)
