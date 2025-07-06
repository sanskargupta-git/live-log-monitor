import time
import re
import argparse

suspicious_patterns = {
    "SQL Injection": r"('|%27|\b(UNION|SELECT|DROP|OR 1=1)\b)",
    "XSS": r"(<script>|%3Cscript%3E)",
    "Traversal": r"\.\./|\%2e\%2e"
}

def monitor_log(file_path):
    print(f"\n📡 Monitoring log file: {file_path} (Ctrl+C to stop)\n")
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        f.seek(0, 2)  # Jump to end of file

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue

            for attack_type, pattern in suspicious_patterns.items():
                if re.search(pattern, line, re.IGNORECASE):
                    print(f"[ALERT] {attack_type} Detected → {line.strip()[:120]}...")
                    break

def main():
    parser = argparse.ArgumentParser(description="🔴 Live Log Monitor & Real-Time Alerting")
    parser.add_argument("-f", "--file", required=True, help="Path to live server log (e.g. access.log)")
    args = parser.parse_args()

    try:
        monitor_log(args.file)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped.")

if __name__ == "__main__":
    main()
