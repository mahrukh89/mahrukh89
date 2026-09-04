# MAHRUKH

**Junior Cybersecurity Analyst · SOC Operations · VAPT · Incident Investigation**

<p>
<img src="https://img.shields.io/badge/STATUS-Seeking--Entry--Level--SOC--Role-3fb950?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/TIER-Junior%20%7C%20BS%20Cyber%20Security-a371f7?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/REGION-Lahore%2C%20Pakistan-3671f7?style=flat-square&labelColor=132f4c"/>
</p>

<p>
<a href="https://linkedin.com/in/Ms.mahrukh"><img src="https://img.shields.io/badge/LinkedIn-mahrukh-0A66C2?style=flat-square&logo=linkedin&logoColor=white&labelColor=132f4c"/></a>
<a href="mailto:mahrukhsajj@gmail.com?subject=SOC%20Role%20—%20Opportunity"><img src="https://img.shields.io/badge/Email-mahrukhsajj%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white&labelColor=132f4c"/></a>
<img src="https://img.shields.io/badge/GitHub%20repos-5%20featured-3fb950?style=flat-square&labelColor=132f4c"/>
</p>

> **BS Cyber Security student (graduating 2027)** with hands-on, lab-based experience across SOC operations, incident investigation, vulnerability assessment, and cloud security. I build real, working projects — a firewall, a Sentinel incident investigation, a phishing/threat-intel case, a locked-down AWS bucket, a documented web-app pentest — rather than just collecting certificates. Looking for an entry-level **SOC Analyst**, **Cybersecurity Analyst**, or **Junior VAPT** role.

<p>
<img src="https://img.shields.io/badge/Monitor-132f4c?style=flat-square&labelColor=132f4c&color=58a6ff"/> ➜
<img src="https://img.shields.io/badge/Detect-132f4c?style=flat-square&labelColor=132f4c&color=58a6ff"/> ➜
<img src="https://img.shields.io/badge/Investigate-132f4c?style=flat-square&labelColor=132f4c&color=58a6ff"/> ➜
<img src="https://img.shields.io/badge/Contain-132f4c?style=flat-square&labelColor=132f4c&color=58a6ff"/> ➜
<img src="https://img.shields.io/badge/Report-132f4c?style=flat-square&labelColor=132f4c&color=58a6ff"/>
</p>

---

## 🎓 Education

**BS – Cyber Security** · University of Management and Technology (UMT), Lahore, Pakistan · 2023 – 2027 (Expected)
Coursework: Network Security, Database Systems, Programming (Python, C++), IT Operations

**ICS (Intermediate in Computer Science)** · Aspire College, Jhang, Pakistan · 2021 – 2023

---

## 💼 Experience

**Freelance Project Coordinator** · Self-employed, Lahore, Pakistan · *Feb 2024 – Present*
- Coordinate remote technical projects for distributed teams, managing multiple deadlines and proactively escalating risks
- Maintain timestamped records of decisions and communications for every project

**Project Manager Intern** · Human Alliance Organization (HAO), Lahore, Pakistan · *Jun 2024 – Jul 2024*
- Managed planning and execution of an organizational seminar from concept through delivery
- Coordinated logistics, scheduling, and stakeholder communication

---

## 🛡️ Major Projects — Top 5

| Project | Focus | What it does |
|---|---|---|
| 🔥 **[WebShield Firewall](https://github.com/mahrukh89/webshield-firewall)** | Security Engineering, Traffic Filtering | Designed and built a web application firewall to monitor and filter incoming traffic and harden web app security. |
| 🕵️ **[Simulated CEO Account Takeover Investigation](https://github.com/mahrukh89/ceo-account-takeover-investigation)** | Microsoft Sentinel, KQL | Investigated a simulated account-compromise scenario in Sentinel using KQL — built an incident timeline, documented root-cause analysis and remediation recommendations. *(Simulated lab scenario, test account only.)* |
| 🎣 **[Phishing Email Investigation & Threat Intel](https://github.com/mahrukh89/phishing-threat-intel-investigation)** | OpenCTI, OSINT | Investigated phishing samples via header, URL, and OSINT analysis; correlated IOCs across multiple threat feeds in OpenCTI and documented findings in a threat-intel report. |
| ☁️ **[Secure Cloud Storage](https://github.com/mahrukh89/secure-cloud-storage-aws)** | AWS S3, IAM, CloudTrail | Configured S3 storage with least-privilege IAM policies and enabled CloudTrail logging to monitor and audit access activity. |
| 🧪 **[Security Analysis of OWASP Juice Shop](https://github.com/mahrukh89/owasp-juice-shop-vapt)** | Web Application VAPT | Performed structured web-app penetration testing against OWASP Juice Shop, identified and documented vulnerabilities, then implemented remediation fixes. |

*(Repo links above are guesses based on your project names — swap in your actual repo URLs if they differ.)*

**Also on my radar:** supervised university/personal labs covering CVE-level web-app vulnerability documentation, controlled password-cracking exercises, and Android (Termux) / Ubuntu security testing including reverse-shell communication analysis.

---

## 🔎 Sample Investigation Query

A snippet from the Sentinel account-takeover investigation — flagging impossible-travel-style sign-ins as a starting point for the incident timeline:

```kql
SigninLogs
| where ResultType == 0
| summarize Countries = make_set(LocationDetails.countryOrRegion), SignInCount = count()
    by UserPrincipalName, bin(TimeGenerated, 1h)
| where array_length(Countries) > 1
| order by TimeGenerated desc
```
> Flags a single user signing in successfully from more than one country within the same hour — a common first indicator in an account-takeover timeline, worth cross-referencing with device and IP reputation before escalating.

---

## ⚡ Technical Skills & Tooling

**Security Operations & SIEM**
<img src="https://img.shields.io/badge/Microsoft%20Sentinel-0078D4?style=flat-square&logo=microsoftazure&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Wazuh-3fb950?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Elastic%20Stack-005571?style=flat-square&logo=elastic&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Sigma-FFC107?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Alert%20Triage-58a6ff?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Log%20Analysis-58a6ff?style=flat-square&labelColor=132f4c"/>

**Vulnerability Assessment & Web Security**
<img src="https://img.shields.io/badge/Web%20App%20Pentesting-FF6633?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/CVE%20Documentation-FF4136?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/OWASP-000000?style=flat-square&logo=owasp&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Vulnerability%20Remediation-58a6ff?style=flat-square&labelColor=132f4c"/>

**Incident Response & Threat Intelligence**
<img src="https://img.shields.io/badge/KQL-0078D4?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/MITRE%20ATT%26CK-a371f7?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Root--Cause%20Analysis-58a6ff?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/IOC%20Analysis-58a6ff?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/OSINT-58a6ff?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/OpenCTI-58a6ff?style=flat-square&labelColor=132f4c"/>

**Cloud Security**
<img src="https://img.shields.io/badge/AWS%20S3-FF9900?style=flat-square&logo=amazons3&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/AWS%20IAM-FF9900?style=flat-square&logo=amazonaws&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/CloudTrail-FF9900?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Least--Privilege%20Access-58a6ff?style=flat-square&labelColor=132f4c"/>

**Security Engineering & Frameworks**
<img src="https://img.shields.io/badge/Firewall%20Design-58a6ff?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/NIST-3671f7?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/ISO%2027001-3671f7?style=flat-square&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/CIS%20Controls-3671f7?style=flat-square&labelColor=132f4c"/>

**Programming, Scripting & OS**
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Linux%20(Ubuntu)-FCC624?style=flat-square&logo=linux&logoColor=black&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=windows&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Termux%20(Android)-3DDC84?style=flat-square&logo=android&logoColor=white&labelColor=132f4c"/>

---

## 🔐 Certifications

<img src="https://img.shields.io/badge/Cisco-Ethical%20Hacker-1BA0D7?style=flat-square&logo=cisco&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/TryHackMe-SOC%20Level%201%20Path-212C42?style=flat-square&logo=tryhackme&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Cisco-Cyber%20Threat%20Management-1BA0D7?style=flat-square&logo=cisco&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Cisco-Cybersecurity%20Essentials-1BA0D7?style=flat-square&logo=cisco&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/Cisco-Intro%20to%20Cybersecurity-1BA0D7?style=flat-square&logo=cisco&logoColor=white&labelColor=132f4c"/>
<img src="https://img.shields.io/badge/OPSWAT-ICIP-58a6ff?style=flat-square&labelColor=132f4c"/>

---

## 📊 GitHub Activity

<p>
<img src="https://github-readme-stats.vercel.app/api?username=mahrukh89&show_icons=true&count_private=true&hide_border=true&bg_color=0a1929&title_color=58a6ff&text_color=c9d1d9&icon_color=58a6ff&ring_color=58a6ff" width="48%"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=mahrukh89&layout=compact&hide_border=true&bg_color=0a1929&title_color=58a6ff&text_color=c9d1d9&langs_count=8" width="48%"/>
</p>

<p>
<img src="https://streak-stats.demolab.com?user=mahrukh89&hide_border=true&background=0a1929&stroke=1f6feb&ring=58a6ff&fire=f85149&currStreakNum=c9d1d9&sideNums=c9d1d9&currStreakLabel=58a6ff&sideLabels=c9d1d9&dates=8b949e" width="60%"/>
</p>

---

## 🌍 Quick Facts

| | |
|---|---|
| **Role** | Junior Cybersecurity Analyst |
| **Focus** | SOC Operations · VAPT · Incident Investigation |
| **Open to** | SOC Analyst · Cybersecurity Analyst · Junior VAPT (entry-level) |
| **Location** | Lahore, Punjab, Pakistan |
| **Languages** | English · Urdu · Chinese (Beginner) |
| **Email** | [mahrukhsajj@gmail.com](mailto:mahrukhsajj@gmail.com) |
| **LinkedIn** | [Ms.mahrukh](https://linkedin.com/in/Ms.mahrukh) |

---

<p align="center">
📧 Open to entry-level SOC / cybersecurity opportunities — reach out via LinkedIn or email above.
</p>
