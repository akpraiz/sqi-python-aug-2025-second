import re

with open("reviews.txt", "r", encoding="utf-8") as f:
    text = f.read()

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

phone_pattern = r"\+234\s\d{3}\s\d{3}\s\d{4}"

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

with open("emails.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(emails))

with open("phone_numbers.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(phones))
