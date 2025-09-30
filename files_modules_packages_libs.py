# with open("for_loops.py", "r", encoding="utf-8") as f:
#     contents = f.read()

# print(contents)

# “fiction"
# with - context manager
# with open("manual.txt", "r", encoding="utf-8") as f:
#     contents = f.read()

# print(contents)


# with open("new file.txt", "w") as f:
#     f.write("""This file was created with Python
# We used the open function
# and the with context manager.
# We do not have to close the file ourselves.            
# """)
# with open("new file.txt", "w") as f:
#     f.write("""We just added this line
# We used the append mode.            
# """)

# try:
#     with open("new_file.txt", "r", encoding="utf-8") as f:
#         contents = f.read()
# except FileNotFoundError:
#     contents = ""

# print(f"Contents: {contents}")


# f = None

# try:
#     f = open("new_file.txt", "r", encoding="utf-8")
#     contents = f.read()
# except FileNotFoundError:
#     contents = ""
# else:
#     print(f"Contents: {contents}")
# finally:
#     if f is not None:
#         f.close()

# file_path = "C:\Users\dell\Downloads\transaction_flow_full.md"

# print(file_path)

# import os

# home = os.path.expanduser("~")

# print(home)

# file_path = os.path.join(home, "Downloads", "transaction_flow_full.md")
# print(file_path)


# with open(file_path, "r") as f:
#     print(f.read())


# from pathlib import Path
# home = Path.home()
# print(home)
# file_path = Path(home) / "Downloads" / "transaction_flow_full.md"
# print(file_path)


# with open(file_path, "r") as f:
#     print(f.read())




# -------------------------- ----------------DATETIME-------------------------- ----------------

import datetime

# now = datetime.datetime.now()

# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)


# last_week_thursday = datetime.datetime(2025, 9, 18, 21, 15)

# print(last_week_thursday)

# four_days = datetime.timedelta(days=4)

# print(four_days)

# last_week_thursday = now - four_days

# print(last_week_thursday)


# def is_coupon_expired(coupon_activation_date: datetime.datetime, active_period: datetime.timedelta):
#     now = datetime.datetime.now()
#     expiry_date = coupon_activation_date + active_period
#     return expiry_date < now



# coupon_activation_date = datetime.datetime(2025, 9, 17)
# # active_period = datetime.timedelta(7)
# active_period = datetime.timedelta(3)
# print(is_coupon_expired(coupon_activation_date, active_period))


# now = datetime.datetime.now()

# # formatted_date = now.strftime("%d/%m/%Y, %H:%M:%S")
# # formatted_date = now.strftime("%Y/%m/%d, %H:%M")
# formatted_date = now.strftime("%Y-%h-%d, %H:%M")
# formatted_date = now.strftime("%d %B, %Y")

# print(formatted_date)

# now = datetime.datetime.now()

# name = input("What is your name? ").strip()

# birth_date = input("When were you born? E.g: 22, August: ").strip()
# day, month = birth_date.split(",")
# day, month = day.strip(), month.strip()

# birth_date = datetime.datetime.strptime(f"{now.year}-{month}-{day}", "%Y-%B-%d")


# if now.date() < birth_date.date():
#     days_remaining = birth_date - now
#     print(f"It is not yet your birthday. It is remaining {days_remaining.days} days")
# elif now.date() == birth_date.date():
#     print(f"Happy birthday, {name} 🥳")
# else:
#     print("Your birthday has already passed!")
# -------------------------- ----------------DATETIME-------------------------- ----------------


# -------------------------- ----------------MATH-------------------------- ----------------

# import math

# print(math.sqrt(8))
# print(math.cbrt(8))

# angle = math.radians(90)

# print(math.sin(angle))

# print(math.pi)

# print(math.log(100, 10))
# print(math.log10(100))

# -------------------------- ----------------MATH-------------------------- ----------------


# -------------------- EXERCISE 1: File I/O & Context Managers --------------------
# Task: Save three lines of text (your name, today’s mood, and a random number) 
# into "status.txt". Then reopen it and print only the second line.

# Expected output example (your values will differ):
# Happy

# -------------------------------------------------------------------------------


# -------------------- EXERCISE 2: Exception Handling ----------------------------
# Task: Try to open "grades.csv" for reading.
# If missing, create it with one line: "student,score"
# Print "grades.csv created" if file had to be created.

# Expected output if file missing:
# grades.csv created
#
# Expected output if file exists (contents vary):
# (prints the file contents)

# -------------------------------------------------------------------------------


# -------------------- EXERCISE 3: Manual open/close -----------------------------
# Task: Open "story.txt" using the with context manager.
# Count how many words are inside.

# Expected input file (story.txt):
# "Once upon a time in Python land"

# Expected output:
# Word count: 6

# -------------------------------------------------------------------------------


# -------------------- EXERCISE 4: Paths with os and pathlib ---------------------
# Task: Construct a path to a folder named "reports" in the user’s home directory.
# Print the path using both os.path and pathlib.

# Expected output example (depends on your system):
# Using os: C:\Users\dell\reports
# Using pathlib: C:\Users\dell\reports

# -------------------------------------------------------------------------------


# -------------------- EXERCISE 5: datetime.now() -------------------------------
# Task: Print the current time in 12-hour format with AM/PM (check online for how to do this).

# Expected output example:
# Current time: 02:48 PM

# -------------------------------------------------------------------------------


# -------------------- EXERCISE 6: timedelta ------------------------------------
# Task: Calculate the date 90 days from today. 
# Print it in YYYY-mm-dd format.

# Expected output example (if today = 2025-09-22):
# 2025-12-21

# -------------------------------------------------------------------------------


# -------------------- EXERCISE 7: strftime Month/Day Names ---------------------
# Task: Print today’s date in style: Monday, September 22

# Expected output example:
# Monday, September 22

# -------------------------------------------------------------------------------


# -------------------- EXERCISE 8: strptime -------------------------------------
# Task: A string "2024-07-04 18:30" represents a past event. 
# Parse it and print how many days ago it was.

# Expected output example (if today = 2025-09-22):
# That was 445 days ago.

# -------------------------------------------------------------------------------


# -------------------- EXERCISE 9: math module ----------------------------------
# Task: Circle radius = 7.
# Use math.pi and math.pow to calculate and print the area.

# Formula: area = pi * r^2
# Expected output:
# Area: 153.93804002589985

# -------------------------------------------------------------------------------
