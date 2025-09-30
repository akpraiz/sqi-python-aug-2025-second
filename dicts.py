#                  MUTABLE               INDEXED           ORDERED             ALLOWS DUPLICATES
# List              Yes                    Yes               Yes                        Yes
# Tuple             No                     Yes               Yes                        Yes
# Set               Yes                    No                No                         No
# Dictionaries      Yes              Yes, but with keys Yes (but in recent versions)    Allow duplicate values, but not duplicate keys




# praise = {"name": "Akande Praise", "age": 12, "is_male": True, "complexion": "light"}

# praise = ["Akande Praise", 12, True, "light"]

# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615", 0:"zero"}

# print(phone_book["Ife"])
# print(phone_book["Damilola"])
# print(phone_book[0])
# print(phone_book)


# praise = {"name": "Akande Praise", "age": 12, "favorite_num": 12, "is_male": True, "name": "Olawumi Ayomide", "complexion": "light"}
# print(praise)

# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615", 0:"zero"}
# phone_book["Damilola"] = "07063457610"
# print(phone_book)
# phone_book["Ayomide"] = "08147882614"
# print(phone_book)

# phone_book["Sam"] = "08012378000"
# print(phone_book)

# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615", 0:"zero"}



# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615"}
# # del phone_book["tefv3dbhnxje3k"]  # keyError
# del phone_book["Damilola"]  # keyError
# print(phone_book)

# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615"}
# print("Ife" in phone_book)



# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615"}
# print(phone_book.keys())  # dict_keys
# print(list(phone_book.keys())[0])  # Sam

# print(phone_book.values())  # dict_values
# print(list(phone_book.values())[1])  # dict_values

# print(phone_book.items())  # dict_items - looks like a list of tuples where tuple[0] is the key, and tuple[1] is the 

# print("08169762937" in phone_book.values())


# phone_book = [
#     {"name": "Sam", "phone": "08025538654"},
#     {"name": "Sam", "phone": "08021238634"}
# ]
# print(phone_book[0]["phone"])
# print(phone_book[1]["phone"])

# phone_book = {"Sam": ["08025538654", "08021238634"], "Ife": ["08169762937", "09030556519"], "Damilola": ["07063457615", "0908906723"]}
# print(phone_book["Sam"][1])



# yoruba_translator = {
#     "book": "iwe",
#     "snake": "ejo",
#     "tree": "igi",
#     "shoe": "bata",
#     "broom": "igbale",
#     "get_up": "dide"
# }

# print(yoruba_translator["snake"])
# print(yoruba_translator["get_up"])





# Create a dictionary called student with the following keys: 
# "full_name", "age", "dept", "current_level", "gpa", "course", "is_full_time"
# provide values for the keys and do the following:
# 1. Add a new key "matric_no" with a value to the student dict
# 2. Change the value of the "gpa" key to 5.0
# 3. Remove the age from the student dict
# 4. Check if "dept" is in the dict
# 5. Check if "Data Science" is a value in the dict
# 6. Print out a LIST of the keys of the dict
# 7. Print out the first value in the dict without using the key "full_name"


# student = {"full_name": "Maryam Aleshinloye", "age": 29, "dept": "Artificial Intelligence", "current_level": "Python", "gpa": 4.5, "course": "Artificial Intelligence", "is_full_time": True}

# student["matric_no"] = "20256689"
# student["gpa"] = 5.0

# del student["age"]

# print("dept" in student)

# print("Data Science" in student.values())

# print(list(student.keys()))

# print(list(student.values())[0])


# student = {"full_name": "Maryam Aleshinloye", "age": 29, "dept": "Artificial Intelligence", "current_level": "Python", "gpa": 4.5, "course": "Artificial Intelligence", "is_full_time": True}

# print(student["dept"])
# print(student.get("dept"))

# print(student["department"])  # KeyError
# print(student.get("department"))  # None
# print(student.get("dept", "Does not exist"))
# print(student.get("department", "Does not exist"))


# student = {"full_name": "Maryam Aleshinloye", "age": 29, "dept": "Artificial Intelligence", "current_level": "Python", "gpa": 4.5, "course": "Artificial Intelligence", "is_full_time": True}

# print(student.setdefault("full_name"))
# print(student.setdefault("name"))
# print(student.setdefault("name", "Anonymous"))
# print(student)



# -------------------------------------UPDATE DICT----------------------------------------------
# Method 1: square bracket notation
# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }

# ife_dream_car["model"] = "Model X"
# ife_dream_car["color"] = "silver"

# print(ife_dream_car)


# Method 2: .update with dict

# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }
# ife_dream_car.update({'color': "silver"})
# ife_dream_car.update({'color': "silver", "year": 2000})
# ife_dream_car.update({'color': "silver", "year": 2000, "is fast": True})
# print(ife_dream_car)



# Method 3: .update with kwargs - keyword arguments
# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }

# ife_dream_car.update(color="silver", year=2000, is_fast=True)
# print(ife_dream_car)

# -------------------------------------UPDATE DICT----------------------------------------------



# -------------------------------------REMOVE FROM A DICT----------------------------------------------
# Method 1: using del keyword
# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }

# del ife_dream_car["is_eletric"]
# print(ife_dream_car)


# Method 2: using the .pop()
# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }

# popped = ife_dream_car.pop("is_eletric")
# print("popped:", popped)
# print(ife_dream_car)


# Method 3: using the .popitem()
# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }

# popped = ife_dream_car.popitem()
# print("popped:", popped)
# popped = ife_dream_car.popitem()
# print("popped:", popped)
# popped = ife_dream_car.popitem()
# print("popped:", popped)
# popped = ife_dream_car.popitem()
# print("popped:", popped)
# popped = ife_dream_car.popitem()
# print("popped:", popped)
# print(ife_dream_car)
# -------------------------------------REMOVE FROM A DICT----------------------------------------------





# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025,
#     (12,3, 4): "etfdybhmkx",
#     123: "one hundred and twenty three",
# }
# print(len(ife_dream_car))
# print(type(ife_dream_car))


# my_list = [1, 2, 3, 4, 5]
# print(dict(my_list))
# my_data = [(1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five")]
# my_data = [[1, "one"], [2, "two"], [3, "three"], [4, "four"], [5, "five"]]
# my_data = ([1, "one"], [2, "two"], [3, "three"], [4, "four"], [5, "five"])
# print(dict(my_data))


# my_data = dict(one=1, two=2, three=3, four=4, five=5)
# print(my_data)



# data = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# data.clear()
# print(data)


# empty_dict = {}
# print(type(empty_dict))

# empty_set = set()
# print(type(empty_set))


# my_set = {}


# -------------------------------------COPY A DICT----------------------------------------------

# import copy

# sam_laptop = {
#     "brand": "Mac",
#     "ram": 8,
#     "manufacturer": "Apple",
#     "battery": 90,
#     "configuration": [8, 256]
# }

# # duplicate = sam_laptop.copy()
# duplicate = copy.deepcopy(sam_laptop)

# duplicate["configuration"][0] = 16

# print(sam_laptop)
# print(duplicate)

# -------------------------------------COPY A DICT----------------------------------------------
