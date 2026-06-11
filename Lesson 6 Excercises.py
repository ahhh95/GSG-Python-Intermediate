print(50 * "-")
print("Exercise 1 — Calculator Ask the user for two numbers and print the result of all " \
"seven arithmetic operators on them (add, subtract, multiply, divide, floor divide, modulo, " \
"power).")
print(50 * "-")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
add = first_number + second_number
subtract = first_number - second_number
multiply = first_number * second_number
divide = first_number / second_number
floor_divide = first_number // second_number
modulo = first_number % second_number
power = first_number ** second_number

print(f"Addition of {first_number} and {second_number} is: {add}")
print(f"Subtraction of {first_number} and {second_number} is: {subtract}")
print(f"Multiplication of {first_number} and {second_number} is: {multiply}")
print(f"Division of {first_number} and {second_number} is: {divide}")
print(f"Floor Division of {first_number} and {second_number} is: {floor_divide}")
print(f"Modulo of {first_number} and {second_number} is: {modulo}")
print(f"Power of {first_number} and {second_number} is: {power}")

print(50 * "-")
print("""
Exercise 2 — String analyser
Ask the user for a sentence and print:
 - The sentence in UPPERCASE
 - The number of characters (including spaces)
 - The number of words
 - Whether the sentence contains the word "Python" (True/False)
 - The sentence reversed
""")
print(50 * "-")

sentence = input("Enter a sentence: ")
uppercase_sentence = sentence.upper()
character_count = len(sentence)
word_count = len(sentence.split())
contains_python = "Python" in sentence
reversed_sentence = sentence[::-1]

print(f"UPPERCASE: {uppercase_sentence}")
print(f"Number of characters: {character_count}")
print(f"Number of words: {word_count}")
print(f"Contains 'Python': {contains_python}")
print(f"Reversed sentence: {reversed_sentence}")

print(50 * "-")
print("Exercise 3 — Type conversion chain Start with the string 3.7. Convert it to float, "
"multiply by 4, convert to int, then convert back to string. Print the result and its type "
"at every step.")
print(50 * "-")

number_str = "3.7"
print(f"Original string: {number_str} (type: {type(number_str)})")
number_float = float(number_str)
print(f"Converted to float: {number_float} (type: {type(number_float)})")
number_multiplied = number_float * 4
print(f"Multiplied by 4: {number_multiplied} (type: {type(number_multiplied)})")
number_int = int(number_multiplied)
print(f"Converted to int: {number_int} (type: {type(number_int)})")
number_str_converted = str(number_int)
print(f"Converted back to string: {number_str_converted} (type: {type(number_str_converted)})")

print(50 * "-")
print("Exercise 4 —Password strength checker Ask for a password. Print True or False for " \
"each of these checks:" \
"Is it longer than 8 characters?" \
"Does it contain an uppercase letter? (hint: password != password.lower())" \
"Does it start with a letter? (hint: password[0].isalpha())")
print(50 * "-")

password = input("Enter a password: ")
is_longer_than_8 = len(password) > 8
contains_uppercase = password != password.lower()
starts_with_letter = password[0].isalpha() if password else False
print(f"Is it longer than 8 characters? {is_longer_than_8}")
print(f"Does it contain an uppercase letter? {contains_uppercase}")
print(f"Does it start with a letter? {starts_with_letter}")