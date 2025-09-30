# Write a function called mutiply_two_nums that accepts two numbers first_num and second_num and prints the product of the number
# After, call the function

# def mutiply_two_nums(first_num, second_num):
#     print(f"The product of {first_num} and {second_num} is {first_num * second_num}")

# mutiply_two_nums(9, 10)

# Write a function is_even that accepts a parameter num and returns True if num is even, otherwise, it returns False.

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     if num % 2 == 1:
#         return False

# print(is_even(4))

# Write a function called starts_with_s that accepts a parameter called word and returns True if the word starts with s, regardless of case, otherwise, it returns False

# def starts_with_s(word: str):
#     return word.lower().startswith("s")


# print(starts_with_s("Sun"))

# Assignment

#  1. Create a function called turn_to_upper(names) that takes in a list of names, and returns a list of names uppercased
# after, print the result of the function.
# For example, if names is ["Winifred", "Wilfred", "Justin", "Augusta"], the result would be [ "WINIFRED", "WILFRED", "JUSTIN", "AUGUSTA"]

# def turn_to_upper(names: list):
#     return [name.upper() for name in names]

# print(turn_to_upper(["praise", "tolu"]))


# 2. Create a function called get_middle_name that accepts one paramter `name_dict` that takes in a dictionary with keys
#  "first", "middle", and "last".
# The function should return only the middle name.
# For example, if name_dict is {"first": "Tola", "middle": "James", "last": "Akin"}, then the result would be "James".
#  Another example is if name_dict is {"middle": "Chioma", "first": "Ada", "last": "Okeke"}, the result would be "Chioma".

# def get_middle_name(name_dict: dict):
#     return name_dict ["middle"]

# print(get_middle_name({"first": "Tola", "middle": "James", "last": "Akin"}))

# 3. Create a function called reverse_string that accepts a string as input and returns the string reversed.
# For example, if the string is "Python", the result would be "nohtyP".
# def reverse_string(word: str):
#     return word [::-1]
# print(reverse_string("python"))


# 4. Create a function called count_vowels that accepts a string and returns the number of vowels (a, e, i, o, u) in it.
# For example, if the string is "beautiful", the result would be 5.


# 5. Create a function called even_numbers that takes in a list of integers and returns a new list containing only the even numbers.
# For example, if the list is [1, 2, 3, 4, 5, 6], the result would be [2, 4, 6].

# 6. Create a function called find_max that takes in a list of numbers and returns the maximum number in the list.
# For example, if the list is [12, 45, 3, 67, 23], the result would be 67.

# 7. Create a function called sum_dict_values that takes in a dictionary with numeric values and returns the sum of all the values.
# For example, if the dictionary is {"a": 10, "b": 20, "c": 5}, the result would be 35.

# 8. Create a function called word_lengths that takes in a list of words and returns a dictionary where each word is a key and its length is the value.
# For example, if the list is ["apple", "banana", "cherry"], the result would be {"apple": 5, "banana": 6, "cherry": 6}.

# 9. Create a function called is_palindrome that takes in a string and returns True if the string is a palindrome (same forwards and backwards), otherwise False.
# For example, if the string is "level", the result would be True. If the string is "hello", the result would be False.

# 10. Create a function called merge_lists that takes in two lists and returns one combined list without duplicates.
# For example, if list1 = [1, 2, 3] and list2 = [3, 4, 5], the result would be [1, 2, 3, 4, 5].

# 11. Create a function called multiply_numbers(a, b=2) that multiplies two numbers.
# If the second number is not provided, it should default to 2.
# Example 1: multiply_numbers(5) → 10
# Example 2: multiply_numbers(5, 3) → 15

# 12. Create a function called greet_user(first_name, last_name="") that returns a greeting string.
# If last_name is not provided, it should only greet with the first name.
# Example 1: greet_user("Ada") → "Hello, Ada!"
# Example 2: greet_user("Tola", "Akin") → "Hello, Tola Akin!"

# 13. Create a function called power(base, exponent=2) that raises the base to the power of the exponent.
# The exponent should default to 2 (square).
# Example 1: power(4) → 16
# Example 2: power(2, 3) → 8

# 14. Create a function called format_full_name(first, middle="", last="") that returns the full name as a single string.
# If middle or last is not provided, it should still work correctly.
# Example 1: format_full_name("John", "Paul", "Smith") → "John Paul Smith"
# Example 2: format_full_name("Ada", last="Okeke") → "Ada Okeke"

# 15. Create a function called calculate_discount(price, discount=10, tax=0) that calculates the final price after applying
# a discount (percentage) and then adding tax (percentage).
# Example 1: calculate_discount(100) → 90.0   (10% discount, no tax)
# Example 2: calculate_discount(200, discount=20, tax=5) → 168.0


# steps:
# 1. enter the function and the parameter
# # 2. enter the two word string
# def is_alliteration(two_word_string):
#     two_word_string = two_word_string.strip().lower()
#     two_word_string = two_word_string.split(" ")
#     word1, word2 = two_word_string
#     return word1[0] == word2[0]

# print(is_alliteration("lamella, level"))

# Assignment
# 5. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.

# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)

# print(lesser_of_two_evens(5, 7))

# 6. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False

# def is_alliteration(two_word_string: str):
#     words = two_word_string.lower().strip().split()
#     return words[0][0] == words[1][0]

# print(is_alliteration("Levelheaded llama"))
# print(is_alliteration("Crazy Kangaroo"))

# 7. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.

# def capitalize_positions(word: str, positions: list[int]):
#     word = word.strip()
#     result = ""
#     for i, char in enumerate(word):
#         if i in positions:
#             result += char.upper()
#         else:
#             result += char
#     return result

# print(capitalize_positions("macdonald", [0, 3])) 

# 8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False

# def spy_game(list_of_ints):
#     code = [0, 0, 7]   
#     for num in list_of_ints:
#         if num == code[0]:   
#             code.pop(0)      
#         if not code:         
#             return True
#     return False


# def spy_game(list_of_ints: int):
#     if list_of_ints in [0, 0, 7]:
#         return True

# print(spy_game([1, 2, 4, 0, 0, 7, 5]))

# def filter_list(list_of_ints):
#     list = [0, 0, 7]
#     for num in list:
#         if list[0] in list_of_ints
#         elif list[1] in list_of_ints
#         elif list[2] in list_of_ints
#         return True

# print(spy_game([1, 2, 4, 0, 0, 7, 5]))           

# 9. Write a function vol(radius) that computes the volume of a sphere given its radius.


# def vol(radius: float):
#     return (4/3) * 3.142 * (radius ** 3)

# print(vol(5))


# 10. Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).

# def range_check(num, low, high):
#     return low <= num <= high

# print(range_check(5, 2, 7))
# print(range_check(1, 2, 7))

# 11. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.
# def upper_lower(text: str):
#     upper_count = 0
#     lower_count = 0

#     for char in text:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
    
#     return {"upper": upper_count, "lower": lower_count}

# print(upper_lower("Hello World!"))


# 12. Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.
# def unique_list(list_items):
#     unique = []
#     for item in list_items:
#         if item not in unique:
#             unique.append(item)
#     return unique

# print(unique_list(["apple", "banana", "apple", "cherry", "banana"]))


#  13.	Write a function multiply(list_items) to multiply all the numbers in a list.
# 	Sample List: [1, 2, 3, -4]
# 	Expected output: -24

# def multiply(list_items):
#     result = 1
#     for num in list_items:
#         result *= num
#     return result

# print(multiply([1, 2, 3, -4])) 

#  14. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 
# 	Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# 	least once. For example: “The quick brown fox jumps over the lazy dog”.
# 	Hint: Import and use the string module.

# import string

# def is_pangram(text: str):
#     alphabet = set(string.ascii_lowercase)
#     return alphabet <= set(text.lower())

# print(is_pangram("The quick brown fox jumps over the lazy dog"))


#  15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# 	other. a word, phrase, or name formed by rearranging the letters of another, such as
# 	spar, formed from rasp.

# def are_anagrams(s1: str, s2: str):
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()
#     return sorted(s1) == sorted(s2)


# print(are_anagrams("Eleven plus two", "Twelve plus one"))        

#  16. 	Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# 	(BMI) given weight in kilograms and height in meters.

# def calculate_bmi(weight: float, height: float):
#     return round(weight / (height ** 2), 2)

# print(calculate_bmi(70, 1.75))  # 22.86 (Normal BMI)


#  17. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# 	simple interest given principal amount, interest rate, and time (in years).

# def calculate_simple_interest(principal: float, rate: float, time: float):
#     return (principal * rate * time) / 100

# print(calculate_simple_interest(1000, 5, 3))  # 150.0



# class Car:
#     def __init__(self, brand, model, year, horsepower, fuel_type):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.horsepower = horsepower
#         self.fuel_type = fuel_type

#     def car_info(self):
#         return f"This is a {self.year} {self.brand} {self.model} with {self.horsepower} HP running on {self.fuel_type}."
    
    
# toyota = Car("Toyota", "Corolla", "2009", "233", "PMS")
# honda = Car("Honda", "Civic", "2011", "263", "PMS")
# hyundai = Car("Hyundai", "Sonata", "2021", "453", "PMS")


# print(toyota.car_info())
# print(honda.car_info())
# print(hyundai.car_info())


# Assignment
# 3. Create a class called Student with the following attributes:
#    - name
#    - age
#    - grades (a list of integers)
#
#    The class should have two methods:
#    - average_grade(): returns the average of all grades
#    - is_passing(): returns True if the average grade is >= 50, otherwise False
#
#    After defining the class, create 2 different Student objects with different values.

# Example usage:
# s1 = Student("Alice", 20, [60, 75, 80, 90])
# s2 = Student("Bob", 19, [30, 40, 20, 45])

# print(s1.name, "average:", s1.average_grade(), "passing:", s1.is_passing())
# print(s2.name, "average:", s2.average_grade(), "passing:", s2.is_passing())

# Expected Output:
# Alice average: 76.25 passing: True
# Bob average: 33.75 passing: False

# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades

#     def average_grade(self):
#         return sum(self.grades) / len(self.grades) 
    
#     def is_passing(self):
#         return self.average_grade() >= 50


# s1 = Student("Alice", 20, [60, 75, 80, 90])
# s2 = Student("Bob", 19, [30, 40, 20, 45])

# print(s1.name, "average:", s1.average_grade(), "passing:", s1.is_passing())
# print(s2.name, "average:", s2.average_grade(), "passing:", s2.is_passing())



# 4. Create a class called Playlist with the following attributes:
#    - name
#    - songs (a list of strings)
#
#    The class should have three methods:
#    - add_song(song): adds a new song title to the playlist
#    - total_songs(): returns the total number of songs
#    - show_songs(): returns all song titles as a comma-separated string
#
#    After defining the class, create a Playlist and add a few songs.
# Example usage:
# pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
# pl.add_song("Lose Yourself")
# pl.add_song("Can't Hold Us")

# print(pl.name, "has", pl.total_songs(), "songs")
# print("Songs:", pl.show_songs())

# Expected Output:
# Workout Jams has 4 songs
# Songs: Eye of the Tiger, Stronger, Lose Yourself, Can't Hold Us

# class Playlist:
#     def __init__(self, name, songs):
#         self.name = name
#         self.songs = songs

#     def add_song(self, song: str):
#         self.songs.append(song)
    
#     def total_songs(self):
#         return len(self.songs)
    
#     def show_songs(self):
#         return ", ".join(self.songs)

# pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
# pl.add_song("Lose Yourself")
# pl.add_song("Can't Hold Us")

# print(pl.name, "has", pl.total_songs(), "songs")
# print("Songs:", pl.show_songs())

        

# 5. Create a class called ShoppingCart with the following attributes:
#    - owner
#    - items (a dictionary where keys are item names and values are prices)
#    The class should have three methods:
#    - add_item(item, price): adds the item with its price
#    - total_cost(): returns the sum of all prices
#    - most_expensive(): returns the item with the highest price
#
#    After defining the class, create a ShoppingCart and add multiple items.

# Example usage:
# cart = ShoppingCart("Alice", {})
# cart.add_item("Laptop", 1200)
# cart.add_item("Mouse", 25)
# cart.add_item("Keyboard", 100)
# cart.add_item("Monitor", 300)

# print("Total cost:", cart.total_cost())
# print("Most expensive item:", cart.most_expensive())

# Expected Output:
# Total cost: 1625
# Most expensive item: Laptop

# class ShoppingCart:
#     def __init__(self, owner, items):
#         self.owner = owner
#         self.items = items
    
    # def __str__(self):
    #     return f"{self.owner}"
    
#     def add_item(self, item, price):
#         self.items[item] = price

#     def total_cost(self):
#         return sum(self.items.values())
    
#     def most_expensive(self):
#         return max(self.items, key=self.items.get)

# cart = ShoppingCart("Alice", {})
# cart.add_item("Laptop", 1200)
# cart.add_item("Mouse", 25)
# cart.add_item("Keyboard", 100)
# cart.add_item("Monitor", 300)

# print("Total cost:", cart.total_cost())
# print("Most expensive item:", cart.most_expensive())
# print(cart)