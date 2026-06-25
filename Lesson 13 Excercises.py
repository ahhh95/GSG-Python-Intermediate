# Exercise 1 - Safe lookup
# Create a dictionary for a product with name, price, and quantity. Use .get() to read a missing discount key with default value 0.
print("Exercise 1 - Safe lookup")
product = {"name": "Laptop", "price": 1000, "quantity": 5}

discount = product.get("discount", 0)

print("Product:", product["name"])
print("Discount:", discount)

print(2 * "------------------------------")
# Exercise 2 - Word frequency
# Ask the user for a sentence and count how many times each word appears.
print("Exercise 2 - Word frequency")
sentence = input("Enter a sentence: ")

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

print(2 * "------------------------------")
# Exercise 3 - Unique visitors
# Given a list of visitor emails with duplicates, print the number of unique visitors.
print("Exercise 3 - Unique visitors")
emails = ["a@example.com", "b@example.com", "a@example.com", "c@example.com"]

unique_emails = set(emails)

print("Unique visitors:", len(unique_emails))
print(unique_emails)

print(2 * "------------------------------")
# Exercise 4 - Passed students
# Given a list of student dictionaries, create a list containing only students with score >= 60.
print("Exercise 4 - Passed students")
students = [
    {"name": "Ahmed", "score": 90},
    {"name": "Mahmoud", "score": 75},
    {"name": "Fatma", "score": 50},
    {"name": "Laurine", "score": 40},
]

passed_students = []

for student in students:
    if student["score"] >= 60:
        passed_students.append(student)

for student in passed_students:
    print(student["name"], student["score"])

print(2 * "------------------------------")
# Exercise 5 - Common interests
# Given two sets of interests, print the interests they have in common.
print("Exercise 5 - Common interests")
set1 = {"python", "music", "football", "reading"}
set2 = {"football", "python", "movies", "art"}

common = set1 & set2

print("Common interests:", common)
