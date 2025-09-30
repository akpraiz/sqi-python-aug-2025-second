# --------------------------ARITHMETIC OPERATORS--------------------------

# num1 = 6
# num2 = 8
# print(num1 + num2)
# print(num1 - num2)
# print(num1 / num2)
# print(num1 * num2)


# print(6 + 8)
# print(6 + num2)
# print(num1 + 8)


# print(5 ** 2)  # square

# print(25 ** (1/2))  # sqrt


# print(7 // 2)
# print(25 // 3)
# print(25 % 3)

# print(10 / 4)

# print(10 // 4)
# print(10 % 4)


# first_num = 16
# second_num = 5
# print(first_num / second_num)
# print(first_num // second_num)
# print(first_num % second_num)


# minutes = 340
# # 5 hr 40 mins 
# print(f"{minutes // 60} hr {minutes % 60} mins")



# print(6 % 2 == 0)
# # print(7 % 2 == 0)


# num = int(input("Enter a number: "))
# is_multiple_of_3 = num % 3 == 0
# print(f"It is {is_multiple_of_3} that {num} is a multiple of 3")
# --------------------------ARITHMETIC OPERATORS--------------------------



# --------------------------ASSIGNMENT OPERATORS--------------------------

# num = 8
# print(num)


# num = 8
# # num = num + 5
# num += 5
# print(num)

# balance = 900.56
# deposit = float(input("How much do you want to deposit: "))

# # balance = balance + deposit

# balance += deposit

# print(balance)

# balance = 900.56
# withdrawal_amt = float(input("How much do you want to withdraw: "))

# # balance = balance - withdrawal_amt

# balance -= withdrawal_amt

# print(balance)


# from decimal import Decimal

# num1 = Decimal('0.1')
# num2 = Decimal('0.2')
# print(num1 + num2)

# Error
# num = 8
# print(num += 6)


# num = 8
# num *= 3
# print(num)
# --------------------------ASSIGNMENT OPERATORS--------------------------




# --------------------------COMPARISON OPERATORS--------------------------


# print(7 > 5)
# print(17 > 905)
# print(17 < 905)
# print(17 <= 905)
# print(17 == 18)
# print(17 == 17)
# print(17 == 17.0)

# print(7 % 2 != 0)
# --------------------------COMPARISON OPERATORS--------------------------



# --------------------------LOGICAL OPERATORS--------------------------

# is_happy = True
# is_female = True
# is_student = False

# print(is_happy and is_female and is_student)
# print(is_happy or is_female or is_student)
# print(is_happy or (is_female and is_student))  # True

# is_married = False

# print(not is_married)
# print(not False)
# print(not True)

# is_happy = True
# is_female = True
# is_student = False

# print(not(is_happy and is_female and is_student))

# print(7 == 8)
# print(not(7 == 8))
# print(7 != 8)
# --------------------------LOGICAL OPERATORS--------------------------



# --------------------------IDENTITY OPERATORS--------------------------

# interning

# -5 and 255


# colors = {"red", "green", "blue"}
# colors2 = {"green", "blue", "red"}
# print(colors == colors2)



# colors = ["red", "green", "blue"]
# colors_copy = colors  # reference
# print(colors)
# print(colors_copy)
# print(colors == colors_copy)
# print(colors is colors_copy)

# colors.append("violet")
# print(colors)
# print(colors_copy)


# colors = ["red", "green", "blue"]
# colors_copy = colors.copy()  # true copy
# # print(colors)
# # print(colors_copy)
# print(id(colors))
# print(id(colors_copy))
# print(colors == colors_copy)
# print(colors is colors_copy)


# import copy

# colors = [["red", "green"], ["blue", "yellow"]]
# # colors_copy = colors.copy()  # true copy
# # colors_copy = copy.copy(colors)  # true copy
# colors_copy = copy.deepcopy(colors)  # true copy
# colors[0][0] = "black"
# print(colors)
# print(colors_copy)
# print(colors == colors_copy)
# print(colors is colors_copy)
# married = None

# print(married == None)  # Wrong
# print(married is None)  # Pythonic


# --------------------------IDENTITY OPERATORS--------------------------


# --------------------------MEMBERSHIP OPERATORS--------------------------

# name = "Ifeoluwa"

# print("e" in name)
# print("i" in name)
# print("i" in name.lower())

# print("z" not in name)  # right

# print(not("z" in name))  # don't use this

# iterable


colors = ["red", "green", "blue", "yellow"]

# print("red" in colors)
# print("black" in colors)
# print("GREEN" in colors)

# color1, color2, color3, color4 = colors
# colors = [color1.upper(), color2.upper(), color3.upper(), color4.upper()]
# print("GREEN" in colors)


# colors = ", ".join(colors)
# colors = colors.upper()
# colors = colors.split(", ")
# print("GREEN" in colors)
# print(colors)




# even_nums = [2, 10, 4, 16]


# colors = {"red", "green", "blue", "yellow"}
# print(colors[2])


# --------------------------MEMBERSHIP OPERATORS--------------------------
