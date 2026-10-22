"""
RECORD CHECK  -  my version
===========================

Name  : Muhammad Fateh Laghari
Lane  :  AI 
Date  :

Run it:   python template.py
"""

# =================================================================== FUNCTIONS
# 1. Write your functions here

def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"



def check(value, limit):
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent



def print_report(label, value, limit, difference, percent, status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Value:      {value}")
    print(f"Limit:      {limit}")
    print(f"Difference: {difference:>8.2f}")
    print(f"Percent:    {percent:>8.2f}%")
    print(f"Status:     {status}")
    print("=" * 34)


# ==================================================================== INPUT
# 2. Ask for your three values.

over_count = 0

while True:
    label = input("Enter a label (or quit): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter the value: "))
    limit = float(input("Enter the limit: "))


    # ================================================================== PROCESS
    # 3. Work out the difference, percentage, and status.

    difference, percent = check(value, limit)
    status = status_of(percent)


    # =================================================================== OUTPUT
    # 4. Print the report.

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_count += 1


print()
print("Total OVER LIMIT:", over_count)