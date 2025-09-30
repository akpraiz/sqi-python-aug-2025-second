# yam_and_egg_shopping_list = ["yam", "eggs", "groundnut oil", "atarodo", "tomato", "onions", "salt", "maggi", "curry", "veggies"]



# prime_nums = [2, 3, 5, 7, 11]

# print(prime_nums)

# print(yam_and_egg_shopping_list[0])
# print(yam_and_egg_shopping_list[0][0])

# my_list = ["bag", 1, "12", True, None, 90.23, False]

# print(yam_and_egg_shopping_list)


# yam_and_egg_shopping_list = ["yam", "eggs", "groundnut oil", "atarodo", "tomato", "onions", "salt", "maggi", "curry", "veggies"]
# print("before: ", yam_and_egg_shopping_list)
# yam_and_egg_shopping_list[3] = "tatashe"  # lists are mutable
# yam_and_egg_shopping_list.append("sardine")
# yam_and_egg_shopping_list.insert(1, "sardine")
# yam_and_egg_shopping_list.insert(5, "sardine")
# yam_and_egg_shopping_list.remove("onions")
# yam_and_egg_shopping_list.remove("THYME")
# print("tomato" in yam_and_egg_shopping_list)
# print("tomatoes" in yam_and_egg_shopping_list)
# print("after : ", yam_and_egg_shopping_list)


# Create a list called means_of_transport containing "plane", "ship", "train", "broom", "car" in this order.
# 1. Access and print the first item in the list
# 2. Access and print the last item in the list using positive indexing
# 3. Access and print the last item in the list using negative indexing
# 4. Add "feet" to the end of the list
# 5. Add canoe inbetween "ship" and "train"
# 6. Get rid of broom from the list
# 7. Check if "car" is in the list
# 8. Change "car" to "horse"



# name = "Edward"
# name[2] = "f"  # strings are immutable


# name = "Edward"
# name = name.upper()
# print(name)


# name = "Hullaballo"
# no_of_l = name.count("l")
# print(no_of_l)
# print(name.count("l"))

# list methods work in-place
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)

# my_list = [1, 2, 3]
# my_list = my_list.append(4)
# print(my_list)


# football_clubs = ["Chelsea", "Arsenal", "Manchester City", "Liverpool", "Barcelona"]  # ordered
# football_clubs = {"Chelsea", "Arsenal", "Manchester City", "Liverpool", "Barcelona"}  # unordered
# print(football_clubs)



# football_clubs = ["Chelsea", "Arsenal", "Manchester City", "Liverpool", "Barcelona"]  # indexed
# print(football_clubs[2])
# football_clubs = {"Chelsea", "Arsenal", "Manchester City", "Liverpool", "Barcelona"}  # unindexed
# print(football_clubs[2])


# football_clubs = ["Chelsea", "Arsenal", "Manchester City", "Liverpool", "Arsenal", "Barcelona"]  # allow duplicates
# football_clubs = {"Chelsea", "Arsenal", "Manchester City", "Liverpool", "Arsenal", "Barcelona"}  # do not allow duplicates
# print(football_clubs)


# means_of_transport = ["plane", "ship", "train", "broom", "car"]
# # print(means_of_transport[2])
# # print(means_of_transport[-3])
# # print(means_of_transport[:3])
# print("before:", means_of_transport)
# means_of_transport[1:4] = "helicopter"
# # means_of_transport[1:4] = ["helicopter"]
# # means_of_transport[1] = ["lorry"]
# # means_of_transport[1] = "lorry"
# print("after: ", means_of_transport)

# means_of_transport = ["plane", "ship", "train", "broom", "car"]
# print(len("".join(means_of_transport)))

# means_of_transport = ["plane", "ship", "train", "broom", "car"]
# print(len(means_of_transport))

# are_married = [False, True, True, False, False]
# print(len(are_married))
# means_of_transport = {"plane", "car", "ship", "train", "train", "broom", "car"}
# print(len(means_of_transport))


# means_of_transport = ["plane", "ship", "train", "broom", "car"]
# print(type(means_of_transport))


# cute_nums = (3, 9, 0, 2)
# cute_nums = list(cute_nums)
# print(cute_nums)
# print(type(cute_nums))



# cute_nums = (3, 9, 0, 2)
# cute_nums_list = list(cute_nums)
# print(cute_nums)
# print(cute_nums_list)

# cute_nums = (3, 9, 0, 2)
# print(list(cute_nums))
# print(type(cute_nums))  # tuple


# female_names = ["Deborah", "Maryam", "Esther", "Winifred", "Zainab", "Damilola"]
# other_female_names = ["Sarah", "Mary", "Ruth", "Vanessa"]

# female_names.append(other_female_names)  # maybe not what you want
# female_names.append("Sarah", "Mary", "Ruth", "Vanessa")  # wrong
# print(female_names)


# female_names.extend(other_female_names)  # wrong
# print(female_names)


# other_female_names.extend(female_names)
# print(other_female_names)
# print(female_names)

# female_names = ["Deborah", "Maryam", "Esther", "Winifred", "Zainab", "Damilola"]
# # other_female_names = ("Sarah", "Mary", "Ruth", "Vanessa")
# other_female_names = {"Sarah", "Mary", "Ruth", "Vanessa"}

# # female_names.extend(other_female_names)
# # other_female_names.extend(female_names)
# female_names.extend("Jennifer")
# print(female_names)

# -------------------------------REMOVING FROM A LIST-------------------------------


# Method 1: .remove()
# female_names = ["Deborah", "Maryam", "Esther", "Winifred", "Zainab", "Damilola"]
# print("before:", female_names)
# female_names.remove("Winifred")
# female_names.remove("Joy")  # ValueError
# print("after: ", female_names)


# female_names = ["Deborah", "Maryam", "Winifred", "Esther", "Winifred", "Zainab", "Damilola"]
# print("before:", female_names)
# female_names.remove("Winifred")
# print("after: ", female_names)

# Method 2: del keyword

# female_names = ["Deborah", "Maryam", "Winifred", "Esther", "Winifred", "Zainab", "Damilola"]
# print("before:", female_names)
# del female_names[4]
# del female_names[100]  # IndexError
# print("after: ", female_names)


# Method 3: .pop()
 
# female_names = ["Deborah", "Maryam", "Winifred", "Esther", "Winifred", "Zainab", "Damilola"]
# print("before:", female_names)
# # female_names.pop()
# # female_names.pop(-3)
# # female_names.pop(4)
# popped_female_name = female_names.pop(1)
# print("popped_female_name: ", popped_female_name)

# print("after: ", female_names)



# keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("before:", keypad)
# # keypad.remove([1, 2, 3])
# # del keypad[0]  # correct
# # del keypad[0:2]
# # popped_row = keypad.pop(0)
# # print(popped_row)
# print("after: ", keypad)

# -------------------------------REMOVING FROM A LIST-------------------------------



# -------------------------------CLEARING A LIST-------------------------------

# sports = ["Basketball", "Soccer", 'Volleyball', "Tennis", "Football", "Cricket", "Wrestling"]
# print("before:", sports)
# # sports.clear()
# # sports = []
# print("after: ", sports)
# -------------------------------CLEARING A LIST-------------------------------



# -------------------------------SORTING A LIST-------------------------------
# sports = ["Basketball", "Soccer", 'Volleyball', "Tennis", "Football", "Cricket", "Wrestling"]
# sports = ["basketball", "Soccer", 'Volleyball', "Tennis", "Football", "Cricket", "Wrestling"]
# print("before:", sports)
# sports.sort()
# # sports.sort(reverse=True)
# print("after: ", sports)



# sports = ["basketball", "Soccer", 'Volley-ball', "Tennis", "Football", "Cricket", "Wrestling"]
# sports = "-".join(sports)
# print(sports)
# sports = sports.lower()
# sports = sports.split("-")
# sports.sort()
# print(sports)


# ages = [12, 89, 45, 26, 10]
# # ages = [12, 89, "hey", 45, "26", 10]  # TypeError
# print("before:", ages)
# ages.sort()
# # ages.sort(reverse=True)
# print("after: ", ages)


# sports = ["Basketball", "Soccer", 'Volleyball', "Tennis", "Football", "Cricket", "Wrestling"]
# sports = ["basketball", "Soccer", 'Volleyball', "Tennis", "Football", "Cricket", "Wrestling"]
# print("before:", sports)
# sports.sort(key=str.lower)
# print("after: ", sports)


# nums = [12, 78, 267, 790]
# print(max(nums))

# names = ["Sarah", "John", "Edward", "Mildred", "Ziphorah", "Oluwatomisin"]
# print(max(names))
# print(max(names, key=len))
# print(min(names, key=len))
# -------------------------------SORTING A LIST-------------------------------



# -------------------------------REVERSING A LIST-------------------------------

# names = ["Sarah", "John", "Edward", "Mildred", "Ziphorah", "Oluwatomisin"]
# print("before:", names)
# # names.reverse()
# names = names[::-1]
# print("after: ", names)

# -------------------------------REVERSING A LIST-------------------------------



# -------------------------------COPY A LIST-------------------------------

# names = ["Sarah", "John", "Edward", "Mildred", "Ziphorah", "Oluwatomisin"]
# print("names:", names)
# names_copy = names.copy()
# print(names is names_copy)
# print("names_copy: ", names)

# import copy

# names = ["Sarah", "John", "Edward", "Mildred", "Ziphorah", "Oluwatomisin"]
# print("names:", names)
# names_copy = copy.copy(names)
# print(names is names_copy)
# print("names_copy: ", names)


# import copy

# names = ["Sarah", "John", ["Edward", "Mildred"], "Ziphorah", "Oluwatomisin"]
# print("names:", names)
# names_copy = copy.deepcopy(names)
# print(names is names_copy)
# print("names_copy: ", names)

# -------------------------------COPY A LIST-------------------------------

# -------------------------------JOINING A LIST-------------------------------
# Method 1: .extend()
# female_names = ["Deborah", "Maryam", "Esther", "Winifred", "Zainab", "Damilola"]
# other_female_names = ["Sarah", "Mary", "Ruth", "Vanessa"]
# female_names.extend(other_female_names)
# print(female_names)

# Method 2: list concatenation
# female_names = ["Deborah", "Maryam", "Esther", "Winifred", "Zainab", "Damilola"]
# other_female_names = ["Sarah", "Mary", "Ruth", "Vanessa"]
# # all_female_names = female_names + other_female_names
# female_names = female_names + other_female_names
# print(female_names)
# -------------------------------JOINING A LIST-------------------------------

# -------------------------------NESTED LISTS-------------------------------
# Example:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][1] = matrix[0][0] + matrix[0][2]
# print(matrix)
# print(matrix[0])
# print(matrix[1])
# print(matrix[2])

# print(matrix[1][1])

# print(matrix[-2][-1])

# print(matrix[2][0])

# print(matrix[-3][-3])

# nested_list = [
#     ["Alice", "Bob"],
#     [10, 20, 30],
#     [True, False]
# ]

# print(nested_list[0][0][1:])
# print(nested_list[0][1][1])
# print(nested_list[1][0] + nested_list[1][-1])
# print(sum([nested_list[1][0], nested_list[1][-1]]))
# nested_list[0][0] = nested_list[0][0].upper()
# print(nested_list)
# -------------------------------NESTED LISTS-------------------------------


# -------------------------------ASSIGNMENT CORRECTION-------------------------------
# 3. Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7.
# items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(items[3:7])
# print(items[3:8])


# 4. Create a list called alphabets with items "a", "b", "c", ..., "z". 
# Print a slice from index -3 to the end.


# sentence = "I am at SQI this morning"
# print(list(sentence))
# print(sentence.split())


# import string

# letters = list(string.ascii_lowercase)
# print(letters)
# print(letters[-3:])


# 5. Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".

# grades = ["A", "B", "C", "D"]
# # ["A", "X", "D"]
# print(grades[1:3])
# # grades[1:3] = ["XYZ"]
# grades[1:3] = ["X"]
# print(grades)

# 11. Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.

# tuple_data = ("a", "b", "c")
# # tuple_data = "a", "b", "c"
# tuple_data = list(tuple_data)
# print(list(tuple_data))
# print(tuple_data)
# print(tuple_data)

# 19. Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.

# names = ["Zoe", "Alice", "Bob"]
# names.sort()
# print(names)

# 20. Create a list called ages with items 25, 35, 20. Sort the list in descending order.

# ages = [25, 35, 20]
# ages.sort(reverse=True)
# print(ages)

# 21. Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.

# import copy

# my_list = [1, 5, 980]
# dupliacte_my_list = my_list.copy()
# dupliacte_my_list = copy.copy(my_list)


# my_list = [51, 5, 980]
# my_list.sort()
# print(my_list)

# my_list = [51, 5, 980]
# my_list = sorted(my_list)
# print(my_list)


# name = "Elizabeth"
# name = sorted(name, key=str.lower)
# name = "".join(name)
# print(name)


# my_list = [51, 5, 980]
# my_list = list(reversed(my_list))
# print(my_list)


# 22. Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.

# numbers = [1, 2, 3, 4]
# numbers = list(reversed(numbers))
# print(numbers)

# numbers = [1, 2, 3, 4]
# numbers = numbers[::-1]
# print(numbers)

# numbers = [1, 2, 3, 4]
# numbers.reverse()
# print(numbers)



# 23. Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using
# slicing.

# letters = ["a", "b", "c", "d"]
# letters = letters[::-1]
# print(letters)

# -------------------------------ASSIGNMENT CORRECTION-------------------------------
