# my_set = set()
# print(my_set)

# my_set = {}
# print(my_set)
# print(type(my_set))


# my_set = {1, 89, 5672, 682}
# print(my_set)
# print(type(my_set))




#                       STRINGS            LISTS            TUPLES              DICTS               SETS
# Ordered                 Yes               Yes               Yes               Yes                 No
# Indexed                 Yes               Yes               Yes               Yes, but with keys  No
# Mutable                  No               Yes               No                Yes                 Yes
# Allow duplicates        Yes               Yes               Yes               Allows duplicate    No
#                                                                               values but not keys

# my_set = {89, 678, 262}
# print(my_set[120])


# my_name = "Elizabeth"
# my_name[2] = "G"

# my_names = ["Winifred", "Chinaza", "Igboama"]
# my_names[1] = "Naza"
# print(my_names)

# items = ("bag", "shoe", "clothes", "glasses")
# items[1] = "shoes"


# Sets are unordered
# items = {"bag", "shoe", "clothes", "glasses"}
# print(items)

# items = {"bag", "shoe", "clothes", "glasses"}
# print(items[3])  # unindexed


# items = {"bag", "shoe", "clothes", "bag", "glasses"}
# print(items)
# print(len(items))


# items = {"bag", "shoe", "clothes", "Bag", "glasses"}
# print(items)
# print(len(items))



# items = {"bag", "shoe", True, "clothes", "Bag", 1, "glasses"}
# print(items)


# items = {"bag", False, 0, "shoe", True, "clothes", "Bag", 1, "glasses"}
# print(items)

# items = ("bag", "shoe", "clothes", "glasses")
# print(set(items))

# items = ("bag", "shoe", "clothes", "glasses")
# items = set(items)
# print(items)


# items = ("bag", "shoe", "clothes", "shoe", "glasses", "shoe")

# items = set(items)

# items = tuple(items)
# print(items)



# name = "Damilola"
# name = set(name)
# name = "".join(name)
# print(name)


# -----------------------------------SET METHODS--------------------------------------------

# ========================ADDING TO A SET========================

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# movies.add("Avengers: EndGame")
# print(movies)

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# movies.update({"Black Panther", "Ghost Rider"})
# print(movies)
# movies.update(("Black Panther",))
# print(movies)


# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = {"Black Panther", "Ghost Rider"}
# extra_movies = {"Heads of State", "Pentagon"}
# more_movies = {"White Collar", "Six Dragons"}
# all_movies = set()
# all_movies.update(movies)
# all_movies.update(other_movies)
# all_movies.update(extra_movies)
# all_movies.update(more_movies)


# print(movies)
# print(other_movies)
# print(extra_movies)
# print(more_movies)
# print(all_movies)

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = {"Black Panther", "Ghost Rider"}
# all_movies = movies.union(other_movies)
# print(movies)
# print(other_movies)
# print(all_movies)

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = ["Black Panther", "Ghost Rider"]
# extra_movies = ("Heads of State", "Pentagon")
# more_movies = ("White Collar", "Six Dragons")

# all_movies = movies.union(other_movies).union(extra_movies).union(more_movies)
# print(movies)
# print(other_movies)
# print(extra_movies)
# print(more_movies)
# print(all_movies)

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = {"Black Panther", "Ghost Rider"}
# extra_movies = {"Heads of State", "Pentagon"}
# more_movies = {"White Collar", "Six Dragons"}

# all_movies = movies.union(other_movies).union(extra_movies).union(more_movies)
# print(movies)
# print(other_movies)
# print(extra_movies)
# print(more_movies)
# print(all_movies)

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = {"Black Panther", "Ghost Rider"}
# all_movies = movies | other_movies
# print(movies)
# print(other_movies)
# print(all_movies)


# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = {"Black Panther", "Ghost Rider"}
# extra_movies = {"Heads of State", "Pentagon"}
# more_movies = {"White Collar", "Six Dragons"}

# all_movies = movies | other_movies | extra_movies | more_movies
# print(movies)
# print(other_movies)
# print(extra_movies)
# print(more_movies)
# print(all_movies)


# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = ["Black Panther", "Ghost Rider"]
# extra_movies = ("Heads of State", "Pentagon")
# more_movies = {"White Collar", "Six Dragons"}

# all_movies = movies | other_movies | extra_movies | more_movies
# print(movies)
# print(other_movies)
# print(extra_movies)
# print(more_movies)
# print(all_movies)


# ========================ADDING TO A SET========================



# ========================INTERSECTION OF SETS========================

# animes = {"Blue Lock", "JJK", "AOT"}
# other_animes = {"Death Note", "One Piece"}
# more_animes = {"Naruto", "Bleach"}

# intersection = animes.intersection(other_animes).intersection(more_animes)

# print(intersection)



# animes = {"Blue Lock", "JJK", "AOT"}
# other_animes = {"Death Note", "AOT", "One Piece"}
# # more_animes = {"Naruto", "AOT", "Bleach"}
# more_animes = {"Naruto", "Bleach"}

# intersection = animes.intersection(other_animes).intersection(more_animes)

# print(intersection)


# animes = {"Blue Lock", "JJK", "AOT"}
# other_animes = {"Death Note", "JJK", "AOT", "One Piece"}
# more_animes = {"Naruto", "JJK", "Bleach"}

# animes.intersection_update(animes)
# animes.intersection_update(other_animes)
# animes.intersection_update(more_animes)
# print(animes)


# animes = {"Blue Lock", "JJK", "AOT"}
# other_animes = {"Death Note", "JJK", "AOT", "One Piece"}
# more_animes = {"Naruto", "JJK", "Bleach"}
# intersection = animes & other_animes & more_animes
# print(intersection)


# animes = {"Blue Lock", "JJK", "AOT"}
# other_animes = ["Death Note", "JJK", "AOT", "One Piece"]
# more_animes = ("Naruto", "JJK", "Bleach")
# intersection = animes & other_animes & more_animes
# print(intersection)
# ========================INTERSECTION OF SETS========================




# ========================REMOVE FROM SETS========================

# fast_cars = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# fast_cars.remove("Ferrari")
# print(fast_cars)

# fast_cars = ["Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"]
# fast_cars.remove("Mustang")

# fast_cars = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# fast_cars.remove("Mustang")
# print(fast_cars)

# fast_cars = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# # fast_cars.discard("Ferrari")
# fast_cars.discard("Mustang")
# print(fast_cars)


# type annotation / type hint
# fast_cars: set[str | int] = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# popped_car = fast_cars.pop()
# print(fast_cars)
# print(popped_car)

# fast_cars: set[str | int] = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# fast_cars.clear()
# print(fast_cars)

# fast_cars: set[str | int] = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# # del fast_cars[0]  # TypeError
# del fast_cars
# print(fast_cars)  # NameError


# Del keyword

# my_list = ["James", "John", "Jake", "Jerry"]
# # del my_list[2]
# del my_list
# print(my_list)  # NameError



# ========================.DIFFERENCE() METHOD========================

# # mobile_games = {"CODM", "PUBG", "Fortnite", "Angela", "Candy Crush", "One State", "Free Fire"}
# mobile_games = {"CODM", "PUBG", "Fortnite", "Candy Crush", "Free Fire"}
# more_mobile_games = {"DLS", "Angela", "Talking Tom", "One State", "Subway Surf"}
# # even_more_mobile_games = {"Delta Force", "Warzone", "E-Football", "FIFA"}

# difference = mobile_games.difference(more_mobile_games)

# print(difference)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# # set3 = set1.difference(set2)
# set3 = set1 - set2

# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)

# ========================.DIFFERENCE() METHOD========================


# ========================.SYMMETRIC_DIFFERENCE() METHOD========================
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)


# mobile_games = {"CODM", "PUBG", "Fortnite", "Angela", "Candy Crush", "One State", "Free Fire"}
# more_mobile_games = {"DLS", "Angela", "Talking Tom", "One State", "Subway Surf"}

# print(mobile_games.intersection(more_mobile_games))

# all_games = mobile_games | more_mobile_games
# intersection = mobile_games & more_mobile_games
# symmetric_diff = all_games - intersection
# print(symmetric_diff)

# symmetric_diff_2 = mobile_games.symmetric_difference(more_mobile_games)
# mobile_games.symmetric_difference_update(more_mobile_games)
# print(mobile_games)

# symmetric_diff_2 = mobile_games ^ more_mobile_games
# print(symmetric_diff_2)



# # even_more_mobile_games = {"Delta Force", "Warzone", "E-Football", "FIFA"}

# ========================.SYMMETRIC_DIFFERENCE() METHOD========================



# ========================MISCELLANEOUS========================


# more_mobile_games = {"DLS", "Angela", "Talking Tom", "One State", "Subway Surf"}
# even_more_mobile_games = {"Delta Force", "Warzone", "E-Football", "FIFA"}
# print(even_more_mobile_games.issubset(more_mobile_games))


# nums1 = {1, 2, 3, 4, 5, 6}
# nums2 = {2, 5, 1}
# print(nums2.issubset(nums1))
# print(nums2.issubset(nums2))

# nums1 = {1, 2, 3, 4, 5, 6}
# nums2 = {2, 5, 1}

# print(nums1.intersection(nums2))

# print(nums1.isdisjoint(nums2))
# nums1 = {1, 2, 3, 4, 5, 6}
# nums2 = {20, 15, 11}
# print(nums1.isdisjoint(nums2))





# ========================MISCELLANEOUS========================


# -----------------------------------SET METHODS--------------------------------------------
