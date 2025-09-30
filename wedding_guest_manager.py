# Stage 1
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"] 
waitlist = []
print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 2
waitlist.extend(["Ken", "Jack", "Ivy"])
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 3
waitlist.append("Noah")
waitlist.append("Oliver")
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 4
# confirmed_guests.remove("Alice")
# confirmed_guests.append(waitlist[0])
# del waitlist[0]

confirmed_guests.remove("Alice")
first_person_in_waitlist = waitlist.pop(0)
confirmed_guests.append(first_person_in_waitlist)
print("\n\nStage 4")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 5
print("\n\nStage 5")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print(f"It is {"Charlie" in confirmed_guests} that Charlie is in the guest list")


# Stage 6
confirmed_guests.remove("David")
confirmed_guests.remove("Eve")
print("\n\nStage 6")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 7
# Method 1
# confirmed_guests.extend(waitlist[0:2])
# waitlist.pop(0)
# waitlist.pop(0)

# Method 2
# confirmed_guests.append(waitlist.pop(0))
# confirmed_guests.append(waitlist.pop(0))


# Method 3
first_person_in_waitlist = waitlist.pop(0)
confirmed_guests.append(first_person_in_waitlist)
first_person_in_waitlist = waitlist.pop(0)
confirmed_guests.append(first_person_in_waitlist)
print("\n\nStage 7")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)



# Stage 8
waitlist.remove("Oliver")
print("\n\nStage 8")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 9
print("\n\nStage 9")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print(f"Last three confirmed guests: {confirmed_guests[-3:]}")

# Stage 10
confirmed_guests.append("Noah")
waitlist.remove("Noah")
print("\n\nStage 10")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 11
print("\n\nStage 11")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print(f"Number of confirmed guests: {len(confirmed_guests)}")


# Stage 12
print("\n\nStage 12")
# confirmed_guests.sort()
confirmed_guests = sorted(confirmed_guests)
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 13
confirmed_guests.remove("Grace")
confirmed_guests.remove("Noah")
confirmed_guests.append("Collins")
confirmed_guests.sort()
print("\n\nStage 13")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 14
# guests_list_for_caterer = confirmed_guests.copy()

import copy
guests_list_for_caterer = copy.copy(confirmed_guests)
print("\n\nStage 14")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print("Guest list for caterer: ", guests_list_for_caterer)


# Stage 15
waitlist.clear()
print("\n\nStage 15")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
print("Guest list for caterer: ", guests_list_for_caterer)


