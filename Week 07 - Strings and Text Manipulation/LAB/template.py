"""
RECORD CHECK  -  my version
===========================

Name  :  Muhammad Fateh Laghari
Lane  :  AI
Date  :  11 / 11 / 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.

def parse_line(raw_line):
    """Clean and parse one server record into a dictionary."""
    clean_line = raw_line.strip()
    hostname_part, rest = clean_line.split(",", 1)
    hostname = hostname_part.strip().lower()

    data = {"hostname": hostname}

    for piece in rest.split(","):
        key, value = piece.split("=", 1)
        data[key.strip().lower()] = float(value.strip())

    return data


def status_of(value, limit):
    """Return the server status based on its usage percentage."""
    percentage = value / limit * 100

    if percentage >= 100:
        return "OVER LIMIT"
    elif percentage >= 90:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing 
# and case. Match the shape to your lane:

raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=120,TOTAL=100",
    "  srv-03, used=50,total=100 ",
    "Srv-04 , USED=95 , TOTAL=100",
    "  SRV-05 , used=90 , total=100  "
]


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.

for raw_record in raw_records:
    data = parse_line(raw_record)
    print(data, status_of(data["used"], data["total"]))


# ==========================================================================
# 4. Before you finish:

try:
    parse_line("srv-06,used=unknown,total=100")
except ValueError as error:
    print("Error:", error)
