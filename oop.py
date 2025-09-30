# OOP - Object Oriented Programming
# paradigm - way of doing things


# Functional
# Modular
# OOP - Classes and Objects


# name = ["Ife"
# "Makanjuola"]

# print(name)

# class BankAccount:
#     # magic dunder method - magic double underscore method
#     # initialize
#     def __init__(self, account_owner, balance, bank_name, is_savings):
#         self.account_owner = account_owner
#         self.account_balance = balance
#         self.bank_name = bank_name
#         self.is_savings = is_savings

#     def account_details(self):
#         details = f"Account Owner: {self.account_owner}\n"\
#                     f"Account Balance: {self.account_balance}\n"\
#                     f"Bank Name: {self.bank_name}\n"\
#                     f"Is Savings: {self.is_savings}\n"
#         return details


# ife_account = BankAccount("Ife", 1_000_000, "Access Bank", True)
# maryam_account = BankAccount("Maryam", 50_150_000, "Opay", False)
# damilola_account = BankAccount(bank_name="GTBank", account_owner="Damilola", balance=7_000_000_000, is_savings=False)

# print(ife_account.account_owner)
# print(maryam_account.bank_name)
# print(damilola_account.account_balance)

# print(ife_account.account_details())



# ife_account = {"account_owner": "Ife", "account_balance": 1_000_000}
# maryam_account = {"account_owner": "Maryam", "accoun_balance": 1_200_000}

# accounts = [ife_account, maryam_account]


# for account in accounts:
#     print(account['account_balance'])

# import datetime

# class Car:
#     def __init__(self, color, brand, model, year_made, plate_number, transmission_type, is_luxurious, price):
#         self.color = color
#         self.brand = brand
#         self.model = model
#         self.year_made = year_made
#         self.plate_number = plate_number
#         self.transmission_type = transmission_type
#         self.is_luxurious = is_luxurious
#         self.price = price

#     def years_since_made(self):
#         return datetime.datetime.now().year - self.year_made

#     def is_cheaper_than(self, amount):
#         return self.price < amount

# micra = Car("Red and cream", "Nissan", "Micra", 2012, "BDJ419-OY", "Manual", False, 2_500_000)
# bugatti = Car("Black", "Bugatti", "Chiron", 2020, "FST666-OY", "Automatic", True, 45_000_000)

# print(micra.plate_number) 
# print(bugatti.price)

# print(micra.years_since_made())
# print(bugatti.years_since_made())

# print(micra.is_cheaper_than(3_000_000))

# 2. Create a class called Car with the following attributes:
#    - brand
#    - model
#    - year
#    - horsepower
#    - fuel_type
#
#    The class should have a method called car_info() that returns:
#    "This is a {year} {brand} {model} with {horsepower} HP running on {fuel_type}."
#
#    After defining the class, create 3 different Car objects with different values.


int("6")

from enum import Enum

class NoteBookPage:
    def __init__(self, content: str, page_number: int, color: str):
        self.content = content
        self.page_no = page_number
        self.color = color

    def __str__(self):
        return f"{self.content[:20]}"
    
    def __repr__(self):
        return f"{self.content[:20]}"

class Medium(Enum):
    HARD = 'hard'
    SOFT = 'soft'

class NoteBook:
    def __init__(self, title: str, medium: Medium, pages: list[NoteBookPage]=None):
        self.title = title
        self.medium = medium
        self.pages = pages

        if pages is None:
            self.pages = []

    def __str__(self):
        return f"{self.title} ({self.medium.value} copy)"
    
    def add_page(self, content, page_no: int, color="white"):
        for page in self.pages:
            if page.page_no == page_no:
                return "This page number is already taken"
        self.pages.append(NoteBookPage(content, page_no, color))
        return "Successfully added page"

    def list_pages(self):
        if not self.pages:
            print("No pages in this notebook yet")
            return
        
        for page in self.pages:
            print("Content:")
            print(page.content)
            print("Color:",page.color)
            print("Page Number:",page.page_no)

my_diary = NoteBook("Winnie's Diary", Medium.SOFT)

# intro_page_biology = NoteBookPage("Introduction to Biology\nBiology surrounds us.", 3, "white")

# biology_textbook = NoteBook("Essential Biology", Medium.HARD, [intro_page_biology])


# print(my_diary)
# my_diary.list_pages()
# my_diary.add_page("Winnie's Diary", 23, "red")
# my_diary.list_pages()
# print(biology_textbook)


# class CartItem:
#     def __init__(self, item_name: str, price: int, quantity: int):
#         self.name = item_name
#         self.price = price
#         self.quantity = quantity
    
#     def total(self):
#         return self.price * self.quantity

    
# class Cart:
#     def __init__(self, cart_items: list[CartItem]):
#         self.cart_items = cart_items

#     def total(self):
#         total_price = 0
#         for item in self.cart_items:            
#             total_price += item.total()
#         return total_price

# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# cart = Cart([cart_item1, cart_item2])
# print(cart.total()) # -> 8200



# class Book:
#     def __init__(self, title: str, author: str, pages: int):
#         self.title = title
#         self.author = author
#         self.pages = pages


# class Library:
#     def __init__(self, books: list[Book]):
#         self.books = books

#     # def total_pages(self):
#     #     total_no_of_pages = 0
#     #     for book in self.books:
#     #         total_no_of_pages += book.pages
#     #     return total_no_of_pages

#     def total_pages(self):
#         return sum(book.pages for book in self.books)

# book1 = Book("Things Fall Apart", "Chinua Achebe", 300)
# book2 = Book("Purple Hibiscus", "Chimamanda Ngozi Adichie", 250)

# library = Library([book1, book2])

# print(library.total_pages())  # 550 



# class OrderItem:
#     def __init__(self, item, quantity):
#         self.item = item 
#         self.quantity = quantity


# class Order:
#     def __init__(self, order_items: list[OrderItem]):
#         self.order_items = order_items

# class Warehouse:

#     def __init__(self, inventory: dict[str, int]):
#         self.inventory = inventory

#     def place_order(self, order: Order):
#         for order_item in order.order_items:
#             if order_item.item in self.inventory and order_item.quantity <= self.inventory[order_item.item]:
#                 self.inventory[order_item.item] -= order_item.quantity
#                 return True
#             return False

# warehouse = Warehouse({
#     "laptop": 10,
#     "phone": 25,
#     "headphones": 50
# })

# order1 = Order([
#     OrderItem("laptop", 2),
#     OrderItem("phone", 5)
# ])

# order2 = Order([
#     OrderItem("laptop", 9), 
#     OrderItem("headphones", 2)
# ])

# print(warehouse.place_order(order1))
# # -> True

# print(warehouse.inventory)
# # -> {'laptop': 8, 'phone': 20, 'headphones': 50}

# print(warehouse.place_order(order2))
# # -> False

# print(warehouse.inventory)
# # -> {'laptop': 8, 'phone': 20, 'headphones': 50}



# class Genre(Enum):
#     HORROR = 'Horror'
#     FICTION = 'Fiction'
#     PSYCHOLOGICAL_THRILLER = 'Psychological Thriller'
#     COMEDY = 'Comedy'
#     ROM_COM = 'Romantic Comedy'
#     SCI_FI = 'Sci Fi'


# lookup = {g.value.lower(): g for g in Genre}


# class Movie:
#     def __init__(self, title: str, director: str, rating: int, duration_in_mins: int, genre: Genre):
#         self.title = title
#         self.director = director
#         self.rating = rating
#         self.duration_in_mins = duration_in_mins
#         self.genre = genre

#     def format_duration(self):
#         return f"{self.duration_in_mins // 60} hrs, {self.duration_in_mins % 60} mins"
    

# class Watchlist:
#     def __init__(self, movies: list[Movie]):
#         self.movies = movies

#     def display_movies(self):
#         for movie in self.movies:
#             print(f"{movie.title} directed by {movie.director}. Duration: {movie.format_duration()}")

# my_watchlist = Watchlist([])

# while True:
#     i = 1
#     proceed = input(f"Enter the details for Movie {i} below or press 'stop' to stop or press the enter key to proceed: ").strip().lower()
#     if proceed == 'stop':
#         break

#     title = input("Enter the title of the movie: ").strip()
#     director = input("Enter the director of the movie: ").strip()
#     rating = int(input("Enter the rating of the movie: "))
#     duration_in_mins = int(input("Enter the duration in minutes of the movie: "))
#     genre = input("Enter the genre of the movie: ").strip().lower()

#     genre = lookup[genre]

#     movie = Movie(title, director, rating, duration_in_mins, genre)
#     my_watchlist.movies.append(movie)
#     i += 1


# my_watchlist.display_movies()




# class Circle:

#     PI = 22/7

#     def __init__(self, radius, circumference=None):
#         self.radius = radius
#         self.diameter = radius * 2
#         self._circumference = circumference
#         if circumference is None:
#             self._circumference = 2 * Circle.PI * self.radius

#     @property
#     def circumference(self):
#         return 2 * Circle.PI * self.radius

#     @circumference.setter
#     def circumference(self, value):
#         self._circumference = value

    
# circle_1 = Circle(4)
# circle_2 = Circle(9)


# # print(circle_1.radius)
# # print(circle_1.diameter)
# print(circle_1.circumference)

# circle_1.circumference = 20

# print(circle_1.circumference)



# class Person:
#     def __init__(self, name: str, age: int, is_male: bool):
#         self.name = name
#         self._age = age
#         self.is_male = is_male

#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             raise ValueError("Age cannot be negative")
#         self._age = value
    

# praise = Person("Praise Akande", 56, True)
# damilola = Person("Damilola Aregbesola", 3, False)

# print(praise.age)

# # praise.age = -76
# praise.age = 76
# print(praise.age)


# class BankAccount:
#     def __init__(self, name: str, balance: int):
#         self.name = name
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance
    
#     @balance.setter
#     def balance(self, amount: int):
#         if amount < 0:
#             amount *= -1
#             if self._balance < amount:
#                 raise ValueError("Insufficient funds")
#             self._balance -= amount
#             return
#         self._balance += amount



# # --- Test Cases ---
# john = BankAccount("John Doe", 1000)

# print(john.balance)   # 1000

# john.balance = 500    # Deposit 500
# print(john.balance)   # 1500

# john.balance = -200   # Withdraw 200
# print(john.balance)   # 1300

# john.balance = -2000  # ❌ Should raise ValueError: Insufficient funds!


# $1,000,000.00


# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self._balance = balance

#     def __str__(self):
#         return f"Account owner: {self.owner}\nAccount balance: ${self._balance:,.2f}"    

#     @property
#     def balance(self):
#         return f"${self._balance:,.2f}"
    
#     @balance.setter
#     def balance(self, new_balance):
#         if new_balance < 0:
#             raise ValueError("New Balance must be positive")
        
#         self._balance = new_balance

#     def deposit(self, amount):
#         self._balance += amount
#         print("Deposit accepted")

#     def withdraw(self, amount):
#         if amount > self._balance:
#             print("funds Unavailable!")
#             return
        
#         self._balance -= amount
#         print("Withdrawal accepted")

# # #1. Instantiate the class
# acct1 = Account('Winnie', 100)

# # #2. Print the object
# print(acct1)
# # # Output:
# # # Account owner: Winnie
# # # Account balance: $100.00
# # #3. Show the account owner attribute
# # print(acct1.owner)  # Winnie

# # # #4. Show the account balance attribute 
# print(acct1.balance)  # 100

# # # #5. Make a series of deposits and withdrawals 
# acct1.deposit(50)  # Output: Deposit Accepted

# print(acct1.balance)  # 150
# # acct1.withdraw(15)  # Output: Withdrawal Accepted

# # # #6. Make a withdrawal that exceeds the available balance 
# # acct1.withdraw(500)  # Output: Funds Unavailable!

# acct1.balance = -400
# print(acct1.balance)  # 150


# class Parent:
#     def __init__(self, complexion, height, eye_color, face_structure, hair_color, weight):
#         self.complexion = complexion
#         self.height = height
#         self.eye_color = eye_color
#         self.face_structure = face_structure
#         self.hair_color = hair_color
#         self.weight = weight

#     def can_drive(self):
#         return True

#     def introduce_yourself(self):
#         print(f"I am a Parent. Complexion: {self.complexion}, Height: {self.height}, Eye Color: {self.eye_color}, Face Structure: {self.face_structure}, Hair color: {self.hair_color}, Weight: {self.weight}")

    
# class Child(Parent):

#     def __init__(self, complexion, height, face_structure, weight):
#         super().__init__(complexion, height, "blue", face_structure, "brown", weight)

#     def can_drive(self):
#         return False


# kariola = Parent("light", "tall", "black", "oval", "black", "slim")
# john = Child("dark", "tall", "oval", "slim")

# print(kariola.height)
# print(john.height)

# print(kariola.can_drive())
# print(john.can_drive())


# print(john.hair_color)
# print(john.eye_color)

# sarah = Child("light", "tall", "oval", "slim")

# print(sarah.hair_color)
# print(sarah.eye_color)




# class Animal:
#     def __init__(self, name, type, is_mammal, has_wings, has_tail, sound, age, color, domestication_status):
#         self.name = name
#         self.is_mammal = is_mammal
#         self.has_wings = has_wings
#         self.has_tail = has_tail
#         self.age = age
#         self.type = type
#         self.color = color
#         self.sound = sound
#         self.domestication_status = domestication_status


#     def make_sound(self):
#         return f"{self.name}, the {self.type} says {self.sound}"
    

# class Dog(Animal):
#     def __init__(self, name, age, color, domestication_status, breed, position: tuple[int, int] = (0, 0)):
#         super().__init__(name, "Dog", True, False, True, "Woof", age, color, domestication_status)
#         self.breed = breed
#         self.position = position

#     def show_position(self):
#         return f"I am at {self.position}"

#     def fetch(self, destination: tuple[int, int]):
#         self.position = destination


# spider = Animal("Itsy Bitsy Spider", "Spider", False, False, False, None, 2, "brown", True)
# lizzy = Dog("Lizzy", 3, "black and tan", True, "German Shepherd")

# print(spider.name)
# print(lizzy.name)

# print(lizzy.make_sound())
# print(spider.make_sound())

# print(lizzy.show_position())

# print(lizzy.fetch((4, 9)))

# print(lizzy.show_position())



# class Device:
#     def __init__(self, brand, type, price, resolution: tuple[int, int], battery, storage, is_smart):
#         self.brand = brand
#         self.type = type
#         self.price = price
#         self.resolution = resolution
#         self.battery = battery
#         self.storage = storage
#         self.is_smart = is_smart

#     def details(self):
#         return f"""Device Type: {self.type}
# Brand: {self.brand}
# Price: {self.price}
# Resolution: {self.resolution}
# Battery: {self.battery}
# Storage: {self.storage}
# is smart: {'Yes' if self.is_smart else 'No'}
# """
    

# class Phone(Device):
#     def __init__(self, brand, price, resolution, battery, storage, is_smart, can_make_calls, has_sim_slots):
#         super().__init__(brand, "mobile phone", price, resolution, battery, storage, is_smart)
#         self.can_make_calls = can_make_calls
#         self.has_sim_slots = has_sim_slots

#     def make_call(self):
#         if self.can_make_calls:
#             return "Call has been made"
#         return "This phone cannot make calls"
    


# google_pixel = Phone("Google Pixel", 1_900_000, (2400, 1080), 5000, 512, True, True, True)
# tonasobe = Phone("Nokia 3310", 11_000, (240, 320), 1200, 16, False, True, True)

# print(google_pixel.battery)
# print(tonasobe.battery)
# print(google_pixel.details())
# print(tonasobe.details())


# tv = Device(
#     brand="LG",
#     type="Television",
#     price=800,
#     resolution=(3840, 2160),
#     battery="N/A",
#     storage="N/A",
#     is_smart=True
# )

# camera = Device(
#     brand="Canon",
#     type="Camera",
#     price=1500,
#     resolution=(6000, 4000),
#     battery="2000mAh",
#     storage="64GB",
#     is_smart=False
# )

# devices: list[Device] = [google_pixel, tonasobe, tv, camera]

# for device in devices:
#     print(device.details())
#     print(device.resolution)


# class Performer:
#     def perform(self):
#         return "I am performing"
    

# class Artiste:
#     def perform(self):
#         return "I am an artiste performing"
    

# class Dancer:
#     def perform(self):
#         return "I am a dancer performing"
    

# performers: Performer | Artiste | Dancer = [Performer(), Artiste(), Dancer()]

# for performer in performers:
#     print(performer.perform())




# class Performer:

#     CAN_PERFORM = True

#     def perform(self):
#         return f"I am performing"



# performer = Performer()
# print(performer.CAN_PERFORM)


# You are building a simple simulation of a fantasy battle. Create different types of game 
# characters.

# 1. Create a base class
# Create a class called GameCharacter that has:
# Attributes:
# name (string)
# health (integer)
# attack_power (integer)

# Methods:
# A method attack(target) that reduces the target's health by self.attack_power.

class GameCharacter:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def stats(self, target):
        print(f"{self.name} attacks {target.name}!")
        print(f"{target.name}'s health is now {target.health}")

    def attack(self, target):
        if target == self:
            print(f"{self.name} cannot attack themself")
            return False
        target.health -= self.attack_power
        return True


# 2. Create subclasses
# Warrior
# Has an extra attribute: armor (integer)
# Override attack(target) so that it deals extra 10 damage.

# Mage
# Has an extra attribute: mana (integer)
# Override attack(target) so that it uses 5 mana each time it attacks. 
# If mana is less than 5, print "Not enough mana to attack".


class Warrior(GameCharacter):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)
        self.armor = armor

    def attack(self, target):
        if super().attack(target):
            target.health -= 10
            self.stats(target)

class Mage(GameCharacter):
    def __init__(self, name, health, attack_power, mana: int):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def attack(self, target):
        if self.mana < 5:
            print("Not enough mana to attack")
            return
        super().attack(target)
        self.mana -= 5
        self.stats(target)
        

# 3. Handle cases where the target is the same as the attacker.
# SAMPLE EXECUTION 1
warrior = Warrior(name="Thor", health=100, attack_power=10, armor=20)
mage = Mage(name="Merlin", health=100, attack_power=10, mana=10)
warrior.attack(mage)
# Output:
# Thor attacks Merlin!
# Merlin's health is now 80
mage.attack(warrior)
# Output:
# Merlin attacks Thor!
# Thor's health is now 90
mage.attack(warrior)
# Output:
# Merlin attacks Thor!
# Thor's health is now 80
mage.attack(warrior)
# Output:
# Not enough mana to attack
print(warrior.health)  # 80
print(mage.health)  # 80
print(mage.mana)  # 0



# SAMPLE EXECUTION 2
merlin = Mage(name="Merlin", health=100, attack_power=20, mana=10)
gaius = Mage(name="Gaius", health=100, attack_power=10, mana=30)

merlin.attack(gaius)
# Output:
# Merlin attacks Gaius
# Gaius’s health is now 80
gaius.attack(merlin)
# Output:
# Gaius attacks Merlin
# Merlin’s health is now 90
gaius.attack(gaius)
# Output:
# Gaius cannot attack themself
gaius.attack(merlin)
# Output:
# Gaius attacks Merlin
# Merlin’s health is now 80
merlin.attack(gaius)
# Output:
# Merlin attacks Gaius
# Gaius’s health is now 60
merlin.attack(gaius)
# Output:
# Not enough mana to attack




