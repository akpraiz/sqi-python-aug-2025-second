                            # Ordered           Indexed         Mutable         Allows Duplicates
# List                          Yes               Yes             Yes               Yes
# Tuples                        Yes               Yes             No                Yes


# my_colors_list= ["violet", "brown", "black" "brown", "red", "torquoise"]
# print(my_colors_list)

# my_colors_tuple = ("violet", "brown", "black" "brown", "red", "torquoise")
# my_colors_tuple = ("violet", "brown", "black", "brown", "red", "torquoise")
# print(my_colors_tuple)
# print(my_colors_tuple[0])
# print(my_colors_tuple[1:4])

# print(my_colors_tuple.index("black"))
# # print(my_colors_tuple.count("green"))
# print(my_colors_tuple.count("brown"))



# coordinates = [2, 7]



# my_pos = (2, 7)
# horizontal_distance = 10
# my_pos[0] = my_pos[0] + horizontal_distance  # wrong


# my_friends = ("Daniel", "Onyeka", "Benjamin", "Gabriel")
# my_friends[2] = "John"


# my_pos = (2, 7)
# horizontal_distance = 10
# new_pos = (horizontal_distance + my_pos[0], my_pos[1])

# print(my_pos)  # (2, 7)
# print(new_pos)  # (12, 7)


# my_pos = (2, 7)
# my_pos = list(my_pos)
# horizontal_distance = 10
# my_pos[0] = my_pos[0] + horizontal_distance
# my_pos = tuple(my_pos)
# print(my_pos)


# red, green, blue = 0, 0, 255
# print(red)
# print(green)
# print(blue)


# my_colors_tuple = ("violet", "brown", "black", "brown", "red", "torquoise")
# print(len(my_colors_tuple))



# my_tuple = (89, True, False, 89.267, None, "Hiiiiii")
# print(my_tuple)

# my_colors_tuple = ("violet", "brown", "black", "brown", "red", "torquoise")
# print(type(my_colors_tuple))


# my_colors = ["violet", "brown", "black", "brown", "red", "torquoise"]
# my_colors = tuple(my_colors)
# print(my_colors)


# name = "Janet"
# print(tuple(name))



# names = "Janet"
# names = ("Janet")
# names = ("Janet",)
# names = "Janet",
# num = (34)
# print(type(num))
# print(type(names))



# ice_cream_flavors = ("strawberry", "vanilla", "chocolate", "milkshake", "coffee", "banana")
# flavors_times_3 = ice_cream_flavors * 3
# print(flavors_times_3)


# name = "John"
# print(name * 6)


# ice_cream_flavors = ["strawberry", "vanilla", "chocolate", "milkshake", "coffee", "banana"]
# print(ice_cream_flavors * 3)


# ice_cream_flavors = ("strawberry", "vanilla", "chocolate", "milkshake", "coffee", "banana")
# ice_cream_flavors = list(ice_cream_flavors)
# ice_cream_flavors.remove("vanilla")
# ice_cream_flavors = tuple(ice_cream_flavors)
# print(ice_cream_flavors)
# print(type(ice_cream_flavors))


# winnie_favorite_ice_cream_flavors = ("strawberry", "vanilla", "chocolate")
# benjamin_favorite_ice_cream_flavors = ("milkshake", "coffee", "banana")
# all_flavors = winnie_favorite_ice_cream_flavors + benjamin_favorite_ice_cream_flavors
# print(all_flavors)

# winnie_favorite_ice_cream_flavors = ("strawberry", "vanilla", "chocolate")
# red, white, brown = winnie_favorite_ice_cream_flavors
# print(red)
# print(white)
# print(brown)


# winnie_favorite_ice_cream_flavors = ("strawberry", "vanilla", "chocolate")
# red, _, brown = winnie_favorite_ice_cream_flavors
# print(red)
# print(brown)


# red, white, brown, green, coffee_brown = ("strawberry", "vanilla", "chocolate", "mint", "coffee")
# red, white, _, _, coffee_brown = ("strawberry", "vanilla", "chocolate", "mint", "coffee")
# print(_)


# red, white, *others, coffee_brown = ("strawberry", "vanilla", "chocolate", "mint", "coffee")
# print(others)

# red, white, *_, coffee_brown = ("strawberry", "vanilla", "chocolate", "mint", "coffee")
# print(_)


# Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.


# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# # print(record[1][0])
# name, age_position, depts = record
# age, position = age_position
# dept1, dept2 = depts
# print(name)
# print(age)
# print(position)
# print(dept1)
# print(dept2)



# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, (age, position), (dept1, dept2) = record
# print(name)
# print(age)
# print(position)
# print(dept1)
# print(dept2)


# meal = (
#     "Pizza",
#     ("Large", 12.99), 
#     ["Cheese", "Tomato", "Olives"]
# )

# _, (_, price), (_, topping2, _) = meal
# print(price)
# print(topping2)



# flavors = (
#     ("strawberry", "vanilla"),
#     ("chocolate", ("mint", "coffee"))
# )

# # (flavor1, flavor2), (flavor3, (flavor4, flavor5)) = flavors
# _, (_, (_, flavor5)) = flavors
# print(flavor5)

# 4. Given the nested tuple data:
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# Unpack the first element of data into variables student1 and student2, and print student2.


# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# (_, student2), _, _ = data
# print(student2)