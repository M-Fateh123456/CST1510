"""
RECORD CHECK  -  my version
===========================

Name  : Muhammad Fateh Laghari
Lane  :  AI
Date  : 22 / 10 / 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return ('OVER LIMIT')
        elif percent >= 90:
            return ('WARNING')
        else:
            return ('OK')


# ==================================================================== RECORDS
# 2. Create your records.

records = [Record("R-001", 87.0, 100.0), Record("R-002", 120.0, 100.0)]


# ==================================================================== OUTPUT
# 3. Print a report for each record.
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  Value      : {record.value:.2f}")
    print(f"  Limit      : {record.limit:.2f}")
    print(f"  Status     : {record.status()}")

    print("=" * 34)