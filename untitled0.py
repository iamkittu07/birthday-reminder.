# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1741r2FBx5twHky5C8Wb5-0GXEb47g4xj
"""

from datetime import datetime

# Step 1: Dictionary to store names and birthdays in MM-DD format
birthdays = {
    "Tithi": "07-17",
    "Aman": "08-23",
    "Neha": "01-01",
    "Ravi": "07-18",
    "Sneha": "12-25"
}

# Step 2: Get today's date
today = datetime.now().strftime("%m-%d")

# Step 3: Check if today matches any birthday
birthday_found = False
for name, bday in birthdays.items():
    if bday == today:
        print(f"🎉 Today is {name}'s Birthday!")
        birthday_found = True

if not birthday_found:
    print("No birthdays today.")