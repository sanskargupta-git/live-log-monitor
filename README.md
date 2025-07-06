# 🔴 Live Log Monitor – Real-Time Alerting for Suspicious Activity

This Python script watches a live web server log file (like Apache's `access.log`) and prints real-time alerts when suspicious patterns are detected:
- SQL Injection attempts
- XSS payloads
- Directory traversal

## ⚙️ Features

- Continuously tails a log file (like `tail -f`)
- Detects known attack patterns via regex
- Prints real-time alerts to console
- Beginner-friendly and useful in SOC/lab environments

## 🛠️ Usage

```bash
python live_log_monitor.py -f /var/log/apache2/access.log
