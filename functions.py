"""
This file will teach you how functions work in Python.
"""
# password = "P@ssword123"


# is_long_enough = len(password) >= 8
# has_upper = any(char.isupper() for char in password)
# has_lower = any(char.islower() for char in password)
# has_digit = any(char.isdigit() for char in password)
# has_special_char = any(char in "!@#$%^&*()" for char in password)

# is_strong_password = is_long_enough and has_upper and has_lower and has_digit and has_special_char
# print(is_strong_password)


# is_strong_password = all([is_long_enough, has_upper, has_lower, has_digit, has_special_char])
# print(is_strong_password)



# is_long_enough = len(password) >= 8

# has_upper = False
# has_lower = False
# has_digit = False
# has_special_char = False

# for char in password:
#     if char.isupper():
#         has_upper = True
#     elif char.islower():
#         has_lower = True
#     elif char.isdigit():
#         has_digit = True
#     elif char in "!@#$%^&*()":
#         has_special_char = True



# is_strong_password = is_long_enough and has_upper and has_lower and has_digit and has_special_char
# print(is_strong_password)


# is_strong_password = all([is_long_enough, has_upper, has_lower, has_digit, has_special_char])
# print(is_strong_password)


# def password_strength_checker(password_to_check):
#     is_long_enough = len(password_to_check) >= 8

#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special_char = False
#     has_smiley_face = "😃" in password_to_check

#     for char in password_to_check:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in "!@#$%^&*()":
#             has_special_char = True

#     is_strong_password = is_long_enough and has_upper and has_lower and has_digit and has_special_char and has_smiley_face
#     print(is_strong_password)

# password1 = "P@ssword1😃23"
# password_strength_checker(password1)
# print()
# print()
# print()
# password2 = "passWord123!"
# password_strength_checker(password2)

# password3 = "qwerty12😃3"
# password_strength_checker(password3)





# def greet():
#     print("good morning")


# greet()


# def greet(name):  # parameter
#     print(f"Good morning {name}!")


# my_name = "Praise"
# greet(my_name)  # argument





# def add_two_nums(num1, num2):
#     print(f"The sum of {num1} and {num2} is {num1 + num2}")

# add_two_nums(8, 100)




# def greet(name, time_of_day):
#     print(f"Good {time_of_day}, {name}")


# greet("Deborah", "morning")


# Write a function called multiply_two_nums that accepts two numbers first_num and second_num
# and prints the product of the numbers
# After, call the function

# def multiply_two_nums(first_num, second_num):
    # return first_num * second_num
    # print(first_num * second_num)
    # pass

# print(multiply_two_nums(4, 6))
# multiply_two_nums(4, 6)




# def double(num):
#     print(num)
#     return num * 2

# print(double(7))
# double(7)
# greet()




# def greet():
#     print("Good afternoon, SQI July Python Gurus")
#     print("inside function")


# print(greet())



# def greet():
#     print('Hello World!')

# greet()
# print('Outside function')





# print("Lorem ipsum dolor")  # 1
# def greet():
#     print("sit amet")  # 3, 6
#     print('Hello World!')  # 4, 7

# print('tempor incididunt ut labore')  # 2
# greet()
# print("consectetur adipiscing elit")  # 5
# greet()
# print("Nemo enim ipsam voluptatem")  # 8


# print("The sun rises in the east")  # 1


# def greet():
#     print("How's it going?")  # 2, 5, 7, 10
#     print("Stay curious, stay kind.")  # 3, 6, 8, 11


# greet()

# print("Midnight thoughts and coffee sips")  # 4
# greet()
# greet()
# print("Learning never exhausts the mind")  # 9
# greet()
# print("Wander often, wonder always")  # 12



# def cube(num):
#     return num ** 3


# cubed = cube(2)
# print(cubed)

# print(cube(2))



# def my_func():
#     return "False"


# Write a function is_even that accepts a paramter num and returns True if num is even, otherwise, it returns False.


# def is_even(num: int):
#     return num % 2 == 0
    
# print(is_even(5))
# print(is_even(12))



# Write a function called starts_with_s that accepts a parameter called word
# and returns True if the word starts with s, regardless of case,
# otherwise, it returns False.


# def loop_through_list(list_of_nums):
#     for num in list_of_nums:
#         print(num)


# print(loop_through_list([8, 289, 1, 98, 19, 94, 56]))


# type hints / type annotations
# def get_first_multiple_of_3(list_of_nums: list[int]):
#     for num in list_of_nums:
#         if num % 3 == 0:
#             return num


# result = get_first_multiple_of_3([10, 2, 7, 19, 36])  # 36
# print(result)
# print(get_first_multiple_of_3([10, 2, 6, 7, 19]))  # 6
# print(get_first_multiple_of_3([10, 2, 7, 19]))  # 6


# phone_book: list[dict[str, str | int | bool]] = [
#     {"name": "Damilola Aregbesola", "contact": "07063457615", "is_favorite": True, "age": 20},
#     {"name": "Benjamin Anjorin", "contact": "08088624654", "is_favorite": False, "age": 95},
#     {"name": "Maryam Aleshinloye", "contact": "09034983551", "is_favorite": True, "age": 10}
# ]



# def greet(name, time_of_day):
#     print(f"Good {time_of_day}, {name}")


# result = greet("Deborah", "morning")
# print(result)
# print(result)
# print(result)
# print(result)
# print(result)
# print(result)



# def greet(name, time_of_day):
#     return f"Good {time_of_day}, {name}", name.upper()


# result, uppercase_name = greet("Deborah", "morning")
# print(result)
# print(uppercase_name)



# def greet(name="Anonymous", time_of_day="day"):
# def greet(time_of_day="evening", name="Anonymous"):
#     print(f"Good {time_of_day}, {name}")


# # result = greet("Deborah", "afternoon")
# result = greet()
# print(result)



# def greet(name, time_of_day, hobby, location, age, fave_thing_to_do):
#     print(f"Good {time_of_day}, everyone. My name is {name}. My fave thing to do is {fave_thing_to_do}. I am {age} years old living in {location}. I also love to {hobby}.")


# # greet("Deborah", "afternoon", "code", "Ibadan", 12, "art")  # positional arguments
# greet(hobby="code", location="Ibadan", name="Deborah", age=12, time_of_day="afternoon", fave_thing_to_do="art")  # kwargs - keyword arguments

#-----------------------------------------ASSIGNMENT-----------------------------------------------
# 1. Create a function called turn_to_upper(names) that takes in a list of names, and returns a list of names uppercased
# after, print the result of the function.
# For example, if names is ["Winifred", "Wilfred", "Justin", "Augusta"], the result would be [ "WINIFRED", "WILFRED", "JUSTIN", "AUGUSTA"]

# 2. Create a function called get_middle_name that accepts one paramter `name_dict` that takes in a dictionary with keys "first", "middle", and "last".
# The function should return only the middle name.
# For example, if name_dict is {"first": "Tola", "middle": "James", "last": "Akin"}, then the result would be "James". Another example is if name_dict is {"middle": "Chioma", "first": "Ada", "last": "Okeke"}, the result would be "Chioma".


# happy path
# def get_middle_name(name_dict):
#     return name_dict.get("middle", "N/A")
#     # return name_dict["middle"]

# # print(get_middle_name({"first": "Tola", "middle": "James", "last": "Akin"}))
# print(get_middle_name({"first": "Tola", "other": "James", "last": "Akin"}))

# 3. Create a function called reverse_string that accepts a string as input and returns the string reversed.
# For example, if the string is "Python", the result would be "nohtyP".


# 4. Create a function called count_vowels that accepts a string and returns the number of vowels (a, e, i, o, u) in it.
# For example, if the string is "beautiful", the result would be 5.

# def count_vowels(text: str) -> int:
#     text = text.lower()
#     vowels = "aeiou"
#     no_of_vowels = 0
#     for char in text:
#         if char in vowels:
#             no_of_vowels += 1
#     return no_of_vowels

# print(count_vowels("beautiful"))


# def count_vowels(text: str) -> int:
#     text = text.lower()
#     vowels = "aeiou"
#     vowels_found = [char for char in text if char in vowels]
#     return len(vowels_found)

# print(count_vowels("beautiful"))


# def count_vowels(text: str) -> int:
#     text = text.lower()
#     vowels = "aeiou"
#     vowels_found = sum(char in vowels for char in text)
#     return vowels_found
# print(count_vowels("beautiful"))

# 5. Create a function called even_numbers that takes in a list of integers and returns a new list containing only the even numbers.
# For example, if the list is [1, 2, 3, 4, 5, 6], the result would be [2, 4, 6].

# def even_numbers(list_of_ints):
#     return [num for num in list_of_ints if num % 2 == 0]

# print(even_numbers([1, 2, 3, 4, 5, 6]))

# 6. Create a function called find_max that takes in a list of numbers and returns the maximum number in the list.
# For example, if the list is [12, 45, 3, 67, 23], the result would be 67.

# def find_max(list_of_nums):
#     return max(list_of_nums)

# max_num = find_max([12, 45, 3, 67, 23])
# print(max_num)

# 7. Create a function called sum_dict_values that takes in a dictionary with numeric values and returns the sum of all the values.
# For example, if the dictionary is {"a": 10, "b": 20, "c": 5}, the result would be 35.

# def sum_dict_values(dict_nums):
#     return sum(dict_nums.values())

# print(sum_dict_values({"a": 10, "b": 20, "c": 5}))

# 8. Create a function called word_lengths that takes in a list of words and returns a dictionary where each word is a key and its length is the value.
# For example, if the list is ["apple", "banana", "cherry"], the result would be {"apple": 5, "banana": 6, "cherry": 6}.

# def word_lengths(words: list[str]):
#     value_lengths = {}
#     for word in words:
#         value_lengths[word] = len(word)
#     return value_lengths

# print(word_lengths(["apple", "banana", "cherry"]))


# def word_lengths(words: list[str]):
#     return {word: len(word) for word in words}

# print(word_lengths(["apple", "banana", "cherry"]))

# 9. Create a function called is_palindrome that takes in a string and returns True if the string is a palindrome (same forwards and backwards), otherwise False.
# For example, if the string is "level", the result would be True. If the string is "hello", the result would be False.

# def is_palindrome(text: str):
#     text = text.lower().strip().replace(" ", "")
#     return text == text[::-1]
    
# print(is_palindrome("level"))
# print(is_palindrome("nurses run"))
# print(is_palindrome("TUNde EdNut"))

# 10. Create a function called merge_lists that takes in two lists and returns one combined list without duplicates.
# For example, if list1 = [1, 2, 3] and list2 = [3, 4, 5], the result would be [1, 2, 3, 4, 5].

# def merge_lists(list1: list[int], list2: list[int]):
#     return list(set(list1 + list2))

# print(merge_lists([1, 2, 3], [3, 4, 5]))

# 11. Create a function called multiply_numbers(a, b=2) that multiplies two numbers.
# If the second number is not provided, it should default to 2.
# Example 1: multiply_numbers(5) → 10
# Example 2: multiply_numbers(5, 3) → 15

# def multiply_numbers(a, b=2):
#     return a * b

# print(multiply_numbers(5))  # 10
# print(multiply_numbers(5, 3))  # 15

# 12. Create a function called greet_user(first_name, last_name="") that returns a greeting string.
# If last_name is not provided, it should only greet with the first name.
# Example 1: greet_user("Ada") → "Hello, Ada!"
# Example 2: greet_user("Tola", "Akin") → "Hello, Tola Akin!"

# def greet_user(first_name, last_name=""):
#     name = f"{first_name} {last_name}".strip()
#     return f"Hello, {name}!"

# print(greet_user("Ada"))
# print(greet_user("Tola", "Akin"))


# def greet_user(first_name, last_name=""):
#     last_name = f" {last_name}" if last_name else ""
#     return f"Hello, {first_name}{last_name}!"

# print(greet_user("Ada"))
# print(greet_user("Tola", "Akin"))

# 13. Create a function called power(base, exponent=2) that raises the base to the power of the exponent.
# The exponent should default to 2 (square).
# Example 1: power(4) → 16
# Example 2: power(2, 3) → 8

# 14. Create a function called format_full_name(first, middle="", last="") that returns the full name as a single string.
# If middle or last is not provided, it should still work correctly.
# Example 1: format_full_name("John", "Paul", "Smith") → "John Paul Smith"
# Example 2: format_full_name("Ada", last="Okeke") → "Ada Okeke"
# Example 3: format_full_name("Ada", middle="Chinenye") → "Ada Chinenye"
# Example 4: format_full_name("Ada") → "Ada"

# def format_full_name(first, middle="", last=""):
#     middle = f" {middle}" if middle else ""
#     last = f" {last}" if last else ""
#     return f"{first}{middle}{last}!"



# print(format_full_name("John", "Paul", "Smith")) # "John Paul Smith"
# print(format_full_name("Ada", last="Okeke")) # "Ada Okeke"
# print(format_full_name("Ada", middle="Chinenye")) # "Ada Chinenye"
# print(format_full_name("Ada")) # "Ada"


# 15. Create a function called calculate_discount(price, discount=10, tax=0) that calculates the final price after applying a discount (percentage) and then adding tax (percentage).
# Example 1: calculate_discount(100) → 90.0   (10% discount, no tax)
# Example 2: calculate_discount(200, discount=20, tax=5) → 168.0

# def calculate_discount(price, discount=10, tax=0):
#     price_after_discount = ((100 - discount) / 100) * price
#     price_after_tax = (tax / 100) * price_after_discount
#     return price_after_tax + price_after_discount

# print(calculate_discount(100))  # 90.0
# print(calculate_discount(200, discount=20, tax=5))  # 90.0

# -----------------------------------------ASSIGNMENT-----------------------------------------------



# print("Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", "Python", sep=";", end="")



# *args - arbitrary arguments

# print(sum([19, 8, 278, 477, 2893, 273]))


# def add_any_number_of_nos(*nums):
#     return sum(nums)


# print(add_any_number_of_nos(19, 8, 278, 477, 2893, 273))



# def greet_everyone(*names, greeter):
#     for name in names:
#         print(f"Hello, {greeter} says hi {name} 💗")

# greet_everyone("Praise", "Damilola", "Maryam", "Benjamin", "John", "Ayomide", greeter="Ife")



# def greet_with_emoji(**people_and_emojis):
#     print(people_and_emojis)
#     for person, emoji in people_and_emojis.items():
#         print(f"{person} {emoji}")


# # greet_with_emoji(maryam="🔥", benjamin="💀", damilola="💗", praise="💻", ife="🌚", john="🐐", ayomide="👍")

# people_and_emojis = {'Maryam Aleshinloye': '🔥', 'benjamin': '💀', 'damilola': '💗', 'praise': '💻', 'ife': '🌚', 'john': '🐐', 'ayomide': '👍'}

# greet_with_emoji(**people_and_emojis)


# def states_and_their_capitals(**states_and_capitals: dict[str, str]):
#     for state, capital in states_and_capitals.items():
#         print(f"The capital of {state} is {capital}")

# # states_and_their_capitals(**{'Oyo': "Ibadan", "Osun": "Osogbo", "Delta": "Asaba", "Anambra": "Awka", "Bauchi": "Bauchi"})
# states_and_their_capitals(oyo="Ibadan", osun="Osogbo", delta="Asaba", anambra="Awka", bauchi="Bauchi")


# def count_fruits(something, *no_of_fruits, **fruits_and_quantities):
#     print("something is ",something)
#     return sum(no_of_fruits) + sum(fruits_and_quantities.values())



# print(count_fruits("pen", 3, 8, 9, apple=8, bananas=12, cherry=3))  # 43



# def power(base, exponent):
#     if exponent == 0:  # Base case
#         return 1
#     else:
#         return base * power(base, exponent - 1)  # Recursive call

# print(power(2, 3))  # Output: 8



# power(2, 3)
# 2 * power(2, 2)
# 2 * 2 * power(2, 1)
# 2 * 2 * 2 * power(2, 0)
# # 2 * 2 * 2 * 1 -> 8



# Variable scope

# story = """Once upon a time,
# there lived a girl.
# She taught herself to code.
# She now teaches Python at SQI."""



# name = "Winnie"

# def calculate_discount(price, discount=10, tax=0):
#     """
#     This will calculate the discount on price and add tax.
#     """
#     global name
#     name = "Ben"
#     print("Inside func", name)
#     price_after_discount = ((100 - discount) / 100) * price
#     price_after_tax = (tax / 100) * price_after_discount
#     return price_after_tax + price_after_discount


# print(name)
# print(calculate_discount(100))  # 90.0
# # print(calculate_discount(200, discount=20, tax=5))  # 90.0

# # print(price)
# print("Outside func", name)


# docstring


# Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration('Levelheaded llama') # True
# is_alliteration('Crazy Kangaroo') # False


# "Levelheaded llama"

# 1. Separate the two word string into two words
# 2. Check if the first letter of the first word is the same as the first letter of the second word
# 3. Return that result



# def is_alliteration(two_word_string: str):
#     words = two_word_string.lower().split()
#     word1, word2 = words
#     return word1[0] == word2[0]
    
# print(is_alliteration('Levelheaded llama')) # True
# print(is_alliteration('Crazy Kangaroo')) # False




# ====================================ASSIGNMENT 1===========================================
# 1. Create a function called get_total_length that returns the total number of characters in all the words passed in.

# Test Data:
# print(get_total_length("apple", "banana", "car"))
# print(get_total_length("hi", "hello"))

# Expected Output:
# 14
# 7

# def get_total_length(*words):
#     no_of_words = 0
#     for word in words:
#         no_of_words += len(word)
#     return no_of_words

# print(get_total_length("apple", "banana", "car"))
# print(get_total_length("hi", "hello"))


# def get_total_length(*words):
#     return sum(len(word) for word in words)

# print(get_total_length("apple", "banana", "car"))
# print(get_total_length("hi", "hello"))
 
# 2. Create a function called highest_score that returns the name of the student with the highest score.


# def highest_score(**students_with_scores):
#     if not students_with_scores:
#         return
#     highest_score = list(students_with_scores.values())[0]
#     student_with_highest_score = list(students_with_scores.keys())[0]
#     for student, score in students_with_scores.items():
#         if score > highest_score:
#             highest_score = score
#             student_with_highest_score = student
#     return student_with_highest_score            

# # Test Data:
# # print(highest_score(Ada=72, Bisi=89, Charles=67))
# # print(highest_score(Emeka=90, Tolu=91, Zainab=88))
# print(highest_score())
# print(highest_score())


# def highest_score(**students_with_scores):
#     if not students_with_scores:
#         return
#     return max(students_with_scores, key=students_with_scores.get)

# print(highest_score())
# print(highest_score())

# Expected Output:
# Bisi
# Tolu

# 3. Create a function called multiply_first_two that returns the product of the first two numbers passed in.

# arbitrary (any) number of args
# def multiply_first_two(*nums):
#     if len(nums) < 2:
#         return
#     return nums[0] * nums[1]

# # Test Data:
# print(multiply_first_two(3, 5, 9, 2))
# print(multiply_first_two(10, 2, 7))
# print(multiply_first_two())
# print(multiply_first_two(10))

# Expected Output:
# 15
# 20


# 4. Create a function called describe_books that prints out each book title and its author.



# def describe_books(**books_with_authors: dict[str, str]):
#     for book, author in books_with_authors.items():
#         print(f"{book} was written by {author}")

# # describe_books(Hamlet="Shakespeare", ThingsFallApart="Chinua Achebe", Dune="Frank Herbert")
# describe_books(**{"Hamlet": "Shakespeare", "Things Fall Apart": "Chinua Achebe", "Dune": "George Orwell"})
# describe_books(**{"Matilda": "Roald Dahl", "1984": "George Orwell"})
# describe_books(Matilda="Roald Dahl", 1984="George Orwell")
# Test Data:


# Expected Output:
# Hamlet is written by Shakespeare
# ThingsFallApart is written by Chinua Achebe
# Dune is written by Frank Herbert
# Matilda is written by Roald Dahl
# 1984 is written by George Orwell


# 5. Create a function called total_age that returns the sum of all the ages given.

# def total_age(*ages):
#     return sum(ages)

# # Test Data:
# print(total_age(12, 30, 18))
# print(total_age(40, 25))

# # Expected Output:
# # 60
# # 65


# 6. Create a function called list_countries that prints out each country passed in.

# Test Data:
# list_countries("Nigeria", "Ghana", "Kenya")
# list_countries("Canada", "Mexico")

# Expected Output:
# Nigeria
# Ghana
# Kenya
# Canada
# Mexico

# 7. Create a function called student_details that prints each student's name and score.

# Test Data:
# student_details(Fola=78, Muna=88, Kola=65)
# student_details(Sandra=91, Alex=85)

# Expected Output:
# Fola scored 78
# Muna scored 88
# Kola scored 65
# Sandra scored 91
# Alex scored 85


# 8. Create a function called average_score that returns the average of all scores passed in.

# def average_score(*scores):
#     return sum(scores) / len(scores)

# # Test Data:
# print(average_score(50, 60, 70))
# print(average_score(80, 90))

# Expected Output:
# 60.0
# 85.0

# 9. Create a function called total_price that adds up the prices of all items passed as keyword arguments.

# def total_price(**items_and_prices):
#     return sum(items_and_prices.values())

# # Test Data:
# print(total_price(bread=500, milk=1200, eggs=700))
# print(total_price(book=1500, pen=200))

# Expected Output:
# 2400
# 1700


# 10. Create a function called first_and_last that prints the first and last values passed in.


# def first_and_last(*values):
#     print(f"First: {values[0]}, Last: {values[-1]}")

# # # Test Data:
# first_and_last(4, 10, 6, 9, 12)
# first_and_last("a", "b", "c", "d")

# Expected Output:
# First: 4, Last: 12
# First: a, Last: d

# def first_and_last(*values):
#     return values[0], values[1]


# first, last = first_and_last(4, 10, 6, 9, 12)
# print(f"First: {first}, Last: {last}")
# first, last = first_and_last("a", "b", "c", "d")
# print(f"First: {first}, Last: {last}")



# 11. Create a function called describe_animals that prints out animal and their sound.

# Test Data:
# describe_animals(cat="meow", dog="bark", cow="moo")
# describe_animals(lion="roar", snake="hiss")

# Expected Output:
# cat makes the sound meow
# dog makes the sound bark
# cow makes the sound moo
# lion makes the sound roar
# snake makes the sound hiss


    

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# # list3 = [1, 2, 3, 4, 5, 6]
# list3 = [*list1, *list2]
# print(list3)

# 12. Create a function called total_characters that returns how many characters in total exist in all keyword values.


# def total_characters(**keywords_and_values):
#     return sum(len(value) for value in keywords_and_values.values())


# # Test Data:
# print(total_characters(a="banana", b="mango", c="kiwi"))
# print(total_characters(x="hi", y="there"))

# Expected Output:
# 15
# 7


# 13. Create a function called find_minimum that returns the smallest number from all the values passed in.

# Test Data:
# print(find_minimum(99, 45, 12, 88))
# print(find_minimum(8, 3, 7))

# Expected Output:
# 12
# 3


# 14. Create a function called sum_scores_and_bonuses that returns the total of all numbers passed, including keyword values.

# Test Data:
# print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
# print(sum_scores_and_bonuses(100, bonus=50))

# Expected Output:
# 50
# 150


# 15. Create a function called longest_word that returns the longest string from all the values passed in (args + kwargs).

# def longest_word(*args, **kwargs):
#     all_words = [*args, *kwargs.values()]
#     return max(all_words, key=len)

# # Test Data:
# print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
# print(longest_word("short", name="exaggeration", tool="pen"))

# Expected Output:
# hippopotamus
# exaggeration
# ====================================ASSIGNMENT 1===========================================



# ====================================ASSIGNMENT 2===========================================

# 1. Write a function sum_numbers(a, b) that returns the sum of two numbers.
# def sum_numbers(a, b):
#     return a + b

# print(sum_numbers(4, 9))
# print(sum_numbers(5, 1))


# 2. Write a function is_even(n) that returns True if n is even and False if n is odd.

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False


# def is_even(n):
#     return True if n % 2 == 0 else False

# print(is_even(19))

# def is_even(n):
#     return n % 2 == 0

# 3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.

# A prime number is a natural number that can only be divided EXACTLY by 1 and itself.
# def is_prime(n: int):
#     if n <= 1:
#         return False
    
#     for num in range(2, round(n ** 0.5) + 1):
#         if n % num == 0:
#             return False
#     return True

# print(is_prime(353))


# 4. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.

# def list_all_primes(limit):
#     prime_nums = []
#     for num in range(2, limit+1):
#         if is_prime(num):
#             prime_nums.append(num)

#     return prime_nums


# n = int(input("Enter the value of n: "))
# print(list_all_primes(n))

# print(is_prime(9))
# def list_first_n_primes(limit):
#     prime_nums = []
#     num = 2
#     while True:
#         if is_prime(num):
#             prime_nums.append(num)
#         if len(prime_nums) == limit:
#             break 
#         num += 1

#     return prime_nums


# n = int(input("Enter the value of n: "))
# print(list_first_n_primes(n))



# 5. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.

# 6. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration('Levelheaded llama') —> True
# is_alliteration('Crazy Kangaroo') –> False


# 7. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') —> MacDonald
# Note: 'macdonald'.capitalize() returns Macdonald, not MacDonald.

# def old_macdonald(name: str):
#     # return name[0:3].capitalize() + name[3].upper() + name[4:]
#     return name[0:3].capitalize() + name[3:].capitalize()

# print(old_macdonald('macdonald')) # MacDonald
# print(old_macdonald('macmahon')) # MacMahon


# 8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False

# def spy_game(list_of_ints):
#     pattern = [0, 0, 7]
#     for num in list_of_ints:
#         if num == pattern[0]:
#             pattern.pop(0)
#         if not pattern:
#             return True
#     return False


# print(spy_game([1, 2, 4, 0, 0, 7, 5])) # True
# print(spy_game([1, 0, 2, 4, 0, 5, 7])) # True
# print(spy_game([1, 7, 2, 0, 4, 5, 0])) # False


# def spy_game(list_of_ints):
#     pattern = [0, 0, 7]
#     pattern_index = 0
#     for num in list_of_ints:
#         if num == pattern[pattern_index]:
#             pattern_index += 1
#         if pattern_index == len(pattern):
#             return True
#     return False


# print(spy_game([1, 2, 4, 0, 0, 7, 5])) # True
# print(spy_game([1, 0, 2, 4, 0, 5, 7])) # True
# print(spy_game([1, 7, 2, 0, 4, 5, 0])) # False


# def spy_game(list_of_ints):
#     pattern = [0, 0, 7]
#     filtered_list_of_ints = [num for num in list_of_ints if num in [0, 7]]
#     for i in range(len(filtered_list_of_ints) - 2):
#         sublist = filtered_list_of_ints[i:i+len(pattern)]
#         if sublist == pattern:
#             return True
#     return False


# print(spy_game([1, 2, 4, 0, 0, 7, 5])) # True
# print(spy_game([1, 0, 2, 4, 0, 5, 7])) # True
# print(spy_game([1, 7, 2, 0, 4, 5, 0])) # False
# print(spy_game([1, 7, 2, 0, 4, 5, 0, 9, 2, 29, 0, 2, 9, 10, 7])) # True

# [1, 2, 4, 0, 0, 7, 5]  # -> [0, 0, 7]
# [1, 0, 2, 4, 0, 5, 7]  # -> [0, 0, 7]
# [1, 7, 2, 0, 4, 5, 0]  # -> [7, 0, 0]
# [1, 7, 2, 0, 4, 5, 0, 9, 2, 29, 0, 2, 9, 10, 7]  # -> [7, 0, 0, 0, 7]



# def filter_list(list_of_ints):
#     filtered_list = []
#     for num in list_of_ints:
#         if num == 0 or num == 7:
#             filtered_list.append(num)
#     return filtered_list


# print(filter_list([9, 39, 28, 1, 0, 4, 8, 0, 2, 4, 7]))  # [0, 0, 7]
# print(filter_list([9, 39, 28, 1, 0]))  # [0]

# def filter_list(list_of_ints):
#     return [num for num in list_of_ints if num in [0, 7]]
#     # return [num for num in list_of_ints if num == 0 or num == 7]


# print(filter_list([9, 39, 28, 1, 0, 4, 8, 0, 2, 4, 7]))  # [0, 0, 7]
# print(filter_list([9, 39, 28, 1, 0]))  # [0]



# 9. Write a function vol(radius) that computes the volume of a sphere given its radius.



# def vol(radius):
#     return (4/3) * (22/7) * (radius ** 3)

# print(vol(5))


# import math
# def vol(radius):
#     return (4/3) * math.pi * (radius ** 3)


# print(vol(5))

# 10. Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).

# def range_check(num, low, high):
#     # return low <= num <= high
#     # return num >= low and num <= high
#     return num in range(low, high+1)

# print(range_check(6, 1, 10))  # True
# print(range_check(1, 1, 10))  # True
# print(range_check(10, 1, 10))  # True
# print(range_check(10, 20, 98))  # False


# 11. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.

# 12. Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.


# 13. Write a function multiply(list_items) to multiply all the numbers in a list.
# Sample List: [1, 2, 3, -4]
# Expected output: -24

# def multiply(list_items):
#     result = 1
#     for num in list_items:
#         result *= num
#     return result

# print(multiply([1, 2, 3, -4]))

# 14. Write a function is_pangram(text) to check whether a string is a pangram or not. 
# Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# least once. For example: “The quick brown fox jumps over the lazy dog”.
# Hint: Import and use the string module.

# def is_pangram(text: str):
#     text = text.upper()
#     # alphabets = [chr(num) for num in range(97, 123)]
#     alphabets = [chr(num) for num in range(65, 91)]
#     for alphabet in alphabets:
#         if alphabet not in text:
#             return False
#     return True

# def is_pangram(text: str):
#     text = text.upper()
#     alphabets = [chr(num) for num in range(65, 91)]
#     return all(letter in text for letter in alphabets)


# def is_pangram(text: str):
#     text = text.upper()
#     text = set(text)
#     alphabets = {chr(num) for num in range(65, 91)}
#     # return alphabets.issubset(text)
#     return alphabets <= text




# text1 = "Pack my box with five dozen liquor jugs!"
# print(is_pangram(text1))
# text2 = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(text2))
# text3 = "Go, lazy fat vixen; be shrewd, jump quick."
# print(is_pangram(text3))
# text4 = "This is not a pangram"
# print(is_pangram(text4))


# 15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# other. a word, phrase, or name formed by rearranging the letters of another, such as
# spar, formed from rasp.
# bcrypt
# hashlib

# def are_anagrams(s1, s2):
#     s1, s2 = set(s1.lower().replace(" ", "")), set(s2.lower().replace(" ", ""))
#     return s1 == s2


# def are_anagrams(s1, s2):
#     s1, s2 = s1.lower().replace(" ", ""), s2.lower().replace(" ", "")
#     return sorted(s1) == sorted(s2)


# def are_anagrams(s1: str, s2: str):
#     s1, s2 = s1.lower().replace(" ", ""), s2.lower().replace(" ", "")
#     l1 = list(s1)
#     l1.sort()
#     l2 = list(s2)
#     l2.sort()
#     return l1 == l2

# print(are_anagrams("Eleven plus two", "twelve plus one"))
# # elevenplustwo -> twelveplusone
# print(are_anagrams("angel", "angle"))
# print(are_anagrams("spar", "rasp"))
# print(are_anagrams("A Gentle Man", "Elegant man"))
# print(are_anagrams("I am Lord Voldemort", "Tom Marvolo Riddle"))
# print(are_anagrams("Raps", "Spoon"))  # False



# 16. 	Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# (BMI) given weight in kilograms and height in meters.

# def calculate_bmi(weight, height):
#     if weight < 0 or height < 0:
#         return "Invalid weight or height entered. They must be positive"
#     return weight / (height ** 2)


# def check_bmi_category(weight, height):
#     if weight < 0 or height < 0:
#         return "Invalid weight or height entered. They must be positive"
    
#     bmi = calculate_bmi(weight, height)
#     if bmi < 18.5:
#         return "You are underweight"
#     if 18.5 <= bmi <= 24.9:
#         return "Your weight is normal"
#     if 25.0 <= bmi <= 29.9:
#         return "You are overweight"
#     return "You are obese"


# print(check_bmi_category(65, 1.75))
# print(check_bmi_category(400, 1.75))
# print(check_bmi_category(35, 1.75))


# 17. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# simple interest given principal amount, interest rate, and time (in years).
# ====================================ASSIGNMENT 2===========================================