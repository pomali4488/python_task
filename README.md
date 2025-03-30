Log Analyzer

Overview

The Log Analyzer script (log_analyzer.py) reads and processes log files, extracting key information such as timestamps, service names, log levels, and messages. It aggregates log statistics and provides insights into log levels, service activity, and common error messages. The output can be printed to the console, saved as a JSON file.

Features

Parses log files line by line.

Extracts structured data:

Timestamp (optional)

Service Name

Log Level (INFO, ERROR, WARN, DEBUG)

Message

Handles malformed log lines gracefully by logging warnings.

Aggregates statistics:

Count of log levels (e.g., how many ERROR messages).

Count of log entries per service.

Most common error message.

Outputs data in a readable JSON format.

Saves the summary to both JSON and CSV files.

Provides an optional function to filter logs by a specific date range.

Requirements

Python 3.x

Usage

Place your log file (app.log) in the same directory as log_analyzer.py.

Run the script:

python log_analyzer.py

The script will:

Print a summary of log statistics to the console.

Save the summary to log_summary.json.


Output

Console Output (Example):

{
    "Log Level Counts": {"INFO": 6, "ERROR": 3, "WARN": 2},
    "Service Counts": {"ServiceA": 4, "ServiceB": 3, "ServiceC": 2},
    "Most Common Error": {"message": "Null pointer exception", "count": 2}
}

Generated Files:

log_summary.json (Formatted JSON summary)



Error Handling

Malformed log lines are skipped with a warning message.

If the log file is missing, an error message is displayed.