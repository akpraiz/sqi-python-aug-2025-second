# 1. Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".
# student = {"name": "John", "age": 20, "grade": "A"}
# print(student["name"])

# 2. Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
# product = {"name": "Laptop", "price": 999.99, "stock": 50}
# product["price"] = 899.99
# print(product)

# 3. Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
# employee = {"name": "Alice", "position": "Manager"}
# employee["salary"] = 50000
# print(employee)

# 4. Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
# inventory = {"apple": 10, "banana": 5, "orange": 8}
# del inventory["banana"]
# print(inventory)

# 5. Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
# person = {"name": "Bob", "age": 25, "city": "New York"}
# person_copy = person.copy()
# print(person_copy)

# 6. Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
# family = {
#   "child1" : [{"name": "Alice", "age": 16}],
#   "child2" : [{"name": "Paul", "age": 18}],
#   "child3" : [{"name": "Peter", "age": 20}]
# }
# print(family["child2"]["age"])

# 7. Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
# car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
# print(car["model"])

# 8. Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
# settings = {"volume": 50, "brightness": 75, "language": "English"}
# settings["language"] = "Spanish"
# print(settings)

# 9. Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
# scores = {"math": 90, "science": 85, "english": 88}
# del scores["science"]
# print(scores)

# 10. Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
# menu = {"starter": "Soup", "main_course": "Steak", "dessert": "Ice Cream"}
# print(menu["appetizer"])

# 11. Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
# config = {"theme": "dark", "language": "English", "timezone": "UTC"}
# config.clear()
# print(config)

#  12.	Create a dictionary called `phone_book` with keys "Alice", "Bob", and 
# "Charlie", and corresponding phone numbers as values. Print the number of 
# items in the dictionary.
# phone_book = {"Alice": 7060495939, "Bob": 9010203040, "Charlie": 8103298493}
# print(len(phone_book))

#  13. Create a dictionary called `grades` with keys "math", "science", and "history", 
# and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.
# grades = {"math": "A", "science": "B", "history": "C"}
# print(grades.keys())

#  14. 	Create a dictionary called `employee` with keys "name", "position", and 
# "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# of all the values in the dictionary.
# employee = {"name": "David", "position": "Engineer", "salary": 70000}
# print(list(employee.values()))

#  15. 	Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# key-value pairs in the dictionary.
# game = {"title": "Minecraft", "genre": "Sandbox", "rating": 4.5}
# print(list(game.values()))


# Assignment 2
# Q1. Given this dictionary, change the "math" score to 95.
# student = {
#     "name": "Alice",
#     "scores": {"math": 80, "english": 85}
# }
# student["scores"]["english"] = 95
# print(student)


# Expected Output:
# {'name': 'Alice', 'scores': {'math': 95, 'english': 85}}


# Q2. Add a new subject "science" with score 90 inside "scores".
# student = {
#     "name": "Alice",
#     "scores": {"math": 80, "english": 85}
# }
# student["scores"]["science"] = 90 
# print(student)

# Expected Output:
# {'name': 'Alice', 'scores': {'math': 80, 'english': 85, 'science': 90}}

# Q3. Change the author's name of "Python 101" to "Mike".
# library = {
#     "Python 101": {"author": "Tom", "year": 2020},
#     "Data Science": {"author": "Jane", "year": 2021}
# }

# library["Python 101"]["author"] = "Mike"
# print(library)

# Expected Output:
# {'Python 101': {'author': 'Mike', 'year': 2020}, 'Data Science': {'author': 'Jane', 'year': 2021}}


# Q4. Add a new key "publisher" = "O'Reilly" to "Data Science".
# library = {
#     "Python 101": {"author": "Tom", "year": 2020},
#     "Data Science": {"author": "Jane", "year": 2021}
# }
# library["Data Science"]["publisher"] = "O'Reilly"
# print(library)

# Expected Output:
# {'Python 101': {'author': 'Tom', 'year': 2020}, 'Data Science': {'author': 'Jane', 'year': 2021, 'publisher': "O'Reilly"}}

# Q5. In this dictionary, add a new phone number "work": "555-999" for Alice.
# contacts = {
#     "Alice": {"home": "555-123", "mobile": "555-456"},
#     "Bob": {"home": "555-789"}
# }
# contacts["Alice"]["work"] = "555-999"
# print(contacts)

# Expected Output:
# {'Alice': {'home': '555-123', 'mobile': '555-456', 'work': '555-999'}, 'Bob': {'home': '555-789'}}


# Q6. Change Bob’s "home" number to "555-000".
# contacts = {
#     "Alice": {"home": "555-123", "mobile": "555-456"},
#     "Bob": {"home": "555-789"}
# }
# contacts["Bob"]["home"] = "555-000"
# print(contacts)

# Expected Output:
# {'Alice': {'home': '555-123', 'mobile': '555-456'}, 'Bob': {'home': '555-000'}}

# Q7. Add a new student {"name": "Eve", "scores": {"math": 88, "english": 92}}
# into the list of students.
students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 70}}
]
# # students = list(students)
# students.extend({"name": "Eve", "scores": {"math": 88, "english": 92}})

print((students))

# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}},
#  {'name': 'Bob', 'scores': {'math': 75, 'english': 70}},
#  {'name': 'Eve', 'scores': {'math': 88, 'english': 92}}]

# Q8. Change Bob's english score from 70 to 78.
students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 70}}
]

students =
# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}},
#  {'name': 'Bob', 'scores': {'math': 75, 'english': 78}}]


# Q9. Add a new dictionary {"year": 2022, "semester": "Spring"} 
# inside Alice’s record under a new key "enrollment".
students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 78}}
]
# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}, 'enrollment': {'year': 2022, 'semester': 'Spring'}},
#  {'name': 'Bob', 'scores': {'math': 75, 'english': 78}}]

# Q10. In this shop cart, add a new product "Notebook" with price 200.
cart = {
    "items": [
        {"name": "Pen", "price": 10},
        {"name": "Book", "price": 50}
    ],
    "owner": "Alice"
}
# Expected Output:
# {'items': [{'name': 'Pen', 'price': 10}, {'name': 'Book', 'price': 50}, {'name': 'Notebook', 'price': 200}],
#  'owner': 'Alice'}



