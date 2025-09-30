# class Book:
#     def __init__(self, title: str, author: str, pages: int):
#         self.title = title
#         self.author = author
#         self.pages = pages
    

# class Library:
#     def __init__(self, books: list[Book]):
#         self.books = books

#     def total_pages(self):
#         return sum(book.pages for book in self.books)

# book1 = Book("Things Fall Apart", "Chinua Achebe", 300)
# book2 = Book("Purple Hibiscus", "Chimamanda Ngozi Adichie", 250)

# library = Library([book1, book2])
# print(library.total_pages()) #550

# Assignment
# 1. Fill in the Line class methods to accept coordinates as a pair of tuples and 
# return the slope and distance of the line. Look up the formulas for 
# finding the distance and slope of a line.

# import math

# class Line:
#     def __init__(self, coor1, coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2

#     def distance(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#     def slope(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         if x2 - x1 == 0:
#             return None
#         return (y2 - y1) / (x2 - x1)

# EXAMPLE EXECUTION

# coordinatel = (3,2)
# coordinate2 = (8,10)

# line_1 = Line(coordinatel, coordinate2)

# print(line_1.distance())  # 9.433981132056603
# print(line_1.slope())  # 1.6

# 2.	Fill in the class

# class Cylinder:
#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius

#     def volume (self):
#         return round(math.pi * (self.radius ** 2) * self.height, 2)

#     def surface_area(self):
#         return round(2 * math.pi * self.radius * self.height + 2 * math.pi * (self.radius ** 2), 2)

# # # EXAMPLE EXECUTION

# cylinder = Cylinder(2,3)
# print(cylinder.volume())  # 56.52
# print(cylinder.surface_area())  # 94.2

# ===========================
# Assignment Exercises
# ===========================

# Each exercise describes a scenario with classes, objects, and interactions.  
# Your task: implement the classes and methods so that the given sample execution works  
# and produces the expected output.

# -----------------------------------------------------------
# 1. Library & Borrowing
# -----------------------------------------------------------
# class Book:
#     def __init__(self, title, author, quantity):
#         self.title = title
#         self.author = author
#         self.quantity = quantity

# class Library:
#     def __init__(self, books:list[Book]):
#         self.books = books

#     def borrow(self, title):
#         for book in self.books:
#             if book.title == title:
#                 if book.quantity > 0:
#                     book.quantity -= 1
#                     return True
#                 else:
#                     return False
#         return False

#     def available_books(self):
#         return {book.title: book.quantity for book in self.books}

# book1 = Book("1984", "George Orwell", 5)
# book2 = Book("Brave New World", "Aldous Huxley", 2)

# library = Library([book1, book2])

# print(library.borrow("1984"))
# # -> True

# print(library.borrow("Brave New World"))
# # -> True

# print(library.borrow("Brave New World"))
# # -> True

# print(library.borrow("Brave New World"))
# # -> False

# print(library.available_books())
# # -> {'1984': 4, 'Brave New World': 0}


# -----------------------------------------------------------
# 2. Shopping Cart with Discounts
# -----------------------------------------------------------
# class ShoppingCart:
#     def __init__(self):
#         self.items = []   
#         self.discount = 0 

#     def add_item(self, name, price, quantity=1):
#         self.items.append({"name": name, "price": price, "quantity": quantity})

#     def apply_discount(self, percent):
#         self.discount = percent

#     def total(self):
#         subtotal = sum(item["price"] * item["quantity"] for item in self.items)
#         if self.discount > 0:
#             subtotal -= (self.discount / 100) * subtotal
#         return int(subtotal)  


# cart = ShoppingCart()

# cart.add_item("milk", 500, 2)
# cart.add_item("bread", 1000, 1)

# print(cart.total())
# # -> 2000

# cart.apply_discount(10)   # 10% discount
# print(cart.total())
# # -> 1800


# 3. Cinema Ticket Booking (with user input)
# class Cinema:
#     def __init__(self, movies: dict[str, int]):
#         self.movies = movies

#     def book(self, movie, seats):
#         if movie in self.movies:
#             if self.movies[movie] >= seats:
#                 self.movies[movie] -= seats
#                 return True
#             else:
#                 return False
#         return False

#     def show_available(self):
#         return self.movies


# # Assume input:
# # Enter movie name: Interstellar
# # Enter seats to book: 3

# cinema = Cinema({"Interstellar": 5, "Inception": 2})

# movie = input("Enter movie name: ").strip()
# seats = int(input("Enter seats to book: "))

# print(cinema.book(movie, seats))
# # If user entered "Interstellar" and "3"
# # -> True

# print(cinema.show_available())
# # -> {'Interstellar': 2, 'Inception': 2}


# 4. Student Grades & Average
# -----------------------------------------------------------
# class Course:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade


# class Student:
#     def __init__(self, name, courses: list[Course]):
#         self.name = name
#         self.courses = courses

#     def average(self):
#         if not self.courses:
#             return 0
#         total = sum(course.grade for course in self.courses)
#         return total / len(self.courses)

#     def best_course(self):
#         if not self.courses:
#             return None
#         best = max(self.courses, key=lambda c: c.grade)
#         return best.name


# course1 = Course("Math", 80)
# course2 = Course("Physics", 70)
# course3 = Course("English", 90)

# student = Student("Amina", [course1, course2, course3])

# print(student.average())
# # -> 80.0

# print(student.best_course())
# # -> English

# You are building a simple simulation of a space mission. There are different types of spacecraft.

# 1. Create a base class
# Create a class called Spacecraft with:
# Attributes:
# name (string)
# fuel (integer)

class Spacecraft:
    def __init__(self, name: str, fuel: int):
        self.name = name
        self.fuel = fuel

    def launch(self):
        fuel_required = 50
        if self.fuel < 50:
            print("Not enough fuel to launch.")
            return
        self.fuel -= fuel_required
        print(f"Launching {self.name}!")
    
    def refuel(self, amount:int):
        if amount < 0:
            print("Cannot refuel with negative amount.")
            return
        self.fuel += amount
        print(f"Refueled {self.name} with {amount} units. Fuel is now {self.fuel}.")
              
# Methods:
# launch() — prints "Launching {name}!"
# Reduces fuel by 50 units.
# If not enough fuel, print "Not enough fuel to launch."

# refuel(amount) — adds amount to fuel.


# 2. Create subclasses
# CargoShip
# Has an additional attribute: cargo_weight (integer)
# Override launch() — launching consumes extra fuel depending on cargo:
# total fuel reduction = 50 + (cargo_weight * 2)

# class CargoShip(Spacecraft):
#     def __init__(self, name: str, fuel: int, cargo_weight: int):
#         super().__init__(name, fuel)
#         self.cargo_weight = cargo_weight
    
#     def launch(self):
#         fuel_required = 50 + (self.cargo_weight * 2)
#         if self.fuel < fuel_required:
#             print("Not enough fuel to launch")
#             return
#         self.fuel -= fuel_required
#         print(f"Launching {self.name} with cargo!")

# class PassengerShip(Spacecraft):
#     def __init__(self, name: str, fuel: int, passenger_count: int):
#         super().__init__(name, fuel)
#         self.passenger_count = passenger_count

#     def launch(self):
#         if self.passenger_count > 100:
#             print("Too many passengers. Cannot launch.")
#             return
#         super().launch()


# PassengerShip
# Has an additional attribute: passenger_count (integer)
# Override launch() — if passenger_count > 100, print "Too many passengers. Cannot launch."
# Otherwise, launch normally (reduce fuel by 50 units)

# 3. Handle negative refuel amounts.

# SAMPLE EXECUTION
# Create objects
# cargo_ship = CargoShip("Galactic Hauler", 200, 30)
# passenger_ship = PassengerShip("Star Voyager", 100, 80)

# # Attempt to launch both ships
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 200 - (50 + 30*2) = 90

# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 100 - 50 = 50

# # Refuel both ships
# cargo_ship.refuel(50)
# # Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.

# passenger_ship.refuel(30)
# # Output: Refueled Star Voyager with 30 units. Fuel is now 80.

# # Launch again after refueling
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 140 - (50 + 30*2) = 30

# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 80 - 50 = 30

# # Try to refuel with invalid amount
# cargo_ship.refuel(-10)
# # Output: Cannot refuel with negative amount.

# # Test PassengerShip with too many passengers
# passenger_ship.passenger_count = 120
# passenger_ship.launch()
# # Output: Too many passengers. Cannot launch.

# # Try to launch cargo ship with low fuel
# cargo_ship.launch()
# # Output: Not enough fuel to launch.


# Ask the user for their age
# Tell them when they were born
# If the user enters an age that is not convertible to an integer, 
# then tell them they have to enter an integer and keep asking them till they enter a correct value
# If the user enters an age that is negative, keep asking them till they enter a correct value 
# only show their birth year when the value they entered is correct

from datetime import datetime

# while True:
# current_year = datetime.now().year

# try:
#     age = int(input("Enter your age: "))
#     result = current_year - age
# except ValueError:
#         print("Enter an integer")
# except ValueError:
#         print("Enter a positive integer")
# else:
#     print(f"You were born in the year {result}")
#     break

# def celsius_to_fahrenheit(celsius: float):
#     while True:
#         try:
#             fahrenheit = (float(celsius * 9/5) + 32)
#         except ValueError as e:
#             print(f"Input is not convertible to a number: {e}")
#         else:
#             return fahrenheit
#         break
    # try:
    #         fahrenheit = (celsius * 9/5) + 32
    # except ValueError as e:
    #         print(f"Input is not convertible to a number: {e}")
    # else:
    #         return fahrenheit
        


# print(celsius_to_fahrenheit("45"))

# Assignment
# 1. Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.


# class NegativeNumberError(Exception):
#     """Raised when a number is negative."""
#     pass

# def check_positive(number):
#     if number < 0:
#         raise NegativeNumberError(f"Negative number entered: {number}")
#     else:
#         print(f"{number} is positive.")

# try:
#     check_positive(-5)
# except NegativeNumberError as e:
#     print("Caught an exception:", e)

# 2. Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.


# def safe_divide(a, b):
#     try:
#         a = float(a)
#         b = float(b)
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero.")
#     except TypeError:
#         print("Error: Both inputs must be numbers.")
#     except ValueError:
#         print("Error: Inputs must be convertible to numbers.")



