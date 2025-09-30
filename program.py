# print("This is Day 2 of our Python class.")

# first_name = "Praise"
# last_name = "Akande"
# course = "Python"

# print("First Name:", first_name)
# print("Last Name:", last_name)
# print("Course:", course)


# x = 4
# y = 8
# z = 19

# print("x + y + z =", x + y + z)
# print('The man said, "The quick brown fox jumps"')


# # An Integer
# my_phones = 2
# print(my_phones)

# # A String
# my_name = "Praise"
# print(my_name)

# # A Float
# my_weight = 65.2
# print(my_weight)
# # A Boolean
# god_is_not_dead = True
# print(god_is_not_dead)

# # A None
# clean_politicians_in_nigeria = None
# print(clean_politicians_in_nigeria)

# # A constant
# acceleration_due_to_gravity = 9.78
# print(acceleration_due_to_gravity)

# story = """Dynamic and results-driven business plan developer and financial forecaster with expertise in crafting tailored business strategies and precise financial models. 
# Adept at translating complex data into actionable insights to drive growth and profitability. 
# Skilled in Microsoft Office and financial analysis, with a passion for helping businesses secure funding and achieve sustainable success.
# Renowned for innovative thinking, attention to detail, and an unwavering commitment to delivering impactful solutions."""
# print(story)

# story = '''Dynamic and results-driven business plan developer and financial forecaster with expertise in crafting tailored business strategies and precise financial models. 
# Adept at translating complex data into actionable insights to drive growth and profitability. 
# Skilled in Microsoft Office and financial analysis, with a passion for helping businesses secure funding and achieve sustainable success.
# Renowned for innovative thinking, attention to detail, and an unwavering commitment to delivering impactful solutions.'''
# print(story)

# new_story = story = "Dynamic and results-driven business plan developer and financial forecaster with expertise in crafting tailored business strategies and precise financial models. \nAdept at translating complex data into actionable insights to drive growth and profitability.\nSkilled in Microsoft Office and financial analysis, with a passion for helping businesses secure funding and achieve sustainable success./nRenowned for innovative thinking, attention to detail, and an unwavering commitment to delivering impactful solutions."
# print(new_story)


# Indexing
# sentence = "Today is Monday! Today's date is 8/11/2025"
# print(sentence[6])
# print(sentence[-2])

# print(len("name"))

# Create a variable called greeting and assign the value "I am happy" to it
# Print the first character using positive indexing
# Print the last character using positive indexing
# Print the last character using negative indexing

# greeting = "I am happy"

# print(greeting[0])
# print(greeting[9])
# print(greeting[-1])

# Imutability of strings

# name = "Winnie"

# name = "Deborah"

#Strings are imutabale. List are mutable.

# Create a varable called story and assign the value "Once upon a time. there lived a king" to it.
# Use slicing to extract and print "Once upon a time"
# Use slicing to extract "there lived a king"
# Extract "Once upon a time", but skip a single character each time i.e. Oc pnatm
# Use slicing to print "king", do not specify the end
# Use slicing to print "Once upon", do not spepcify the end
# Use slicing to print "lived a", using negative slicing.

# story = "Once upon a time, there lived a king"
# print(story[0:16])
# print(story[18:36])
# print(story[0:16:2])
# print(story[-4:])
# print(story[:9])
# print(story[-12:-4])

# 1. Create a multi-line string variable using triple quotes.
# my_story = """My name is Praise
# I am data analyst
# I love working on my system
# """
# 2. Create a string variable word with the value "Python". Print the first and last characters using indexing.
# word = "Python"
# print(word[0])
# print(word[5])
# 3. Attempt to modify the character at index 2 in the string "Python" from question 9. Print the resulting error message.
# word[2] = "A"
# print(word[2])
# 4. Given the string course_name = "Introduction to Python", use slicing to print:
# 	The word "Introduction".
# The word "Python".
# course_name = "Introduction to Python"
# print(course_name[0:12])
# print(course_name[-6:])
# 5. Given the string name = "Alexander", use slicing to:
# Print the first three characters concatenated with the last three characters.
# name = "Alexander"
# result = name[:3] + name[-3:]
# print(result)

# Create two variables:
# 1. Location = "SQI"
# 2. Greeting = "Good morning,"

# Form the string "Good morning, SQI" using concatenation

# location = "SQI"
# greeting = "Good morning,"

# location_greeting = greeting + " " + location
# print(location_greeting)

# favorite_food = "yam and egg"
# favorite_num = 34
# slept_early = False
# distance = 34.7
# It is False that I slept early last night. My favorite food is yam and egg.
# The distance from my school to my house is 34.7km.
# Also, my favorite number is 34.

# sentence = "It is " + str(slept_early) + " that I slept early last night. " + " My favorite food is " + favorite_food + "\nThe distance from my school to my house is " + str(distance) + "km" + "\nAlso, my favorite number is " + str(favorite_num) + "."
# print(sentence)

# sentence = "It is {} that I slept early last night. My favorite food is {}. \nThe distance from my school to my house is {}km. \nAlso, my favorite number is {}.".format(slept_early, favorite_food, distance, favorite_num)
# print(sentence)

# sentence = """It is {} that I slept early last night. My favorite food is {}. 
# The distance from my school to my house is {}km. 
# Also, my favorite number is {}.""".format(slept_early, favorite_food, distance, favorite_num)
# print(sentence)

# sentence = f"""It is {slept_early} that I slept early last night. My favorite food is {favorite_food}. 
# The distance from my school to my house is {distance}km. 
# Also, my favorite number is {favorite_num}."""
# print(sentence)

# age = 12
# # I am 12 years old.
# print("I am " + str(age) + " years old.")
# print("I am {} years old.".format(age))
# print(f"I am {age} years old.")

# 1. Create two string variables: first_name with value "John" and last_name with value 
# "Smith". Concatenate them together with a space in between and print the result.
# first_name = "John"
# last_name = "Smith"
# first_and_last_name = first_name + " " + last_name
# print(first_and_last_name) 

# 2. Given the string word = "Python", print the first character.
# word = "Python"
# print(word[0])

# 3. Create a string variable greeting with the value "Hello". Use string interpolation to insert the name "Alice" into the greeting and print the result.
# greeting = "Hello"
# print(f"{greeting} Alice")

# 4. Given the strings part1 = "Data" and part2 = "Science", concatenate them to form "DataScience" and print the result.
# part1 = "Data" 
# part2 = "Science"
# part1_part2 = part1 + part2
# print(part1_part2)

# 5. Given the string phrase = "Welcome", print the last character using negative indexing.
# phrase = "Welcome"
# print(phrase[-1])

# 6. Create a string variable food with the value "pizza". Use string interpolation to create the sentence "I love pizza" and print it.
# food = "pizza"
# print(f"I love {food}")

# 7. Given the strings str_1 = "Good" and str_2 = "Morning", concatenate them with a space in between to form "Good Morning" and print the result.
# str_1 = "Good" 
# str_2 = "Morning"
# str_1_and_str_2 = str_1 + " " + str_2
# print(str_1_and_str_2)

# 8. Given the string text = "Concatenate", print the character at index 5.
# text = "Concatenate"
# print(text[5])

# 9. Create a variable age with the value 25. Use string interpolation to create the sentence "I am 25 years old" and print it.
# age = 25
# print(f"I am {age} years old")

# 10. Create three string variables: city = "New", space = " ", and country = "York". Concatenate them to form "New York" and print the result.
# city = "New"
# space = " "
# country = "York"
# print(city + space + country)

# 11. Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", print the 10th character.
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(alphabet[9])

# 12. Create variables day = "Sunday" and activity = "hiking". Use string interpolation to create the sentence "On Sunday, I am going hiking" and print it.
# day = "Sunday"
# activity = "hiking"
# print(f"On {day}, I am going {activity}")

# 13. Given the strings a = "Super" and b = "Hero", concatenate them to form "SuperHero" and print the result.
# a = "Super"
# b = "Hero"
# print(a + b)

# 14. 	Given the string universe = "MilkyWay", print the third character from the end using 
# negative indexing.
# universe = "MilkyWay"
# print(universe[-3])

# 15. 	Create variables item = "book" and price = 12.99. Use string interpolation to create the 
# sentence "The price of the book is $12.99" and print it.
# item = "book"
# price = 12.99
# print(f"The price of the {item} is ${price}")

# 16. 	Given the strings hello = "Hello" and world = "World", concatenate them with a comma and space 
# in between to form "Hello, World" and print the result.
# hello = "Hello"
# world = "World"
# print(hello + ", " + world)

# 17. 	Given the string sequence = "ABCDEFG", print the character at index 4.
# sequence = "ABCDEFG"
# print(sequence[4])

# 18. 	Create a variable language = "Python". Use string interpolation to create the sentence "I am 
# learning Python" and print it.
# language = "Python"
# print(f"I am learning {language}")

# 19. 	Given the strings start = "Once upon a" and end = " time", concatenate them to form "Once upon a 
# time" and print the result.
# start = "Once upon a"
# end = " time"
# print(start + end)

# 20. 	Given the string sports = "Basketball", print the second character.
# sports = "Basketball"
# print(sports[1])

# 6. Create two string variables: first_name with value "John" and last_name with value "Doe". Concatenate them together and print the result.
# first_name = "John"
# last_name = "Doe"
# print(first_name + " " + last_name)

# 7. Create a string variable message with the value "Hello, ". Interpolate the variable name (assigned the value "Alice") into the message and print the result.
# message = "Hello"
# print(f"{message} Alice")

# 13-08-20225
# 17.	Convert a string “James John Kennedy” called “names” to a list using the string 
# .split() method. Store the result in a list called “names_list”
# names = "James John Kennedy"
# names_list = names.split()
# print(names_list)

# 18.	You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# 'Chicago']. Convert this list into a single string where each city is separated by a 
# semicolon and a space. Store the result in a string called cities_string.
# cities_list = ['New York', 'Los Angeles', 'Chicago']
# cities_string = "; ".join(cities_list)
# print(cities_string)

# 19.	Create a string variable sentence with the value "the quick brown fox jumps over the 
# lazy dog". Capitalize the first letter of the string and 
# print the result.
# sentence = "the quick brown fox jumps over the lazy dog"
# print(sentence.capitalize())

# 20. 	Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# the first letter of each word and print the result.
# book_title = "to kill a mockingbird"
# print(book_title.title())

# 21. 	Create a string variable text with the value "hello world". Count the number of 
# occurrences of the letter 'o' and print the result.
# text ="hello world"
# print(text.count("o"))

# 22. 	Create a string variable filename with the value "document.txt". Check if the string 
# starts with "doc" and print the result.
# filename = "document.txt"
# print(filename.startswith("doc"))

# 23.	Create a string variable url with the value "https://www.example.com". Check if the 
# string ends with ".com" and print the result.
# url = "https://www.example.com"
# print(url.endswith(".com"))

# 24.	Create a string variable phrase with the value "find the needle in the haystack". Find 
# the position of the word "needle" and print the result.
# phrase = "find the needle in the haystack"
# print(phrase.find("needle"))

# 25.	Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# Result. Bonus point if you can do it with the f-string and concatenation methods also.
# template = "Hello, {}. Welcome to {}."
# print(template.format("Alice", "Wonderland"))

# 26.	Create a string variable `quote` with the value "To be or not to be". Find the position 
# of the word "not" and print the result.
# quote = "To be or not to be"
# print(quote.find("not"))

# 27.	Create a string variable word with the value "hello". Check if all characters in the 
# string are lowercase and print the result.
# word = "hello"
# print(word.islower())

# 28.	Create a string variable shout with the value "HELLO". Check if all characters in the 
# string are uppercase and print the result.
# shout = "HELLO"
# print(shout.isupper())

# 29.	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# lowercase and print the result.
# mixed_case = "PyThOn"
# print(mixed_case.lower())

# 30. 	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# uppercase and print the result.
# mixed_case ="PyThOn"
# print(mixed_case.upper())

# 31. 	Create a string variable padded_text with the value " hello ". Remove leading whitespace and 
# print the result.
# padded_text = " hello "
# print(padded_text.lstrip())

# 32. 	Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# print the result.
# padded_text = " hello "
# print(padded_text.rstrip())

# 33.	Create a string variable padded_text with the value " hello ". Remove both leading and trailing 
# whitespace and print the result.
# padded_text = " hello "
# print(padded_text.strip(" "))

# 34.	Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# and print the result.
# greeting = "Hello, World!"
# print(greeting.replace("World", "Alice"))

# text = "hello world"

# text_1 = " hello World"
# text_2 = "hello WORLD "
# text_3 = " HELLO world "
# text_4 = " lorem ipsum dolor sit amet "
# text_5 = " testing whitespace "

# print(text.capitalize())

# Assigment 1
# Example
# book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"
# book_info = "harper lee ; to kill a mockingbird ; 1960 ; ISN 978-0-06-112008-4 ; 324 ; 2999.4789"
# book_info = "george orwell ; 1984 ; 1949 ; ISN 978-0-452-28423-4 ; 328 ; 1999"
# book_info = "j.k. rowling ;  harry potter and the sorcerer's stone   ; 1997 ; ISN 978-0-590-35340-3 ; 309 ; 3499.997"
# book_info = "mary shelley ; frankenstein ; 1818 ; ISN 978-0-14-143947-1 ; 280 ; 2096.78"


# components = book_info.split(" ; ")
# # print(components)

# author = components[0]
# book_title = components[1]
# year_published = components[2]
# isbn = components[3]
# no_of_pages = components[4]
# cost = components[5]

# author, book_title, year_published, isbn, no_of_pages, cost = components
# author = author.title()
# book_title = book_title.title()
# year_published = year_published
# isbn = isbn.replace("ISN", "ISBN")
# no_of_pages = no_of_pages
# cost = f"₦{float(cost):.2f}"

# print(f"""The book {book_title} was written by {author} and published in {year_published}. 
# It has {no_of_pages} pages and {isbn} and costs {cost}.""")


# Assignment 2
# 11. Assign values "Orange", "Banana", "Cherry" to multiple variables x, y and z in one line respectively.
# x, y, z = "Oranges", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# 12.	Assign the values 10, "John", and True to the variables age, name, and is_student in a 
# single line.
# age, name, is_student = 10, "John", True
# print(age)
# print(name)
# print(is_student)

#  13. 	Swap the values of x and y, where x = 5 and y = 10, without using a temporary variable.
# x, y = 5, 10
# x, y = 10, 5
# print(x)
# print(y)

#  14. 	Create a list of numbers with values 1, 2, and 3. Unpack the list into separate 
# variables a, b, and c.

# a, b, c = [1, 2, 3]
# print(a)
# print(b)
# print(c)

#  15. 	Convert a string variable called height from “1.35” to a float.
# height = "1.35"
# c_float = float(height)
# print(type(c_float))


#  16.	Predict the output of the following statements:
	# a) bool("") False
# b) bool(123) True
# c) bool(["apple", "cherry", "banana"]) True
# d) bool(False) False
# e) bool(None) False
# f) bool(0) False
# g) bool("abc") True
# h) bool(()) False
# i) bool([]) False
# j) bool({}) False



# Assignment 3

# One has been done for you as an example:

# Sample Execution:
# Enter your name: David
# Enter the activity you did (e.g., running, cycling): Hiking
# Enter the duration of the activity (in minutes): 120
# Enter the calories burned: 850
#
# Fitness Activity:
# Name: David
# Activity: Hiking
# Duration: 120 minutes
# Calories Burned: 850 kcal
#
# Task:
# Write a Python program that works exactly like the sample above.
# The program should ask the user for their name, activity, duration, and calories burned,
# and then print the details in the same format.

# Solution
# name = input("Enter your name: ")
# activity = input("Enter the activity you did (e.g., running, cycling): ")
# duration = input("Enter the duration of the activity (in minutes): ")
# calories = input("Enter the calories burned: ")

# print("\nFitness Activity:")
# print(f"Name: {name}")
# print(f"Activity: {activity}")
# print(f"Duration: {duration} minutes")
# print(f"Calories Burned: {calories} kcal")


# NOW DO THESE:
# Exercise 1:
# Sample Execution:
# Enter your first name: Alice
# Enter your last name: Johnson
#
# Full Name: Alice Johnson
#
# Task:
# Write a Python program that asks the user for their first name and last name,
# then prints their full name in the format shown above.

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(f"Full Name: {first_name} {last_name}")

# Exercise 2:
# Sample Execution:
# Enter the length of the rectangle: 8
# Enter the width of the rectangle: 5
#
# Area of the rectangle: 40
#
# Task:
# Write a Python program that calculates the area of a rectangle.
# The program should ask for length and width, then display the area.

# rectangle_length = int(input("Enter the length of the rectangle: "))
# rectangle_width = int(input("Enter the width of the rectangle: "))
# print("Area of the rectangle: " + str(rectangle_width * rectangle_length))

# Exercise 3:
# Sample Execution:
# Enter the temperature in Celsius: 25
#
# Temperature in Fahrenheit: 77.0
#
# Task:
# Create a Python program that converts a temperature from Celsius to Fahrenheit.
# Formula: F = (C × 9/5) + 32

# temperature_in_celsius = int(input("Enter the temperature in Celsius: "))
# print("Temperature in Fahrenheit: " + str((temperature_in_celsius * 9/5) +32))

# Exercise 4:
# Sample Execution:
# Enter the number of apples: 4
# Enter the number of bananas: 6
#
# Total fruits: 10
#
# Task:
# Write a program that asks the user for the number of apples and bananas,
# then prints the total number of fruits.

# no_of_apples = int(input("Enter the number of apples: "))
# no_of_bananas = int(input("Enter the number of bananas: "))
# print("Total fruits: " + str(no_of_apples + no_of_bananas))
# print(f"Total fruits: {no_of_apples + no_of_bananas}")

# Exercise 5:
# Sample Execution:
# Enter your age: 30
#
# You will be 35 years old in 5 years.
#
# Task:
# Create a program that asks the user for their age,
# then calculates and prints how old they will be in 5 years.

# age = int(input("Enter your age: "))
# print("You will be " + str(age + 5) + " years old in 5 years." )

# Exercise 6:
# Sample Execution:
# Enter the distance in kilometers: 10
#
# Distance in miles: 6.21371
#
# Task:
# Write a Python program that converts kilometers to miles.
# 1 kilometer = 0.621371 miles.

# distance = float(input("Enter the distance in kilometers: "))
# print("Distance in miles: " + str(distance * 0.621371))


# Exercise 7:
# Sample Execution:
# Enter your favorite color: Blue
# Enter your favorite food: Pizza
#
# Your favorite color is Blue and your favorite food is Pizza.
#
# Task:
# Write a Python program that asks the user for their favorite color and food,
# then displays the message exactly like the example.

# favorite_color = input("Enter your favorite color: ")
# favorite_food = input("Enter your favorite food: ")
# print(f"Your favorite color is {favorite_color} and your favorite food is {favorite_food} ")

# Exercise 8:
# Sample Execution:
# Enter the price of an item: 50
# Enter the discount percentage: 20
#
# Price after discount: 40.0
#
# Task:
# Write a program that calculates the final price after a discount.
# Formula: final_price = price - (price × discount/100)

# item_price = int(input("Enter the price of an item: "))
# discount = int(input("Enter the discount percentage: "))
# print("Price after discount: " + str(item_price - (item_price * discount/100)))


# Exercise 9:
# Sample Execution:
# Enter the number of hours worked: 40
# Enter your hourly rate: 15
#
# Weekly pay: 600
#
# Task:
# Write a program that calculates a worker's weekly pay
# based on hours worked and hourly rate.

# hours_worked = int(input("Enter the number of hours worked: "))
# hourly_rate = int(input("Enter your hourly rate: "))
# print("Weekly pay: " + str(hours_worked * hourly_rate))

# Exercise 10:
# Sample Execution:
# Enter your favorite movie: Inception
# Enter your favorite song: Bohemian Rhapsody
#
# Your favorite movie is Inception and your favorite song is Bohemian Rhapsody.
#
# Task:
# Create a Python program that asks the user for their favorite movie and song,
# then prints them in the same format as the example.

# favorite_movie = input("Enter your favorite movie: ")
# favorite_song = input("Enter your favorite song: ")
# print(f"Your favorite movie is {favorite_movie} and your favorite song is {favorite_song}.")

# num = int(input("Enter a number that is a mutiple of 3: "))
# is_mutiple = num % 3 == 0
# print(f"It is {is_mutiple} that {num} is a mutiple of 3")

# Assignment 18/8/2025
# 1. Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".

# name = input("Enter your name, ")
# print(f'"Hello, {name}!".')

# 2. Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.

# from datetime import datetime

# birth_year = int(input("Enter your birth year: "))
# current_year = datetime.now().year
# age = current_year - birth_year
# print(f'"You are {age} years old."')

# 3. Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.
# favourite_color = input("What is your favorite color? ")
# print(f"Your favorite color is {favourite_color}.")

# 4. Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.

# word = input("Enter a palindrome in the next line: ")
# is_palindrome = word[::] == word[::-1]  
# print(f"It is {is_palindrome} that {word} is a palindrome")
# # OR

# word = input("Enter a palindrome: ")
# the_word = word.replace(" ", "").lower()
# is_palindrome = the_word == the_word[::-1]  
# print(f"It is {is_palindrome} that {the_word} is a palindrome")

# 5. Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.
# import getpass

# password = getpass.getpass("Enter your password (at least 8 characters and not more than 30 characters): ")
# is_valid = 8 <= len(password) <= 30
# print(f"It is {is_valid} that the password fulfils the criteria.")


# 6. Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.
# weight = float(input("Enter your weight: "))
# height = float(input("Enter your height: "))
# bmi = round((weight / (height ** 2)), 2)
# print(f"Your BMI is {bmi}")

# Game 2
# person_1 = input("Enter the name of a person: ").strip()
# number_1 = input("Enter a number: ").strip()
# adjective_1 = input("Enter an adjective: ").strip()
# color = input("Enter a color: ").strip()
# noun_1 = input("Enter a noun: ").strip()
# food_type = input("Enter a type of food in plural form: ").strip()
# noun_2 = input("Enter a noun: ").strip()
# verb = input("Enter a verb ending in 'ing': ").strip()
# cloth_article = input("Enter a/an article of clothing: ").strip()
# adjective_2 = input("Enter an adjective: ").strip()
# celebrity = input("Enter a name of a celeb: ").strip()
# number_2 = input("Enter a number: ").strip()
# person_2 = input("Enter the name of a person: ").strip()
# noun_2 = input("Enter a noun: ").strip()
# person_3 = input("Enter the name of a person: ").strip()
# occupation = input("Enter an occupation: ").strip()


# story = f"""My name is {person_1} and I am {number_1} years old. If I were president, I'd do a whole bunch of {adjective_1} things:
# 1. I would drive the biggest {color} car in the country. And that car would go faster than any other {noun_1} in the world!
# 2. Everyone would eat pepperoni {food_type} for dinner.
# 3. I would live in the Statue of {noun_2} and build a {verb}" pool at her feet.
# 4. I would wear a/an {cloth_article} on my head... and everyone would say I look ADJECTIVE like {celebrity}.
# 5. School would be open only {number_2} days a year.
# 6. I would give my friends the best jobs. I would nominate {person_2} IN ROOM to be secretary of (the) {noun_2}, and {person_3} IN ROOM could be vice {occupation}!
# """
# print(story)

# Game 2
# story = """Hey, TERM OF ENDEARMENT. It's me. What's up? You know, FIRST NAME, FIRST NAME AND LAST NAME. From the PLACE. Two DAY OF THE WEEK s ago. I was the ADJECTIVE guy in the COLOR parachute ITEM OF CLOTHING. I paid the bus boy NUMBER dollars to VERB me your information. I was wondering if maybe you'd like to VERB out with me. Please don't call the VERB department. Alright, I'll VERB. So, that's a no, right?"""

# Assignment 1 19/08/2025
# 1. Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
# fruits = ["apple", "banana",  "orange"]
# print(fruits[0])

# 2. Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.
# colors = ["red", "green", "blue"]
# print(colors[-1])

# 3. Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[3:8])

# 4. Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.
# import string

# alphabets = list(string.ascii_lowercase)
# print(alphabets[-3:])

# 5. Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
# ages = [20, 30, 40]
# ages[1] = 35
# print(ages)

# 6. Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".
# grades = ["A", "B", "C", "D"]
# grades[1:4] = "X"
# print(grades)

# 7. Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.
# cities = ["New York", "London", "Paris"]
# cities.insert(0, "Tokyo")
# print(cities)

# 8. Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
# fruits = ["apple", "banana", "cherry"]
# print(len(fruits))

# 9. Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
# prices = [10.5, 20.0, 15.75]
# print(type(prices[1]))

# 10. Create a list called mixed with items 10, "apple", True. Print the list.
mixed = [10, "apple", True]
print(mixed)

# Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.
# Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
# Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
# Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
# Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.
# Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
# Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
# 18.	Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
#  19.	Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
#  20. 	Create a list called ages with items 25, 35, 20. Sort the list in descending order.
#  21. 	Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
#  22. 	Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
#  23.	Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using
# 	slicing.
#  24.	Create a list called original with items "one", "two", "three". Create a copy of the list.
#  25.	Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and 
# 	list2 together.
#  26.	Access and print the second subject of the first person in the list.
# 	data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]
#  27.	Access and print the first value in the list of numbers associated with "San Francisco".
# 	records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]

#  28.	Get the first e in Ayo’s gender and Get Ben’s age.
#  	group = [
#     ["Ayo", ["Female", 12]],
#     ["Ben", ["Male", 9]]
# ]
#  29.	Get the l in Nina’s gender and Get Tobi’s age
# 	records = [
#     ["Tobi", ["Male", [6]]],
#     ["Nina", ["Female", [7]]]
# ]
#  30.	Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
# robot_grid = [
#     ["R2", ["battery", [98]]],
#     ["R5", ["status", "active"]],
#     ["X1", [["joint", "loose"], "error"]]
# ]
#  31.	Get the Five in the Jazz song title and Get the duration of the Jazz song
# playlist = [
#     ["Jazz", ["Take Five", 5.24]],
#     ["Pop", ["Blinding Lights", 3.20]],
#     ["Rock", ["Bohemian Rhapsody", 5.55]]
# ]
#  32.	Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
# animals = [
#     ["Elephant", ["Herbivore"]],
#     ["Tiger", ["Carnivore"]],
#     ["Frog", ["Amphibian"]]
# ]

