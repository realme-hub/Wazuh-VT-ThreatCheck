WAZUH-VT-THREATCHECK
An Integrated Framework for Automated Threat Intelligence & Incident Response

This project demonstrates the deployment and configuration of Wazuh SIEM integrated with:

✔ VirusTotal

✔ AlienVault OTX

✔ MITRE ATT&CK

✔ File Integrity Monitoring (FIM)

✔ Active Response

✔ Docker Single-Node Deployment

✔ Windows Agent Monitoring

📝 1. Project Overview

This project builds a complete security monitoring environment using Wazuh SIEM, enhanced with multiple threat-intelligence and automated response integrations.

You will see:

Real-time alerts

MITRE ATT&CK mapping

Automatic VirusTotal scan

OTX threat lookup

File integrity monitoring

Automated Active Response

Full documentation is available in:
📄 Final_Wazuh_Project_Report.pdf

⚙️ 2. Installation — Step-by-Step
A. Install Docker Desktop (Windows)

Download from: https://docs.docker.com/desktop/setup/install/windows-install/

Enable WSL 2

Open PowerShell and run:

docker --version
docker info

B. Install Git (Windows)

Download from:
https://git-scm.com/download/win

C. Clone Wazuh Docker Repo

Open PowerShell:

git clone https://github.com/wazuh/wazuh-docker.git -b v4.14.0
cd wazuh-docker/single-node/

D. Generate Certificates
docker compose -f generate-indexer-certs.yml run --rm generator

E. Deploy Wazuh
docker compose up -d
docker ps

F. Access Wazuh Dashboard
https://localhost
username: admin
password: SecretPassword

🖥️ 3. Windows Agent Installation

Download from:
https://documentation.wazuh.com/current/installation-guide/wazuh-agent/wazuh-agent-package-windows.html

Edit:

C:\Program Files (x86)\ossec-agent\ossec.conf


Add:

<server-address>127.0.0.1</server-address>


Restart agent:

net stop wazuh
net start wazuh

🔍 4. File Integrity Monitoring (FIM)

Detects file/registry modifications

Generates alerts with Rule ID 751

View:
Wazuh Dashboard → Integrity Monitoring

🦠 5. VirusTotal Integration

Add to wazuh-manager.conf:

<integration>
  <name>virustotal</name>
  <api_key>YOUR_API_KEY</api_key>
  <group>syscheck</group>
  <alert_format>json</alert_format>
</integration>


Test using EICAR:

Invoke-WebRequest -Uri "https://secure.eicar.org/eicar.com.txt" -OutFile "C:\Users\Public\eicar.com.txt"

🌍 6. AlienVault OTX Integration

Get API key:
https://otx.alienvault.com

Create Python script:

alienvault-otx.py


Add integration to:

/var/ossec/etc/ossec.conf

🔥 7. Active Response

Add:

<active-response>
  <command>firewall-drop</command>
  <location>all</location>
  <level>6</level>
</active-response>


Check:

/var/ossec/logs/active-responses.log

🧠 8. MITRE ATT&CK Mapping

Automatically maps alerts

View:
Dashboard → MITRE ATT&CK

🧪 9. Testing & Results

FIM alerts work

VirusTotal scan detects EICAR

OTX reputation lookup works

MITRE mapping shows technique IDs

Active Response blocks attacks

📦 10. Project Folder Structure (for GitHub)
Wazuh-VT-ThreatCheck/
│
├── README.md
├── Final_Wazuh_Project_Report.pdf
│
├── configs/
│   ├── ossec.conf
│   ├── agent.conf
│   └── wazuh-manager.conf
│
├── docker-setup/
│   ├── docker-compose.yml
│   └── generate-indexer-certs.yml
│
├── integrations/
│   ├── alienvault-otx.py
│   └── virustotal.conf
│
└── screenshots/
    ├── dashboard.png
    ├── fim.png
    ├── mitre.png
    └── virustotal.png

🚀 11. Deployment Commands

Clone:

git clone https://github.com/USERNAME/Wazuh-VT-ThreatCheck


Start Wazuh:

docker compose up -d


Dashboard URL:

https://localhost
username: admin
password: SecretPassword

👨‍💻 Author

Athul
Cybersecurity Student
Kerala, India
