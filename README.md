# 🔐 NetRecon

> **Day 02 / 100 — Network Reconnaissance & Attack-Surface Mapper**

NetRecon is a Python-based **defensive network reconnaissance utility** for authorized security testing. It performs TCP connect scanning, basic service identification, optional banner collection, and structured JSON reporting from the command line.

## 🎯 Problem

During security assessments, defenders need a quick way to establish which TCP services are exposed on an authorized host. Manually checking ports is slow and makes it difficult to preserve consistent reconnaissance results.

## 💡 Solution

Authorized Target → Host Resolution → TCP Port Scan → Service Identification → Optional Banner Check → JSON Report

## ✨ Features

- TCP connect scanning
- Custom ports and ranges
- Concurrent scanning
- Basic service-name identification
- Optional banner collection
- Hostname/IP resolution
- Structured JSON reports
- Command-line interface
- Input validation and timeout handling
- Automated unit tests

## 🛠️ Tech Stack

- Python 3.10+
- Python standard library: socket, ipaddress, argparse, concurrent.futures
- Pytest for testing

**No machine learning, data science pipeline, or dashboard is used.**

## 🚀 Installation

    git clone https://github.com/devanshshukla-3004/NetRecon.git
    cd NetRecon
    python -m venv .venv

Windows PowerShell:

    .\\.venv\\Scripts\\Activate.ps1

Install dependencies:

    pip install -r requirements.txt

## ▶️ Usage

Scan common TCP ports:

    python main.py --target 192.168.1.10 --ports 1-1024

Scan selected ports:

    python main.py --target example.local --ports 22,80,443,8080

Disable banner collection:

    python main.py --target 192.168.1.10 --ports 1-1024 --no-banner

Save a report:

    python main.py --target 192.168.1.10 --ports 1-1024 --output reports/internal-host.json

## 🧪 Tests

    pytest -q

## 📄 Example Output

    NETRECON v1.0 | Network Reconnaissance Utility

    Target       : 192.168.1.10
    Resolved IP  : 192.168.1.10

    PORT     STATE     SERVICE       BANNER
    ------------------------------------------------------
    22       open      ssh           -
    80       open      http          -
    443      open      https        -

    Scanned ports: 1024 | Open ports: 3
    Report saved : reports/scan.json

## 🔒 Responsible Use

NetRecon is intended for **authorized security testing, laboratory environments, CTFs, and systems you own or have explicit permission to assess**. Do not scan third-party systems or networks without authorization.

The project performs connection-based reconnaissance only. It does not exploit discovered services, bypass authentication, or attempt to compromise systems.

## 📚 Learning Objectives

- Understand TCP-based reconnaissance
- Learn how ports and services expose an attack surface
- Practice Python socket programming
- Understand concurrency in security tooling
- Produce reproducible security assessment reports

## 🗺️ Roadmap

- [x] TCP port scanner
- [x] Concurrent scanning
- [x] Service identification
- [x] Banner collection
- [x] JSON reporting
- [x] Unit tests
- [ ] CIDR-aware host discovery module
- [ ] Rich terminal output
- [ ] Pluggable service probes

---

**Part of Devansh Shukla's 100 Days • 100 Cybersecurity Projects challenge.**
