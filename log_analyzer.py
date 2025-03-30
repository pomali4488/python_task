"""
This script checking the log file app.log and
creating json file(log_summary.json) with all details
"""

import re
import json
from collections import Counter
from datetime import datetime

LOG_FILE_PATH = "app.log"
OUTPUT_JSON = "log_summary.json"

# Define the regex pattern to match log entries (timestamp is optional)
LOG_PATTERN = re.compile(
    r"(?:([\d]{4}-[\d]{2}-[\d]{2})\s+([\d]{2}:[\d]{2}:[\d]{2})\s+-\s+)?"  # Optional timestamp
    r"([\w?-]+)\s+-\s+"  # Service name (handles ??? as well)
    r"(INFO|ERROR|WARN|DEBUG)\s+-\s+"  # Log level
    r"(.+)"  # Log message
)


def parse_log_file(file_path):
    """Reads and parses the log file, extracting structured log details."""
    try:
        log_data = []
        log_level_count = Counter()
        service_count = Counter()
        error_messages = Counter()

        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                match = LOG_PATTERN.match(line)

                if match:
                    date, time, service, level, message = match.groups()
                    timestamp = f"{date} {time}" if date and time else "N/A"

                    # Store log entry
                    log_data.append({
                        "timestamp": timestamp,
                        "service": service,
                        "level": level,
                        "message": message
                    })

                    # Update counters
                    log_level_count[level] += 1
                    service_count[service] += 1

                    if level == "ERROR":
                        error_messages[message] += 1
                else:
                    print(f"WARNING: Skipping malformed log line: {line}")
    except Exception as excp:
        print("Exception Occured")
        print(excp)

    return log_data, log_level_count, service_count, error_messages

def generate_summary(log_level_count, service_count, error_messages):
    """Generates a summary of log statistics."""
    most_common_error = max(error_messages.items(), key=lambda x: x[1], default=("N/A", 0))
    return {
        "Log Level Counts": dict(log_level_count),
        "Service Counts": dict(service_count),
        "Most Common Error": {"message": most_common_error[0], "count": most_common_error[1]},
    }


def save_summary_json(summary, output_path):
    """Saves the summary to a JSON file."""
    with open(output_path, "w") as json_file:
        json.dump(summary, json_file, indent=4)


def filter_logs_by_date(log_data, start_date, end_date):
    """Filters logs between a given date range."""
    filtered_logs = []
    for entry in log_data:
        if entry["timestamp"] == "N/A":
            continue

        log_date = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S")
        if start_date <= log_date <= end_date:
            filtered_logs.append(entry)
    return filtered_logs


def main():
    """Main execution function."""
    log_data, log_level_count, service_count, error_messages = parse_log_file(LOG_FILE_PATH)
    summary = generate_summary(log_level_count, service_count, error_messages)

    print(json.dumps(summary, indent=4))
    save_summary_json(summary, OUTPUT_JSON)


if __name__ == "__main__":
    main()
