# Print all the numbers from 3 to 27

# i = 3

# while i <= 27:
#   print(i)
#   i += 1

# Print all the numbers from 90 to 16
# i = 90

# while i >= 16:
#   print(i)
#   i -= 1

# Print all the even numbers from 8 to 24 i.e. 8, 10, 12, 14, 16, 20, 22, 24
# i = 8

# while i <= 24:
#   print(i + 2)
#   i += 1

# print all the mutiples of 5 between 7 and 36 i.e. 10, 15, 20, 25, 30, 35

# j = 7

# while j <= 36:
#   if j % 5 == 0:
#     print(j)
#   j += 1

# k = 1
# num = []
# while k <= 50:
#   num.append(k)
#   k += 1

# num = ("").join
# print((num))

# Create a list containing 60 to 100, but stop when you get to 70

# i = 60
# while i <= 69:
#   i += 1
#   if i == 70:
#     continue
#   print(i)


# Create a list containing 10 to 20, but skip 15

# i = 9
# nums = []
# while i <= 19:
#   i += 1
#   if i == 15:
#     continue
#   nums.append(i)

# print(nums)

# Assignment

# 1. Print numbers from 1 to 5

# i = 1

# while i <= 5:
#   print(i)
#   i += 1

# 2. Print "Hello" 3 times

# i = 1
# while i <= 3:
#   print(f"Hello")
#   i += 1

# 3. Print only even numbers from 2 to 10 (do not use += 2)

# i = 1

# while i <= 10:
#   if i % 2 == 0:
#     print(i)
#   i += 1

# 4. Print numbers in reverse from 5 to 1 using a while loop.

# i = 5

# while i >= 1:
#   print(i)
#   i -= 1


# 5.	Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 

# i = 1

# while i <= 10:
#   if i != 5:
#     print(i)
#   i += 1

#  6. 	Print a square of stars
# Ask the user to enter a number
# size = int(input("Enter the size of the sqaure: "))

# i = 0

# while i < size:
#   print("*" * size)
#   i += 1

#  7.	Print a right triangle of stars
# Ask the user to enter a number
# triangle_size = int(input("Enter the size of the triange: "))

# i = 1

# while i < triangle_size:
#   print("*" * i)
#   i += 1


#  8. 	Print a countdown
# Ask the user to enter a number where they want to start the countdown from.

# num = int(input("Enter the number to countdown from: "))

# i = num

# while i >= 1:
#   print(i)
#   i -= 1

# 9. 	Print "1" ten times on the same line using a while loop

# i = 0
# result = ""

# while i < 10:
#     result += "1 "
#     i += 1

# print(result)

# 10.  Print a list of the first 12 multiples of 3 starting from 3

# i = 3

# while i <= 36:
#   if  i % 3 == 0:
#      print(i)
#   i += 1


# Assignment 2

# 1. Write a program that uses a while loop to print numbers from 1 to 10.

# i = 1

# while i <= 10:
#   print(i)
#   i += 1

# 2. Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).

# num = int(input("Enter a number: "))

# i = 1
# total = 0

# while i <= num:
#     total += i
#     i += 1

# print(f"The sum of natural numbers up to {num} is {total}")

# 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.
# correct_password = "secret"

# password = input("Enter the password: ")

# while password != correct_password:
#     print("Incorrect password, try again.")
#     password = input("Enter the password: ")

# print("Correct password")

# 5. Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.

# num = int(input("Enter the number to countdown from: "))

# i = num

# while i >= 0:
#   print(i)
#   i -= 1

# 6. Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.

# n = int(input("Enter the even number to countdown from: "))

# i = 2

# while i <= n:
#   print(i)
#   i += 2

# 7. Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))

# result = 1
# i = 0

# while i < exponent:
#     result *= base
#     i += 1

# print(f"{base} raised to the power of {exponent} is {result}")

# name = "Toluwalase"
# i = 0

# while i < len(name):
#   char = name[i]
#   print(char)
#   i += 1

# naija = "God bless Nigeria"
# i = 0

# while i < len(naija):
#   char = naija[i]
#   print(char)
#   i += 1

# cars = "bmw", "toyota", "honda", "innosun", "mercedes_benz", "nissan"

# i = 0
# while i < len(cars):
#   print(cars[i])
#   i += 1


# Assignment 1 01/09/2025
# 3. Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. 
# E.g. if the secret num is 35, and the user guesses 42, their guess is too high. 
# If they guess lower than 35, their guess is too low.

# import random

# Generate a random secret number between 1 and 50
# secret_number = random.randint(1, 50)

# attempts = 0
# max_attempts = 5

# print("Guess the secret number between 1 and 50. You have 5 attempts.")

# while attempts < max_attempts:
#     guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
#     attempts += 1

#     if guess == secret_number:
#         print(f"🎉 Congratulations! You guessed it right in {attempts} attempts.")
#         break
#     elif guess > secret_number:
#         print("Too high!")
#     else:
#         print("Too low!")

#     if attempts == max_attempts:
#         print(f"❌ Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")


# 9. Write a program that takes a string input from the user and uses a while loop to reverse the string.
# Do not use slicing or reversed().

# text = input("Enter a string: ").strip()
# reversed_text = ""
# i = len(text) - 1

# while i >= 0:
#   reversed_text += text[i]
#   i -= 1

# print("Reversed String:", reversed_text)

# 10.	Write a program that takes comma-separated integers from the user, converts that
# 	to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
#       Use the min() function.

# Take comma-separated integers from the user
# numbers = input("Enter comma-separated integers: ")

# # Convert to tuple of integers
# num_tuple = tuple(int(x.strip()) for x in numbers.split(","))

# # Initialize minimum with the first element
# i = 1
# minimum = num_tuple[0]

# # Loop through the tuple
# while i < len(num_tuple):
#     if num_tuple[i] < minimum:
#         minimum = num_tuple[i]
#     i += 1

# # Print result
# print("The minimum value in the tuple is:", minimum)

#  11. 	Write a program that takes a string input from the user and uses a while loop to count
# 	the occurrences of each character, storing the counts in a dictionary.
# 	Sample Input:
# 	Enter a string: Hello
# 	Sample Output:
# 	{‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}

# # Ask the user for input
# text = input("Enter a string: ")

# # Convert to lowercase (optional, so 'H' and 'h' count the same)
# text = text.lower()

# # Dictionary to store counts
# char_count = {}

# i = 0
# while i < len(text):
#     char = text[i]
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
#     i += 1

# print(char_count)


# Assignment 2

# 2. Write a program that simulates a grocery store checkout. 
# The user should enter the prices of items until they decide to stop. 
# The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48

# Grocery store checkout program

# total_cost = 0.0

# while True:
#     # Ask for item price
#     price = float(input("Enter item price: "))
#     total_cost += price

#     # Ask if the user wants to continue
#     another = input("Enter another item? (yes/no): ").strip().lower()

#     if another != "yes":
#         break

# # Print total cost
# print(f"Total cost: {total_cost:.2f}")



# 3.Write a program that continuously prompts the user to enter a password until they enter a valid one. A
#  valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.
# Password validation program

# while True:
#     password = input("Enter password: ")

#     if 8 <= len(password) <= 25:
#         print("Password accepted.")
#         break
#     else:
#         print("Password must be at least 8 characters long and have a maximum of 25 characters.")

# 4.	Write a program that asks for the user's age and keeps prompting them until they 
# 	enter a valid age (greater than or equal to 0).
# 	Sample Input and Output:
# 	Enter your age: -5
# 	Invalid age. Please enter a valid age.
# 	Enter your age: 25
# 	Age accepted.

# Age validation program

# while True:
#     age = int(input("Enter your age: "))
    
#     if age >= 0:
#         print("Age accepted.")
#         break
#     else:
#         print("Invalid age. Please enter a valid age.")


#  5. 	Write a program that tracks the inventory of items in a store. The user should be able 
# 	to add or remove items and the program should display the current inventory after each
# 	operation. The program stops when the user decides to exit.
# 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit

# Store inventory program

# # Initial inventory
# inventory = {'eggs': 40, 'fish': 200, 'bread': 343, 'yam': 2}

# while True:
#     operation = input("Enter operation (add/remove/exit): ").strip().lower()

#     if operation == "add":
#         item = input("Enter item: ").strip().lower()
#         qty = int(input("Enter quantity: "))

#         if item in inventory:
#             inventory[item] += qty
#         else:
#             inventory[item] = qty

#         print("Current inventory:", inventory)

#     elif operation == "remove":
#         item = input("Enter item: ").strip().lower()
#         qty = int(input("Enter quantity: "))

#         if item in inventory:
#             inventory[item] -= qty
#             if inventory[item] < 0:  # prevent negative stock
#                 inventory[item] = 0
#         else:
#             print(f"{item} not found in inventory.")

#         print("Current inventory:", inventory)

#     elif operation == "exit":
#         print("Exiting program. Final inventory:", inventory)
#         break

#     else:
#         print("Invalid operation. Please enter add/remove/exit.")


# 1. Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)

# digits = input("Enter an integer: ")
# sum_of_digits = 0

# for digit in digits:
#     sum_of_digits += int(digit)

# print(sum_of_digits)


# 2. Collect a string from the user and use loops to count the number of vowels 
# and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

# text = input("Enter a text: ").strip().lower()
# vowels = "aeiou"

# vowel_count = 0
# consonant_count = 0

# for char in text:
#     if char.isalpha():
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1

# print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")        

# text = input("Enter a text: ")

# vowels = ("aeiou")

# vowel_count = 0
# consonant_count = 0

# for char in text:
#     if char.isalpha():
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
    
# print(f"{vowel_count} {consonant_count}")







# 3. Write a program that takes an integer input from the user and 
# prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

# number = int(input("Enter an integer: "))


# for num in range(1, 13):
#     print(f"{number} x {num} = {number * num}")




# 4. Collect a string from the user and use a loop to reverse the string. 
# Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

# text = input("Enter a text: ").strip().lower()

# reversed_text = ""

# for char in text:
#     reversed_text = char + reversed_text

# print(reversed_text)

# 5. Write a program that takes a list of numbers (entered as comma-separated values) 
# from the user and removes any duplicate values. 
# Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# # Step 1: Take input
# raw_input = input("Enter numbers as comma-separated values: ")

# # Step 2 & 3: Convert input string to a list of integers
# numbers = []
# for part in raw_input.split(","):
#     part = part.strip()        # remove spaces
#     if part:                   # skip empty entries
#         numbers.append(int(part))

# # Step 4 & 5: Remove duplicates using a loop
# unique_numbers = []
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)

# # Step 6: Print result
# print("List without duplicates:", unique_numbers)

# 6.	Write a program that takes an integer input n from the user and prints the first 
# 	n numbers in the Fibonacci sequence. Example:
# 	Input: 10
# 	Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Step 1: Input
# n = int(input("Enter how many Fibonacci numbers to print: "))

# # Step 2: Handle small cases
# a, b = 0, 1   # first two Fibonacci numbers

# # Step 3: Loop through n terms
# for i in range(n):
#     print(a, end=", " if i < n-1 else "")  # print with commas
#     a, b = b, a + b  # update values



#  7. 	Collect a list of numbers from the user (entered as comma-separated values) and use a 
# 	loop to find and print the largest number in the list. Don’t use the built-in max 
# 	function or anything similar.
# 	Input: "10, 20, 5, 15"
# 	Output: 20

# # Step 1: Take input
# raw_input = input("Enter numbers as comma-separated values: ")

# # Step 2 & 3: Convert to list of integers
# numbers = []
# for part in raw_input.split(","):
#     part = part.strip()
#     if part:   # skip empty parts
#         numbers.append(int(part))

# # Step 4: Assume first number is the largest
# largest = numbers[0]

# # Step 5: Loop to find the largest
# for num in numbers:
#     if num > largest:
#         largest = num

# # Step 6: Print result
# print("The largest number is:", largest)

#  8. 	Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# 	Input: 10
# 	Output: 30 (2 + 4 + 6 + 8 + 10)

# # Step 1: Input
# n = int(input("Enter an integer: "))

# # Step 2: Initialize sum
# total = 0

# # Step 3: Loop from 1 to n
# for i in range(1, n + 1):
#     if i % 2 == 0:   # Step 4: check if even
#         total += i   # Step 5: add to total

# # Step 6: Print result
# print("Sum of even numbers from 1 to", n, "is:", total)



#  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# 	in the string. Print each character along with its frequency. Example:
# 	Input: "hello"
# 	Output:
# h: 1
# e: 1
# l: 2
# o: 1


# text = input("Enter a string: ")
# frequency = {}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# for char, count in frequency.items():
#     print(f"{char}: {count}")
 

# 10.	Write a program that takes an integer n from the user and calculates the sum of 
# 	squares of all numbers from 1 to n. Print the sum. Example:
# 	Input: 3
# 	Output: 14 (1^2 + 2^2 + 3^2)



# n = int(input("Enter an integer: "))

# total = 0

# for i in range(1, n + 1):
#     total += i ** 2 
# print("Sum of squares from 1 to", n, "is:", total)


#  11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. Example:
# 	Input: "Portable Network Graphics"
# 	Output: "PNG"


# phrase = input("Enter a phrase: ")

# words = phrase.split()

# acronym = ""

# for word in words:
#     acronym += word[0].upper()
# print("Acronym:", acronym)


#  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# 	Print the count. Example:
# 	Input: "Hello world from Python"
# 	Output: 4

# text = input("Enter a string: ")

# words = text.split()

# count = 0
# for word in words:
#     count += 1

# print(f"{count}")


#  13. 	Collect a string from the user and only print put the words that start with the letter 
# 	‘S’. Example:
# 	Input: “Print only the words that start with s in this sentence”
# 	Output: 
# 	start
# 	s
# 	Sentence

# text = input("Enter a string: ")

# words = text.split()

# for word in words:
#     if word[0].lower() == 's':   # .lower() handles both 's' and 'S'
#         print(word)


#  14. 	Print all the even numbers from 1 to 20 using the range function and a loop.


#  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	by 3.

# divisible_by_3 = [i for i in range(1, 51) if i % 3 == 0]
# print(divisible_by_3)


# 16.	Go through the string below and if the length of a word is even, print that word.
# 	st = ‘Print every word in this sentence that has an even number of letters’
# 	Output: 
# 	word
# 	in
# 	this
# 	sentence
# 	that
# 	an
# 	even
# 	number
# 	of

# st = "Print every word in this sentence that has an even number of letters"

# # Split into words
# words = st.split()

# # Loop through and check length
# for word in words:
#     if len(word) % 2 == 0:
#         print(word)


#  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



#  18.	You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B

# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# for i in range(len(names)):
#     print(f"{names[i]} got grade {grades[i]}")



#  19. Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']

# Expected Output:
# 0: shoe
# 2: toy

# items = ['shoe', 'stick', 'toy', 'fruit']
# for i in range(len(items)):
#     if i % 2 == 0:
#         print(f"{i}: {items[i]}")



#  20.	Given two lists of numbers of the same length, print the indices and values
#  	of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
# ]

# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# # Loop through indices
# for i in range(len(list1)):
#     if list1[i] != list2[i]:
#         print(f"Index {i}: list1 = {list1[i]}, list2 = {list2[i]}")


# Comprehension Assignments
# 7. Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]
# the_greetings = all(greeting.isupper() for greeting in greetings)
# print(the_greetings)


# 8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
# words = ["apple", "zebra", "mango", "lemon"]
# the_words = any(word.startswith("z") for word in words)
# print(the_words)


# 9. Is there any email address that contains ".org"?
# Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# Expected Output: True
# emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# the_emails = any(email.endswith(".org") for email in emails)
# print(the_emails)

# 10. Are all numbers odd?
# Input: [1, 3, 5, 7, 9]
# Expected Output: True
# values = [1, 3, 5, 7, 9]
# the_values = all(value % 2 == 1 for value in values)
# print(the_values)

# 11. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
# words = ["hi", "dog", "go", "sun"]
# the_words = all(len(word) > 2 for word in words)
# print(the_words)

# 12. Create a list of triple the value of each number
# Input: [2, 4, 6, 8]
# Expected Output: [6, 12, 18, 24]
# nums = [2, 4, 6, 8]
# the_nums = [num * 3 for num in nums]
# print(the_nums)


# 13. Are all temperatures above 0°C?
# Input: [12, 7, 3, -1, 5]
# Expected Output: False
# temperatures = [12, 7, 3, -1, 5]
# the_temperatures = all(temperature > 0 for temperature in temperatures)
# print(the_temperatures)

# 14. Do all words end with a vowel?
# Input: ["banana", "mango", "kiwi", "grape"]
# Expected Output: True
# fruits = ["banana", "mango", "kiwi", "grape"]
# the_fruits = all(fruit.endswith("a") or fruit.endswith("e") or fruit.endswith("i") or fruit.endswith("o") or fruit.endswith("u") for fruit in fruits)
# print(the_fruits)


# 15. Create a list of words in lowercase
# Input: ["HELLO", "WORLD", "PYTHON"]
# Expected Output: ["hello", "world", "python"]
# greetings = ["HELLO", "WORLD", "PYTHON"]
# the_greetings = [greeting.lower() for greeting in greetings]
# print(the_greetings)

# 16. Is there any number less than 0?
# Input: [5, -2, 3, 0, 8]
# Expected Output: True
# numbers = [5, -2, 3, 0, 8]
# the_numbers = any(number < 0 for number in numbers)
# print(the_numbers)

# 17. Create a list of words that contain the letter 'e'
# Input: ["sky", "tree", "rock", "stone"]
# Expected Output: ["tree", "stone"]
# items = ["sky", "tree", "rock", "stone"]
# the_items = [item for item in items if item.lower().count("e")]
# print(the_items)

# 18. Are all names starting with uppercase letters?
# Input: ["Alice", "Bob", "charlie", "David"]
# Expected Output: False
# names = ["Alice", "Bob", "charlie", "David"]
# the_names = all(name.isupper() for name in names)
# print(the_names)

# 19. Is there any sentence longer than 20 characters?
# Input: ["Short one", "This is a much longer sentence", "Okay"]
# Expected Output: True
# sentences = ["Short one", "This is a much longer sentence", "Okay"]
# the_sentences = any(len(sentence) > 20 for sentence in sentences)
# print(the_sentences)
