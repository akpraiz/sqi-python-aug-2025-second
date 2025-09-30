# 1. Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# length, width, and height, and print each variable.
# dimensions = 10, 20, 30
# length, width, height = dimensions
# print("length: ", length)
# print("width: ", width)
# print("height: ", height)

# 2. Given the tuple coordinates:
# coordinates = (1.5, 2.5, 3.5)
# Unpack the tuple into variables x, y, and z, and print the value of y.
# coordinates = (1.5, 2.5, 3.5)
# x, y, z = coordinates
# print("y: ", y)

# 3. Create a tuple called person with values ("John", 25, "Engineer"). Unpack the values into variables name, age, and profession, and print the value of profession.

# person = ("John", 25, "Engineer")
# name, age, profession = person
# print("Profession: ", profession)

# 4. Given the nested tuple data:
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# Unpack the first element of data into variables student1 and student2, and print student2.
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# (student1, student2), (_, _), (_, _) = data
# print("Student2 is", student2)

# 5. Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two values into variables color1 and color2, and print both variables.
# colors = ("red", "green", "blue", "yellow")
# color1, color2, _, _ = colors
# print("color1:", color1)
# print("color2:", color2)

# 6. Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, (age, position), (first_department, second_department) = record
# print("Age:", age)
# print("Department:", first_department)

# 7. Create a tuple called triplet with values ("one", "two", "three"). Unpack the tuple into variables and print the value of the second variable.
# triplet = ("one", "two", "three")
# num_1, num_2, num_3 = triplet
# print("Second variable:", num_2)

# 8. Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# product_ID, (category, price), (manufacture_day, manufacture_month, manufacture_year) = info
# print("Category:", category)
# print("Manufacture year:", manufacture_year)

# 9. Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). 
# Unpack the nested tuples into individual variables and print the second value of the third tuple.
# nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
# first_tuple, second_tuple, third_tuple = nested_tuple
# print(third_tuple[1])

# 10. Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.
# inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# (fruit_1, quantity_1), (fruit_2, quantity_2), (fruit_3, quantity_3) = inventory
# print("Quantity of bananas:", quantity_2)

student = {"full name": "Cyril Stober", "age": 59, "dept": "Mass Communitcation", "current_level": "500", "gpa": 4.97, "course": "GNS101", "is_full_time": True}
# 1. Add a new key "matric_no" with a value to the student dict
# student["matric_no"] = "145939"
# print(student)

# 2. Change the value of the "gpa" key to 5.0
# student["gpa"] = 5.0
# print(student)

# 3. Remove the age from the student dict
# del student["age"]
# print(student)

# 4. Check if "dept" is in the dict
# print("dept" in student)

# 5. Check if "Data Science" is a value in the dict
# print("Data Science" in student.values())

# 6. Print out a LIST of the keys of the dict
# print(list(student.keys()))

# 7. Print out the first value in the dict without using the key "full_name"
# print(list(student.values())[0])

