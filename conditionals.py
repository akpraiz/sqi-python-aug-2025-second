# is_raining = True

# if is_raining:
#     print("Carry an umbrella")
# else:
#     print("No need for an umbrella")



# num1 = 2
# num2 = 2

# if num1 > num2:
#     print("num1 is greater")
# else:
#     print("num2 is greater or equal to num1")


# Ask the user for a number
# Print "It is even" if the number is even
# otherwise, print "it is odd"

# number = int(input("Enter a number: "))
# is_even = number % 2 == 0
# if is_even:
#     print("It is even")
# else:
#     print("It is odd")


# num1 = 12
# num2 = 102

# if num1 > num2:
#     print("num1 is greater")
# elif num1 < num2:
#     print("num2 is greater")
# else:
#     print("num1 and num2 are equal")

 

# word = input("Enter a word: ")
# if word.lower().startswith("a"):
#     print(f"The word '{word}' starts with a")
# else:
#     print(f"The word '{word}' does not start with a")


# word = input("Enter a word: ").strip()

# if word[0].lower() == "a":
#     print(f"The word '{word}' starts with a")
# else:
#     print(f"The word '{word}' does not start with a")


# Ask the user for a sentence
# if all the characters are lowercase, print "Everything is in lowercase"
# otherwise, print "Not everything is in lowercase"


# sentence = input("Enter a sentence: ").strip()
# if sentence.islower():
#     print("Everything is in lowercase")
# else:
#     print("Not everything is in lowercase")


# If the temp is between 0 and 30, "It is cold outside"
# If the temp is between 31 and 59 "It is warm outside"
# If the temp is greater than or equal to 60, "It is hot outside"

# temp = int(input("Enter the temperature: "))

# if temp < 0:
#     print("It is freezing")
# elif 0 <= temp <= 30:
#     print("It is cold outside")
# elif 31 <= temp <= 100:
#     print("It is warm outside")
# else:
#     print("Invalid temp entered")
#     # raise ValueError("Invalid temp entered")


# Ask the user for their score and tell them their grade
# If their score is less than 30 and greater than or eqaul to 0, print "F"
# if their score is equal to or greater than 30 and less than or equal to 59, print "C"
# If their score is 60 or greater than 60 and less than or equal to 100, print "A"

# score = int(input("Enter your score: "))

# if 0 <= score < 30:
#     print("F")
# elif 30 <= score <= 59:
#     print("C")
# elif 60 <= score <= 100:
#     print("A")
# else:
#     print("Invalid score")




# husband = None
# husband = "James"


# if husband is None:
#     print("No husband")
# else:
#     print("Has husband")

# husband = "Ayo"
# husband = ""

# if husband:
#     print("Husband has a name")
# else:
#     print("Husband does not have a name")


# name = input("What is your name? ").strip()
# name = input("What is your name? ")

# if name:
#     print(f"Good morning, {name}!")
# else:
#     print(f"Good morning, Anonymous!")


# name = input("What is your name? ").strip()

# if name: print(f"Good morning, {name}!")
# else: print(f"Good morning, Anonymous!")


# is_male = False
# print("He" if is_male else "She")
# print("He") if is_male else print("She")


# is_male = False
# pronoun = "He" if is_male else "She"
# print(pronoun)


# is_male = False

# if is_male:
#     print("He")
# else:
#     print("She")


# is_male = False
# if is_male:
#     pronoun = "He"
# else:
#     pronoun = "She"

# print(pronoun)


# has_umbrella = True
# has_raincoat = True

# # If they have an umbrella or they have a raincoat, print "You are protected from the rain"
# # If the person has an umbrella and has a raincoat, print "You have double protection from the rain"
# # If they have none, print "You are NOT protected from the rain"

# if has_umbrella and has_raincoat:
#     print("You have double protection from the rain")
# elif has_umbrella or has_raincoat:
#     print("You are protected from the rain")
# else:
#     print('you are NOT protected form the rain')

# has_umbrella = False
# has_raincoat = True


# if has_umbrella:
#     print("You are protected from the rain")
# elif has_raincoat:
#     print("You are protected from the rain")
# elif has_umbrella and has_raincoat:
#     print("You have double protection from the rain")
# else:
#     print("You are NOT protected form the rain")



# name = input("What is your name? ").strip()

# if not name:
#     print("You must enter a name")


# students = ["Praise", "Maryam", "John", "Ayomide"]
# students = [""]

# if students:
#     print("there are students in the class")
# else:
#     print("there are no students in the class")



# is_male = False
# age = 21


# if is_male:
#     if age >= 18:
#         print("You can vote")
#     else:
#         print("You cannot vote")
# else:
#     print("Women do not have the right to vote")
    


# import random

# genders = [
#     "Male",
#     "Female",
#     "Transgender Male",
#     "Transgender Female",
#     "Non-binary",
#     "Genderqueer",
#     "Genderfluid",
#     "Agender",
#     "Bigender",
#     "Two-Spirit",
#     "Demiboy",
#     "Demigirl",
#     "Androgynous",
#     "Intersex"
# ]

# gender = random.choice(genders)

# print(gender)

# age = 12


# if age < 18:
#     if gender == "Male":
#         print("You are a young boy.")
#     elif gender == "Female":
#         print("You are a young girl.")
#     elif gender == "Non-binary":
#         print("You are a young non-binary person.")
#     else:
#         print(f"You are young and identify as {gender}.")
# elif 18 <= age <= 40:
#     if gender == "Male":
#         print("You are an adult man.")
#     elif gender == "Female":
#         print("You are an adult woman.")
#     elif gender == "Non-binary":
#         print("You are an adult non-binary person.")
#     else:
#         print(f"You are an adult and identify as {gender}.")
# else:  # age > 40
#     if gender == "Male":
#         print("You are a mature man.")
#     elif gender == "Female":
#         print("You are a mature woman.")
#     elif gender == "Non-binary":
#         print("You are a mature non-binary person.")
#     else:
#         print(f"You are mature and identify as {gender}.")



# is_female = True

# if is_female:
#     # I will write something here
#     pass
# print("End of file")
        


# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".

# mode = input("Enter a mode, either manual, automatic or off: ").strip().lower()

# if mode == "manual":
#     print("Manaul mode activated")
# elif mode == "automatic":
#     print("Automatic mode activated")
# elif mode == "off":
#     print("System is off")
# else:
#     print("Invalid mode")



# mode = input("Enter a mode, either manual, automatic or off: ").strip().lower()

# if mode == "manual" or mode == "automatic":
#     print(f"{mode} mode activated")
# elif mode == "off":
#     print("System is off")
# else:
#     print("Invalid mode")


# Collect word1, word2 and word3 as comma separated inputs from the user

# hi, hello, hey


# word1, word2, word3 = input("Enter three words separated by commas: ").strip().split(", ")

# print(word1)
# print(word2)
# print(word3)


