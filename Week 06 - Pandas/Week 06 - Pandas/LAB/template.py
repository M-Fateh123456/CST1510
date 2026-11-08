"""
RECORD CHECK  -  my version
===========================

Name  :  Muhammad Fateh Laghari
Lane  :  AI
Date  :  4 / 11 / 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd

# ==================================================================== LOAD
df = pd.read_csv("servers.csv")


# ================================================================= PROCESS
df["percent"] = (df["used"] / df["total"]) * 100

df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK"
)


# ================================================================== OUTPUT
print(df)

# Show only rows that are not OK
print(df[df["status"] != "OK"])
