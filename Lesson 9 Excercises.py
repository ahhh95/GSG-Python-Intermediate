print(50 * "-")
print("""Exercise 1 — Temperature toolkit Write three functions:

celsius_to_fahrenheit(c) → returns (c * 9/5) + 32
fahrenheit_to_celsius(f) → returns (f - 32) * 5/9
celsius_to_kelvin(c) → returns c + 273.15
Call each function and print the results.""")
print(50 * "-")

#Answer Exercise 1
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

# Example
print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"32°F = {fahrenheit_to_celsius(32)}°C")
print(f"0°C = {celsius_to_kelvin(0)}K")

print(50 * "-")
print("""Exercise 2 — String utilities Write a function is_palindrome(text) that returns True if the text reads the same backwards (ignore case and spaces).

"racecar" → True
"A man a plan a canal Panama" → True
"hello" → False""")
print(50 * "-")

#Answer Exercise 2
def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

# Example
print(is_palindrome("racecar"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))

print(50 * "-")
print("""Exercise 3 — Grade statistics Write a function analyse_grades(grades) that takes 
      a list of numbers and prints:
The average
The highest grade
The lowest grade
How many students passed (score ≥ 60)""")
print(50 * "-")

#Answer Exercise 3
def analyse_grades(grades):
    if grades == []:
        print("No grades provided.")
    else:
        average = sum(grades) / len(grades)
        highest = max(grades)
        lowest = min(grades)
        passed = sum(1 for grade in grades if grade >= 60)

        print(f"Average: {average:.2f}")
        print(f"Highest grade: {highest}")
        print(f"Lowest grade: {lowest}")
        print(f"Number of students passed: {passed}")

# Example
grades = [85, 92, 78, 60, 55, 90, 72]
analyse_grades(grades)

grades_empty = []
analyse_grades(grades_empty)

print(50 * "-")
print("""Exercise 4 — Refactor challenge Take this code and refactor it into clean functions 
      with proper names and docstrings:

# Ugly code to refactor
n = int(input("Number: "))
r = 1
for i in range(1, n + 1):
    r = r * i
print(r)""")
print(50 * "-")

#Answer Exercise 4
def factorial(n):
    """Calculate the factorial of a number n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial(number)}")
