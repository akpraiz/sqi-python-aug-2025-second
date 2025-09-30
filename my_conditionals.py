# is_raining = False

# if is_raining:
#   print("Carry an umbrella")
# else:
#   print("No need for an umbrella")

# num1 = 2
# num2 = 2

# if num1 > num2:
#   print("num1 is greater")
# else:
#   print("num2 is greater or equal to num1")

# number = input("Enter a number: ")
# is_even = number % 2 == 0
# if is_even

# Ask the user to enter a word
# print: "It starts with a" if the word starts with a
# otherwise print "It does not start with a"

# letter = input("Enter a word: ").lower()
# a_starts = letter.lower()
# if a_starts[0] == "a":
#   print("It starts with a")
# else:
#   print("It does not start with a")

# Ask the user for a sentence
# if all the characters are lowercase, print "Everything is in lowercase"
# otherwise, print "Not everything is in lowercase"

# sentence = input("Enter a sentence: ")
# if sentence.islower():
#   print("Everything is in lowercase")
# else:
#   print("Not everything is in lowercase")

# Ask the user for their score and tell them their grade
# If their score is less than 30 and greater than 0, print "F"
# If there score is equal to or greater than 30 and less than or equal to 59, print "C"
# if their score is 60 or greater than than 60 and less than or equal to 100, print "A"

# score = int(input("Enter your score: "))


# if 0 < score < 30:
#     print("F")
# elif 30 <= score <= 59:
#     print("C")
# elif 60 <= score <= 100:
#     print("A")
# else:
#     print("Invalid score")

# has_umbrella = False
# has_raincoat = False

# if has_umbrella and has_raincoat:
#     print("You have double protection from the rain")
# elif has_umbrella or has_raincoat:
#     print("You have protection from the rain")
# else:
#     print("You are NOT procteded from the rain")

# mode = input("Enter the mode: ").strip().lower()

# if mode == "manual":
#   print("Manual mode activated")
# elif mode == "automatic":
#     print("Automatic mode activated")
# elif mode == "off":
#     print("System is off")
# else:
#    print("Invalid mode")

# 1. Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# if a > 0 and b > 0:
#     print("a and b are both positive")
# elif (a > 0 and b <= 0) or (a <= 0 and b > 0) :
#     print("Only one is positive")
# else:
#     print("Neither is positive")

# 2. Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" 
# if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.

# x, y, z = input("Enter three numbers separated by a comma: ").split(",")
# x = int(x)
# y = int(y)
# z = int(z)
# print(x)
# print(y)
# print(z)

# if x < y < z:
#     print("Increasing order")
# elif x > y > z:
#     print("Decreasing order")
# else:
#     print("Neither")

# 3. Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. 
# Print "Is a palindrome" if it is, otherwise print "Not a palindrome".

# palindrome = input("Enter a palindrome: ").strip().lower()
# reversed_palindrome = palindrome[::-1]

# if palindrome == reversed_palindrome:
#     print("Is palindrome")
# else:
#     print("Not a palindrome")

# 4. You have three variables: x, y, and z collected as 3 separate inputs from the user. 
# Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. 
# Otherwise, print "All different" or "All same" accordingly.
# x = input("Just enter anything: ").strip()
# y = input("Just enter anything: ").strip()
# z = input("Just enter anything: ").strip()

# if x == y and x==z and y==z:
#     print("Two are equal")


# 5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, 
# use if statements to check if they can form a valid triangle. 
# Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".

# angle1 = int(input("Enter an angle: "))
# angle2 = int(input("Enter an angle: "))
# angle3 = int(input("Enter an angle: "))
# sum = angle1 + angle2 + angle3

# if sum == 180:
#     print("Valid triangle")
# else:
#     print("Invalid triangle")

# 6. You have a single character variable `ch` supplied through user input. 
# Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. 
# Assume that the input is a single alphabet character.


# ch = input("Enter a vowel: ").strip().lower()

# if ch == "a":
#     print("Vowel")
# elif ch == "e":
#     print("Vowel")
# elif ch == "i":
#     print("Vowel")
# elif ch == "o":
#     print("Vowel")
# elif ch == "u":
#     print("Vowel")
# else:
#     print("Consonant")


# 7. Given a comma separated string input from the user of three colors color1, color2, and color3, 
# write an if statement to check if all three colors are primary colors (red, blue, yellow). 
# Print "All primary colors" if they are, otherwise print "Not all primary colors".

# color1, color2, color3 = input("Enter three colors separated with comma: ").lower().split(", ")
# print(color1)
# print(color2)
# print(color3)
# primary_colors = {"red", "blue", "yellow"}
# if {color1, color2, color3}.issubset(primary_colors) :
#     print("All primary colors")
# else:
#     print("Not all primary colors")

# 8. You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". 
# Write an if statement that prints "Manual mode activated" if mode is "manual", 
# "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".

# mode = input("Enter the mode: ").strip().lower()

# if mode == "manual":
#   print("Manual mode activated")
# elif mode == "automatic":
#     print("Automatic mode activated")
# elif mode == "off":
#     print("System is off")
# else:
#    print("Invalid mode")

# 9. Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", 
# "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".

# message = input("Enter a message: ").strip().lower()

# if "urgent" in message:
#     print("High priority message")
# elif "important" in message:
#     print("High priority message")
# elif "immediate" in message:
#     print("High priority message")
# else:
#     print("Normal message")

# 10.	You have two variables, status1 and status2, provided through user input, each of 
# 	which can be "active", “inactive", or "pending". Write an if statement to print 
# 	"Both active" if both statuses are "active", "One active" if exactly one is "active",
# 	and "None active" if neither is "active".

# status1 = input("Enter your status: ").strip().lower()
# status2 = input("Enter your status: ").strip().lower()

# if status1 == "active" and status2 == "active":
#     print("Both active")
# elif (status1 == "pending" and status2 == "active") or (status1 == "active" and status2 == "pending"):
#     print("One active")
# else:
#     print("None active")


#  11. 	Given a string `filename` supplied by the user, write an if statement to check if the
# 	filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# 	print "Not an image file".
# filename = input("Enter a file name: ").strip()
# filename_end = filename[-4:]
# # print(filename_end)
# if filename_end == ".jpg":
#     print("Image file")
# elif filename_end == ".png":
#     print("Image file")
# elif filename_end == ".gif":
#     print("Image file")
# else:
#     print("Not an image file")

#  12. 	You have a variable `access_level` provided through user input which can be "admin",
# 	"user", or "guest". Write an if statement that prints "Full access" if access_level is
# 	"admin", "Limited access" if it is "user", and "No access" if it is "guest".

# access_level = input("Enter whether you're an admin, a user, or guest: ").strip()

# if access_level == "admin":
#     print("Full access")
# elif access_level == "user":
#     print("Limited access")
# elif access_level == "guest":
#     print("No access")
# else:
#     print("Invalid")

#  13. 	Given a string `email` collected from the user, write an if statement to check if the
# 	email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
# 	print "Invalid email".

# email = input("Enter your email: ").strip().lower()

# if "@" in email:
#   print("Valid email")
# elif "."in email:
#   print("Valid email")
# else:
#   print("Invalid email")

#  14. 	You have a variable `day` provided by user input which can be any day of the week 
# 	(e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# 	day is "Saturday" or "Sunday", and "Weekday" if it is any other day.

# day = input("Enter a day of the week: ").strip().lower()


# day = input("Enter a day of the week: ").strip().lower()

# if day == "Monday":
#     print("Weekday")
# elif day == "Tuesday":
#     print("Weekday")
# elif day == "Wednesday":
#     print("Weekday")
# elif day == "Thursday":
#     print("Weekday")
# elif day == "Friday":
#     print("Weekday")
# elif day == "Saturday":
#     print("Weekend")
# elif day == "Sunday":
#     print("Weekend")
# else:
#     print("Invalid")

#  15. 	Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# 	input from the user and prints the greatest number. Use conditional statements
# 	to determine which number is the greatest. Bonus point if you can do it without `else` 
# 	statements.

# num1, num2, num3 = input("Enter three numbers separated by comma: ").split(", ")
# print(num1)
# print(num2)
# print(num3)



# -------------------------------ASSIGNMENT 27th August, 2025-------------------------------
# Exercise 1
# An amusement park ride has these rules:
# - Must be at least 120 cm tall to ride.
# - If under 120 cm but with an adult, still allowed.
# - Otherwise, not allowed.

# rule1 = int(input("Enter your height: "))
# rule2 = input("Enter yes if you're with an adult and no if not with an adult: ").strip().lower()

# if (rule1 >= 120) and (rule2 == "yes" or rule2 == "no"):
#     print("Allowed")
# elif (rule1 < 120) and (rule2 == "yes"):
#     print("Allowed")
# else:
#     print("Not allowed")

#
# Example input/output executions:
#
# Enter height: 130
# With adult? no
# Output: Allowed
#
# Enter height: 110
# With adult? yes
# Output: Allowed
#
# Enter height: 110
# With adult? no
# Output: Not allowed
#
# Enter height: 119
# With adult? yes
# Output: Allowed
#
# Enter height: 100
# With adult? no
# Output: Not allowed
#
# Enter height: 150
# With adult? no
# Output: Allowed



# Exercise 2
# An exam grading system with retake rule:
# The user enters exam score and retake status ("yes" or "no").
# - If score is at least 50, print "Pass".
# - If score is less than 50 but retake is "yes", print "Retake allowed".
# - If score is less than 50 and no retake, print "Fail".

# score = int(input("Enter your score: "))
# retake = input("State if you would retake the exam or not (A 'Yes' or 'No' answer only): ").lower().strip()

# if (score >= 50) and (retake == "yes" or retake == "no"):
#     print("Pass")
# elif (score < 50) and (retake == "yes"):
#     print("Retake allowed") 
# elif (score < 50) and (retake == "no"):
#     print("Fail")
# else:
#     print("Invalid")


# Example input/output executions:
#
# Enter score: 42
# Retake? yes
# Output: Retake allowed
#
# Enter score: 42
# Retake? no
# Output: Fail
#
# Enter score: 50
# Retake? no
# Output: Pass
#
# Enter score: 75
# Retake? yes
# Output: Pass
#
# Enter score: 10
# Retake? no
# Output: Fail



# Exercise 3
# A ride-hailing app calculates trip approval:
# The user enters distance (km) and wallet balance.
# Each km costs 200 units.
# - If wallet balance is enough for the trip, print "Trip confirmed".
# - If balance is less but at least half the cost, print "Add funds".
# - If less than half, print "Trip denied".

# distance = float(input("Enter the distance of the trip: "))
# wallet_balance = float(input("Enter the units in your wallet: "))
# trip_cost = 200 * distance

# if wallet_balance >= trip_cost:
#     print("Trip confirmed")
# elif wallet_balance >= (0.5 * trip_cost):
#     print("Add funds")
# elif wallet_balance < (trip_cost):
#     print("Trip denied")
# else:
#     print("Invalid")

#
# Example input/output executions:
#
# Enter distance: 10
# Enter wallet balance: 800
# Output: Trip denied
# Reasoning: cost = 10 * 200 = 2000; half = 1000; balance = 800.
# 800 < 1000 (less than half), so "Trip denied".
#
# Enter distance: 10
# Enter wallet balance: 2000
# Output: Trip confirmed
# Reasoning: cost = 2000; balance = 2000.
# balance >= cost, so "Trip confirmed".
#
# Enter distance: 10
# Enter wallet balance: 1000
# Output: Add funds
# Reasoning: cost = 2000; half = 1000; balance = 1000.
# not enough (1000 < 2000) but balance >= half, so "Add funds".
#
# Enter distance: 10
# Enter wallet balance: 400
# Output: Trip denied
# Reasoning: cost = 2000; half = 1000; balance = 400.
# balance < half, so "Trip denied".
#
# Enter distance: 5
# Enter wallet balance: 500
# Output: Add funds
# Reasoning: cost = 5 * 200 = 1000; half = 500; balance = 500.
# not enough (500 < 1000) but exactly half, so "Add funds".



# Exercise 4
# An airport boarding system:
# The user enters boarding pass ("yes"/"no") and passport ("yes"/"no").
# - If both are "yes", print "Proceed to boarding".
# - If boarding pass is missing, print "No boarding pass".
# - If passport is missing, print "No passport".
# - If both missing, print "Denied entry".
# #
# boarding_pass = input("Enter 'yes' or 'no' if you have a boarding pass: ").strip().lower()
# passport = input("Enter 'yes' or 'no' if you have a passport: ").strip().lower()

# if (boarding_pass == "yes") and (passport == "yes"):
#     print("Proceed to boarding")
# elif (boarding_pass == "no") and (passport == "yes"):
#     print("No boarding pass")
# elif (boarding_pass == "yes") and (passport == "no"):
#     print("No passport")
# else:
#     print("Denied entry")

# Example input/output executions:
#
# Boarding pass? no
# Passport? yes
# Output: No boarding pass
#
# Boarding pass? yes
# Passport? no
# Output: No passport
#
# Boarding pass? no
# Passport? no
# Output: Denied entry
#
# Boarding pass? yes
# Passport? yes
# Output: Proceed to boarding
#
# Boarding pass? no
# Passport? yes
# Output: No boarding pass


# -------------------------------ASSIGNMENT 27th August, 2025-------------------------------