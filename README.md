# Expense Tracker (Python ETL Pipeline)

A command-line Python application that ingests raw expense data, validates it, and generates analytical reports.

## What This Project Does
This project is a small-scale ETL (Extract, Transform, Load) pipeline:
1. **Extracts** raw expense data from a CSV file.
2. **Transforms** the data by cleaning strings, parsing dates, validating amounts, and categorizing expenses.
3. **Loads** the results by generating three output files:
   - A formatted text report (`report.txt`).
   - A timestamped audit log (`log.txt`), including automated log rotation.
   - A cleaned CSV export (`categorized.csv`).

## Features & Skills Demonstrated
- **File I/O & CSV Processing:** Uses `csv.DictReader` and `csv.DictWriter` to safely read and write CSVs.
- **Defensive Programming:** Implements specific `try/except` blocks to handle missing files, permission errors, and invalid data without crashing.
- **Data Validation:** Checks for invalid dates, negative amounts, non-numeric values, and unauthorized categories.
- **Date Handling:** Uses `datetime.strptime` to parse strings into date objects for accurate filtering and `strftime` for clean exporting.
- **Modular Design:** Separates reusable file utilities into a standalone module (`file_utils.py`).
- **Logging:** Appends timestamped run summaries to a persistent log file and handles log rotation.

## How to Run
1. Ensure Python 3 is installed.
2. Clone this repository or download the files.
3. Run the main script:
   ```bash
   python expense_tracker.py
