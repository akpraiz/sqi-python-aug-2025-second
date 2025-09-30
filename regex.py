import re

# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# # text = "Contact us at support@example.com or enquiries@example.com for more info"
# text = "Contact us for more info."

# match = re.search(pattern, text)

# if match is not None:
#     print("Email is present in the text")
#     print("Found:")
#     print(match.group())
# else:
#     print('no match found')


# all_emails = re.findall(pattern, text)

# print(all_emails)
# word boundary

# pattern = r"\bword\b"
# text = "A in a sentence."
# match = re.search(pattern, text)
# if match:
#     print("Match found:", match.group())  # Match found: word


# pattern = r"\d+"
# text = "There are 123 apples and 456 oranges."
# matches = re.findall(pattern, text)
# print("Numbers found:", matches)  # Numbers found: ['123', '456']



# pattern = r"\s+"
# text = "This   is\na test."
# new_text = re.sub(pattern, " ", text)
# print("Replaced text:", new_text)  # Replaced text: This is a test.

# text = "This   is\na test."

# print(text.replace("\n", "").replace("\t", "").replace(" ", ""))

# import re
# # Example 2: Extract dates in YYYY-MM-DD format
# pattern = r"\b\d{4}-\d{2}-\d{2}\b"
# text = "The event is on 2023-08-15. Deadline is 2023-08-01."
# dates = re.findall(pattern, text)
# print("Dates found:", dates)  # Dates found: ['2023-08-15', '2023-08-01']


import re
# Example 3: Validate a phone number (US format)
pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
phone_number = "(123) 456-7890"
match = re.match(pattern, phone_number)
if match:
    print("Valid phone number")  # Valid phone number
    print(match.group())

else:
    print("Invalid phone number")

import re
# Example 4: Split a string by commas and whitespace
pattern = r"\s*,\s*"
text = "apple, banana,  cherry  ,  date"
fruits = re.split(pattern, text)
print("Fruits list:", fruits)  # Fruits list: ['apple', 'banana', 'cherry', 'date']