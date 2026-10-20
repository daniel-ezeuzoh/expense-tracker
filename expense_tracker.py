import csv
from datetime import datetime
from file_utils import write_report, log_run, export_records, rotate_log

def read_expenses(filename):
    expenses = []
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        print(f"{filename} not found")
    except PermissionError:
        print(f"{filename} could not be accessed")
    return expenses

def clean_expenses(expenses):
    cleaned = []
    for exp in expenses:
        new_expense = exp.copy()
        new_expense["description"] = new_expense["description"].strip()
        new_expense["amount"] = new_expense["amount"].strip()
        new_expense["category"] = new_expense["category"].strip().lower()

        try:
            new_expense["date"] = datetime.strptime(new_expense["date"].strip(), "%Y-%m-%d")
        except ValueError:
            cleaned.append("Invalid date")
            continue
        
        cleaned.append(new_expense)
    return cleaned

def validate_expense(expense):
    try:
        expense["amount"] = float(expense["amount"])
    except ValueError:
        return "Invalid amount"
    
    if expense["amount"] <= 0:
        return "Invalid amount"
    allowed = ["food", "transport", "data", "other"]
    if expense["category"] not in allowed:
        expense["category"] = "uncategorized"
    return expense

def process_expenses(cleaned):
    results = []
    for exp in cleaned:
        if isinstance(exp, str):
            results.append(exp)
            continue
        outcome = validate_expense(exp)
        results.append(outcome)
    return results

def summarize(results):
    totals = {}
    valid = 0
    invalid = 0
    for record in results:
        if isinstance(record, str):
            invalid += 1
            continue
        valid += 1
        category = record["category"]
        amount = record["amount"]
        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount
    return totals, valid, invalid

if __name__ == "__main__":
    raw = read_expenses("expenses.csv")
    cleaned = clean_expenses(raw)
    results = process_expenses(cleaned)
    totals, valid, invalid = summarize(results)
    valid_records = []
    for r in results:
        if isinstance(r, str):
            continue
        r_copy = r.copy()
        r_copy["date"] = r_copy["date"].strftime("%Y-%m-%d")
        valid_records.append(r_copy)

    write_report("report.txt", totals, valid, invalid)
    print("Report written to report.txt")

    rotate_log("log.txt", "log_old.txt", 5)

    log_run("log.txt", valid, invalid)
    print("Log updated in log.txt")

    export_records("categorized.csv", valid_records)
    print("Categorized records exported to categorized.csv")

#What does it take? (parameters)
#What does it return? (or does it return nothing?)
#What does it do? (in plain English, one or two sentences)
#For rotate_log, specifically answer: when does the rename actually happen, and when does it not happen?
#And finally — explain the driver block at the bottom of the file. In plain English, in the order the script actually runs:
#Tell me what happens at each step. Not the code — the effect. "First, it reads the CSV. Then, it..." and so on.