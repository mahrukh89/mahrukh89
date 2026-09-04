<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a1929,50:0f2f4c,100:132f4c&height=230&section=header&text=Mahrukh&fontSize=58&fontColor=ffffff&fontAlignY=38&desc=Junior%20Cybersecurity%20Analyst%20%7C%20SOC%20Operations%20%7C%20VAPT%20%7C%20Incident%20Investigation&descAlignY=58&descSize=16&descColor=c9d1d9&animation=fadeIn" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-OPEN--TO--WORK-2ea44f?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LEVEL-Entry--Level%20%2F%20Junior-a371f7?style=for-the-badge" />
  <img src="https://img.shields.io/badge/BASE-Lahore%2C%20Pakistan-36d1dc?style=for-the-badge" />
</p>

<p align="center">
  <a href="mailto:mahrukhsajj@gmail.com"><img src="https://img.shields.io/badge/Email-mahrukhsajj%40gmail.com-fb9500?style=flat-square&logo=gmail&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/Ms.mahrukh"><img src="https://img.shields.io/badge/LinkedIn-Ms.mahrukh-0A66C2?style=flat-square&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/mahrukh89"><img src="https://img.shields.io/badge/GitHub-mahrukh89-181717?style=flat-square&logo=github&logoColor=white" /></a>
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=900&color=58A6FF&center=true&vCenter=true&width=800&height=50&lines=Junior+SOC+Analyst+%7C+Incident+Investigation;Microsoft+Sentinel+%C2%B7+KQL+%C2%B7+MITRE+ATT%26CK;Web+App+VAPT+%7C+AWS+Cloud+Security;Open+to+entry-level+SOC+%2F+VAPT+roles" alt="Typing SVG" />
</p>

---

name: generate animated snake

on:
  schedule:
    - cron: "0 */6 * * *"   # refreshes every 6 hours
  workflow_dispatch: {}
  push:
    branches: [ main ]

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: generate github-contribution-grid-snake.svg
        uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark

      - name: push github-contribution-grid-snake.svg to the output branch
        uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}


## 🛡️ About Me

I'm a **BS Cyber Security student (graduating 2027)** at UMT Lahore, building hands-on, lab-based experience across **SOC operations, incident investigation, vulnerability assessment, and cloud security** — because I'd rather learn the job by doing it than wait for the degree to finish first.

Currently looking for my **first role as a SOC Analyst, Cybersecurity Analyst, or Junior VAPT Analyst.**

## 🎯 What I Focus On

| Area | What I've Done |
|---|---|
| **SOC & SIEM** | Alert triage and log analysis in Microsoft Sentinel, Wazuh, and Elastic Stack; Sigma-based detection concepts |
| **Incident Response** | Simulated incident investigation in Sentinel using **KQL** — timeline building, root-cause analysis, remediation write-ups |
| **Threat Intelligence** | Phishing/email investigation via header + URL + OSINT analysis; IOC correlation in **OpenCTI** |
| **Web App VAPT** | Structured penetration testing against OWASP Juice Shop and university lab targets; CVE-level vulnerability documentation |
| **Cloud Security** | AWS **S3 + IAM + CloudTrail** — least-privilege access control and audit logging |
| **Security Engineering** | Designed and built a custom web application firewall for traffic filtering |

## 🧰 Tech & Tools

<p>
  <img src="https://img.shields.io/badge/Microsoft%20Sentinel-0078D4?style=flat-square&logo=microsoftazure&logoColor=white" />
  <img src="https://img.shields.io/badge/Wazuh-3FB950?style=flat-square" />
  <img src="https://img.shields.io/badge/Elastic%20Stack-005571?style=flat-square&logo=elastic&logoColor=white" />
  <img src="https://img.shields.io/badge/Sigma-FF6633?style=flat-square" />
  <img src="https://img.shields.io/badge/KQL-2E7D32?style=flat-square" />
  <img src="https://img.shields.io/badge/MITRE%20ATT%26CK-CC2936?style=flat-square" />
  <img src="https://img.shields.io/badge/OpenCTI-005EB8?style=flat-square" />
  <img src="https://img.shields.io/badge/OWASP-000000?style=flat-square&logo=owasp&logoColor=white" />
</p>
<p>
  <img src="https://img.shields.io/badge/AWS%20S3-569A31?style=flat-square&logo=amazons3&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS%20IAM-FF9900?style=flat-square&logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS%20CloudTrail-232F3E?style=flat-square&logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white" />
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux%20(Ubuntu)-FCC624?style=flat-square&logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/Termux-000000?style=flat-square&logo=android&logoColor=white" />
</p>

## 📊 Live GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=mahrukh89&show_icons=true&count_private=true&hide_border=true&bg_color=0D1117&title_color=58A6FF&text_color=C9D1D9&icon_color=58A6FF" height="165" />
  <img src="https://streak-stats.demolab.com?user=mahrukh89&hide_border=true&background=0D1117&stroke=58A6FF&ring=58A6FF&fire=F85149&currStreakLabel=58A6FF" height="165" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=mahrukh89&layout=compact&hide_border=true&bg_color=0D1117&title_color=58A6FF&text_color=C9D1D9" height="165" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=mahrukh89&bg_color=0D1117&color=58A6FF&line=58A6FF&point=C9D1D9&area=true&hide_border=true" width="95%" />
</p>

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=mahrukh89&theme=darkhub&no-frame=true&row=1&column=6&margin-w=8" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mahrukh89/mahrukh89/output/github-contribution-grid-snake-dark.svg" width="95%" />
</p>

## 🧪 Featured Repos · [github.com/mahrukh89](https://github.com/mahrukh89)

| Repo | What It Is |
|---|---|
| 🔥 [**WebShield_Firewall**](https://github.com/mahrukh89/WebShield_Firewall) | A web application firewall for monitoring and filtering incoming traffic to enhance web app security |
| 🐛 [**Security-Analysis-of-OWASP-Juice-Shop**](https://github.com/mahrukh89/Security-Analysis-of-OWASP-Juice-Shop) | Structured threat-modeling framework, security analysis, and hands-on validation against OWASP Juice Shop |
| 🐚 [**reverse-shell-security-lab**](https://github.com/mahrukh89/reverse-shell-security-lab) | Reverse-shell communication on Android (Termux) and Ubuntu in a controlled lab — attack simulation + defensive analysis |
| 🎭 [**social-engineering-security-lab**](https://github.com/mahrukh89/social-engineering-security-lab) | Social-engineering-based exploitation in a controlled environment, with impact analysis and mitigation strategies |
| 🖥️ [**cli-task-manager-cpp**](https://github.com/mahrukh89/cli-task-manager-cpp) | A command-line task manager in C++ — add, view, update, and delete tasks with file handling |

Two additional lab projects from my coursework aren't pushed to public repos yet — a **Simulated CEO Account Takeover Investigation** in Microsoft Sentinel (KQL, incident timeline, root-cause analysis) and a **Phishing Email Investigation & Threat Intelligence** project (OpenCTI, OSINT, IOC correlation). Ask me about either — happy to walk through the write-ups.

## 🎓 University & Personal Security Labs

- Web application security testing in a **supervised university environment**, identifying and documenting CVE-level vulnerabilities; controlled academic password-cracking exercises.
- Controlled **Android (Termux)** and **Ubuntu** security testing on personal devices, including reverse-shell communication analysis and defensive review.

## 📜 Certifications

<p>
  <img src="https://img.shields.io/badge/Cisco-Ethical%20Hacker-1BA0D7?style=flat-square&logo=cisco&logoColor=white" />
  <img src="https://img.shields.io/badge/TryHackMe-SOC%20Level%201%20Path-212C42?style=flat-square&logo=tryhackme&logoColor=white" />
  <img src="https://img.shields.io/badge/Cisco-Cyber%20Threat%20Management-1BA0D7?style=flat-square&logo=cisco&logoColor=white" />
  <img src="https://img.shields.io/badge/Cisco-Cybersecurity%20Essentials-1BA0D7?style=flat-square&logo=cisco&logoColor=white" />
  <img src="https://img.shields.io/badge/Cisco-Intro%20to%20Cybersecurity-1BA0D7?style=flat-square&logo=cisco&logoColor=white" />
  <img src="https://img.shields.io/badge/OPSWAT-ICIP-2E7D32?style=flat-square" />
</p>

## 💼 Experience

**Freelance Project Coordinator** — Self-employed, Lahore, Pakistan · *Feb 2024 – Present*
Coordinate remote technical projects across distributed teams — managing deadlines, escalating risks proactively, and keeping timestamped records of decisions and communications for every project.

**Project Manager Intern** — Human Alliance Organization (HAO), Lahore, Pakistan · *Jun 2024 – Jul 2024*
Managed an organizational seminar end-to-end — logistics, scheduling, and stakeholder communication.

## 🎓 Education

**University of Management and Technology (UMT), Lahore** — BS Cyber Security · *2023 – 2027 (Expected)*
Coursework: Network Security, Database Systems, Programming (Python, C++), IT Operations

**Aspire College, Jhang** — ICS (Intermediate in Computer Science) · *2021 – 2023*

## 🌍 Quick Facts

| | |
|---|---|
| **Role** | Junior Cybersecurity Analyst / SOC Analyst (entry-level) |
| **Focus** | SOC Ops · Incident Investigation · VAPT · Cloud Security |
| **Open to** | SOC Analyst · Cybersecurity Analyst · Junior VAPT roles |
| **Location** | Lahore, Punjab, Pakistan |
| **Languages** | English · Urdu · Chinese (Beginner) |
| **Email** | [mahrukhsajj@gmail.com](mailto:mahrukhsajj@gmail.com) |
| **LinkedIn** | [linkedin.com/in/Ms.mahrukh](https://www.linkedin.com/in/Ms.mahrukh) |

## 📬 Let's Connect

<p align="center">
  <a href="mailto:mahrukhsajj@gmail.com"><img src="https://img.shields.io/badge/Email%20me-mahrukhsajj%40gmail.com-fb9500?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/Ms.mahrukh"><img src="https://img.shields.io/badge/Connect%20on%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
</p>

---

<p align="center"><i>⭐ If any of these labs are useful to you as a fellow student or junior analyst, a star is always appreciated.</i></p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:132f4c,100:0a1929&height=100&section=footer" width="100%" />
