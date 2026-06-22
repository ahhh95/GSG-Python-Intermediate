# Exercise 1 - First and Last
print("Exercise 1 - First and Last")
def first_last(items):
    return (items[0], items[-1])

# Example 
numbers = [10, 20, 30, 40]

result = first_last(numbers)
print(result)

# Exercise 2 - Filter Passing Grades
print("Exercise 2 - Filter Passing Grades")
grades = [90, 45, 75, 60, 30, 88]

passing = []

for grade in grades:
    if grade >= 60:
        passing.append(grade)

print(passing)

# Exercise 3 - Reverse Words
print("Exercise 3 - Reverse Words")
sentence = input("Enter a sentence: ")

words = sentence.split()

words.reverse()

result = " ".join(words)

print(result)

# Exercise 4 - Top Three Scores
print("Exercise 4 - Top Three Scores")
scores = [90, 75, 88, 61, 95, 82]

top_three = sorted(scores, reverse=True)

print(top_three[:3])

# Exercise 5 - Matrix Total
print("Exercise 5 - Matrix Total")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for row in matrix:
    for number in row:
        total += number

print(total)