# Exercise 1 – Scope Prediction
x = 10

def test():
    x = 20
    print(x)

test() # predict 20
print(x) # predict 10

# Exercise 2 – Pure Grade Function
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
# Example
print(calculate_grade(95))  # A
print(calculate_grade(78))  # C
print(calculate_grade(50))  # F

# Exercise 3 – Flexible Average
def average(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)

#Example
print(average(10, 20, 30))      # 20.0
print(average(5, 10, 15, 20))   # 12.5

# Exercise 4 – Profile Builder
def build_profile(name, **details):
    profile = {"name": name}

    for key, value in details.items():
        profile[key] = value

    return profile

# Example
student = build_profile(
    "Mona",
    age=20,
    city="Gaza",
    course="Python"
)

print(student)

# Exercise 5 – Refactor with Docstring and Type Hints

# Original Function
def calculate_grade(percentage):
    """Return a letter grade and message based on percentage."""
    if percentage >= 90:
        return "A", "🏆 Outstanding! You really know your Python!"
    elif percentage >= 75:
        return "B", "🎉 Great job! Solid Python knowledge."
    elif percentage >= 60:
        return "C", "✅ Good effort. Keep practising!"
    elif percentage >= 40:
        return "D", "📖 Keep studying — you're getting there."
    else:
        return "F", "💪 Review the lessons and try again!"

# Improved Version
def calculate_grade(percentage: float) -> tuple[str, str]:
    """
    Calculate the letter grade and feedback message.

    Args:
        percentage: The player's score as a percentage.

    Returns:
        A tuple containing:
        - the letter grade
        - a feedback message
    """
    if percentage >= 90:
        return "A", "🏆 Outstanding! You really know your Python!"
    elif percentage >= 75:
        return "B", "🎉 Great job! Solid Python knowledge."
    elif percentage >= 60:
        return "C", "✅ Good effort. Keep practising!"
    elif percentage >= 40:
        return "D", "📖 Keep studying — you're getting there."
    else:
        return "F", "💪 Review the lessons and try again!"

# Separation Between Calculation and Printing
percentage = 80
grade, message = calculate_grade(percentage)

print(f"Grade: {grade}")
print(message)