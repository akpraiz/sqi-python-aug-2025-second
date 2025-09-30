# Create a tuple containing the following streaming services in order:
# Netflix, Amazon Prime, Hulu, Disney Plus, UEFA TV, AppleTV

# streaming_services = {"Netflix", "Amazon Prime", "Hulu", "Disney Plus", "UEFA TV", "AppleTV"}

# for streaming_platform in streaming_services:
#     print(streaming_platform)

# Count all the even numbers from 23 to 55.

# for even_num in range(23, 55):
#     if even_num % 2 == 0:
#         print(even_num)

# for even_num in range(23, 55) % 2 == 0:
#     print(even_num)

# streaming_services = {"Netflix", "Amazon Prime", "Hulu", "Disney Plus", "UEFA TV", "AppleTV"}

# for index, streaming_service in enumerate(streaming_services):
#     print(f"{index + 1}. {streaming_service}")

# word = input("Enter any word: ").strip().lower()

# 1. Give me every body of water except "river"
# bodies_of_water = ["streams", "ocean", "river", "lagoon", "sea", "lake" "pond"]
# body_of_water = ["river"]
# bodies_of_water_except_river = [body for body in bodies_of_water if body not in "river"]

# print(bodies_of_water_except_river)

# 2. [False, True, True, False, True, True, True] - do the bodies of water have 5 or less chars?

# bodies_of_water_with_more_than_5_chars = [len(body) <=5 for body in bodies_of_water]

# print(bodies_of_water_with_more_than_5_chars)

# things_that_move_in_the_air = ["birds", "rocket", "aeroplane","witches", "chopper", "jet", "drone"]
# dic_of_things_that_moves_in_the_air = {things: things.count("e") for things in things_that_move_in_the_air}
# print(dic_of_things_that_moves_in_the_air)



# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
# digits = [1, 2, 3, 4, 5]


# square_of_digits = [digit ** 2 for digit in digits]
# print(square_of_digits)


# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
names = ["John", "Sara", "Mike", "Amanda"]

names_with_a = [name for name in names if name.lower().count("a")]
print(names_with_a)


# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
# values = [5, 12, 3, 18, 7]
# values_bool = [value > 10 for value in values]
# print(values_bool)

# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
# animals = ["dog", "cat", "lion", "tiger"]
# char_animals = [animal[-1] for animal in animals]
# print(char_animals)


# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
# values = [5, 12, 3, 18, 7]
# num_values = all(value > 10 for value in values)
# print(num_values)


# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
# names = ["John", "Sara", "Mike", "Amanda"]
# all_names = all(name for name in names)
# print(all_names)

# 7. Get only the numbers that are divisible by 3 between 12 to 52
# numbers = [num for num in range(12, 52) if num % 3 == 0]
# print(numbers)
