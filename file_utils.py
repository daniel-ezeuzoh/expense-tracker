import csv
import os
from datetime import datetime

def write_report(filename, totals, valid, invalid):
    total_spent = sum(totals.values())
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Total spent: {total_spent:.2f}\n")
        file.write(f"Valid records: {valid}\n")
        file.write(f"Invalid records: {invalid}\n")
        file.write("\n")
        file.write("By category:\n")
        for category, amount in sorted(totals.items(), key=lambda item: item[1], reverse=True):
            file.write(f"  {category}: {amount:.2f}\n")

def log_run(filename, valid, invalid):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{stamp} - Run complete: {valid} valid, {invalid} invalid\n")

def export_records(filename, records):
    fieldnames = ["date", "description", "amount", "category"]
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

def rotate_log(filename, old_filename, max_lines=20):
    if not os.path.exists(filename):
        return
    with open(filename, "r", encoding="utf-8") as file:
        line_count = len(file.readlines())
    print(f"About to rename {filename} ({line_count} lines)")
    if line_count > max_lines:
        os.replace(filename, old_filename)
        print(f"Renamed {filename} to {old_filename}")