"""
RECORD CHECK  -  my version
===========================

Name  : Muhammad Fateh Laghari
Lane  :  AI
Date  : 1 / 10 / 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT

over_limit_count=0
while True:
    label = input("Enter label (or quit): ")

    if label == "quit":
        break

    value =float(input("Enter value: "))
    limit =float(input("Enter limit: "))


    # ================================================================== PROCESS
    difference = value - limit
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"


    # =================================================================== OUTPUT

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Value:      {value}")
    print(f"Limit:      {limit}")
    print(f"Difference: {difference:.2f}")
    print(f"Percent:    {percent:.2f}%")
    print(f"Status:     {status}")

    print("=" *34)

# ==========================================================================

print(f"OVER LIMIT records:{over_limit_count}")