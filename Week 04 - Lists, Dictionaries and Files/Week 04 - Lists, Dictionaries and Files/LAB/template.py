"""
RECORD CHECK  -  my version
===========================

Name  : Muhammad Fateh Laghari
Lane  :  AI
Date  : 14/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here



# =================================================================== FUNCTIONS
def check_record(value, limit):
    """Calculate the difference, percentage and status."""
    difference = value - limit
    percent = value / limit * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status




def print_report(label, value, limit, difference, percent, status):
    """Print the report for one record."""
    print(f"\nRecord: {label}")
    print(f"Value      : {value:.2f}")
    print(f"Limit      : {limit:.2f}")
    print(f"Difference : {difference:.2f}")
    print(f"Percent    : {percent:.2f}%")
    print(f"Status     : {status}")


# ====================================================================== STORE

records = [
    {"label": "R-001", "value": 87.0, "limit": 100.0},
    {"label": "R-002", "value": 120.0, "limit": 100.0},
    {"label": "R-003", "value": 45.0, "limit": 100.0}
]



def load_records(path):
    """Load records from a file into a list of dictionaries."""
    records = []

    try:
        with open(path, "r") as file:
            for line in file:
                label, value, limit = line.strip().split(",")

                record = {
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                }

                records.append(record)

    except FileNotFoundError:
        print("File not found:", path)
        return []

    return records


# To use the file instead of the records above, uncomment this line:
# records = load_records("records_sample.txt")


# =============================================================== PROCESS + OUTPUT

for record in records:
    difference, percent, status = check_record(
        record["value"], record["limit"]
    )

    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )