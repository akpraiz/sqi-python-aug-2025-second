# with open("my_conditionals.py", "r", encoding="utf-8") as f:
#     contents = f.read()
# print(contents)

# with open("new file.txt", "w") as f:
#     f.write(""" This file was just created by me.
# Here we go, vamosss!!
# """)
    
# with open("new file.txt", "w") as f:
#     f.write("""I wanna overwrite the previous text.
# I don't need it anymore.
# """)

# import os

# home = os.path.expanduser("~")

# print(home)

# Assignment

# -------------------------- ----------------ASSIGNMENT-------------------------- ----------------


# -------------------- EXERCISE 1: File I/O & Context Managers --------------------
# Task: Save three lines of text (your name, today’s mood, and a random number) 
# into "status.txt". Then reopen it and print only the second line.

# Expected output example (your values will differ):
# Happy

# import random

# with open("status.txt", "w") as f:
#     f.write(f""" Akande Praise Toluwalase
# Just there
# {random.randint(1, 50)}
# """)
    
# with open("status.txt", "r", encoding="utf-8") as f:
#     contents = f.readlines()
# print(contents[1].strip())

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

# try:
#     with open("grades.csv", "r") as f:
#         contents = f.read()
#         print(contents)

# except FileNotFoundError:
#     with open("grades.csv", "w") as f:
#         f.write("student,score\n")
#     print("grades.csv created")



# -------------------------------------------------------------------------------


# -------------------- EXERCISE 3: Manual open/close -----------------------------
# Task: Open "story.txt" using the with context manager.
# Count how many words are inside.

# Expected input file (story.txt):
# "Once upon a time in Python land"

# Expected output:
# Word count: 6

# with open("story.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# word_count = len(text.split())

# print(f"Word count: {word_count}")

# -------------------------------------------------------------------------------


# -------------------- EXERCISE 4: Paths with os and pathlib ---------------------
# Task: Construct a path to a folder named "reports" in the user’s home directory.
# Print the path using both os.path and pathlib.

# Expected output example (depends on your system):
# Using os: C:\Users\dell\reports
# Using pathlib: C:\Users\dell\reports

# import os
# from pathlib import Path

# home_dir = os.path.expanduser("~")
# reports_path_os = os.path.join(home_dir, "reports")
# print("Using os:", reports_path_os)

# reports_path_pathlib = Path.home() / "reports"
# print("Using pathlib:", reports_path_pathlib)


# -------------------------------------------------------------------------------


# -------------------- EXERCISE 5: datetime.now() -------------------------------
# Task: Print the current time in 12-hour format with AM/PM (check online for how to do this).

# Expected output example:
# Current time: 02:48 PM

# import datetime

# current_time = datetime.datetime.now().strftime("%I:%M %p")
# print("Current time:", current_time)
# -------------------------------------------------------------------------------


# -------------------- EXERCISE 6: timedelta ------------------------------------
# Task: Calculate the date 90 days from today. 
# Print it in YYYY-mm-dd format.

# Expected output example (if today = 2025-09-22):
# 2025-12-21

# today = datetime.date.today()
# future_date = today + datetime.timedelta(days=90)
# print(future_date.strftime("%Y-%m-%d"))


# -------------------------------------------------------------------------------


# -------------------- EXERCISE 7: strftime Month/Day Names ---------------------
# Task: Print today’s date in style: Monday, September 22

# Expected output example:
# Monday, September 22

# todays_date = datetime.datetime.now().strftime("%A, %B:%d")
# print(todays_date)
# -------------------------------------------------------------------------------


# -------------------- EXERCISE 8: strptime -------------------------------------
# Task: A string "2024-07-04 18:30" represents a past event. 
# Parse it and print how many days ago it was.

# Expected output example (if today = 2025-09-22):
# That was 445 days ago.

# event_strg = "2024-07-04 18:30"

# event_date = datetime.datetime.strptime(event_strg, "%Y-%m-%d %H:%M")
# today = datetime.datetime.now()
# delta = today - event_date

# print(f"That was {delta.days} days ago.")


# -------------------------------------------------------------------------------


# -------------------- EXERCISE 9: math module ----------------------------------
# Task: Circle radius = 7.
# Use math.pi and math.pow to calculate and print the area.

# Formula: area = pi * r^2
# Expected output:
# Area: 153.93804002589985

# import math

# radius = 7
# area = math.pi * math.pow(radius, 2)

# print("Area:", area)

# -------------------------------------------------------------------------------
