print(50 * "-")
print("""Exercise 1 — FizzBuzz Print numbers from 1 to 50. But:
For multiples of 3, print "Fizz" instead
For multiples of 5, print "Buzz" instead
For multiples of both 3 and 5, print "FizzBuzz""")
print(50 * "-")

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print(50 * "-")
print("""Exercise 2 — Sum of digits Ask the user for a number (e.g. 1234). Convert it to a 
      string, loop over each character, convert back to int, and sum all digits. Expected: 
      1+2+3+4 = 10""")
print(50 * "-")

number = input("Enter a number: ")
total = 0
for digit in number:
    total += int(digit)
print(f"The sum of the digits in {number} is: {total}")

print(50 * "-")
print("""Exercise 3 — Password generator preview Print all even numbers between 1 and 100 "
      whose square root is also a whole number. (Hint: n ** 0.5 % 1 == 0 checks for perfect 
      squares)""")
print(50 * "-")

for i in range(1, 101):
    if i % 2 == 0 and (i ** 0.5) % 1 == 0:
        print(i)

print(50 * "-")
print("""Exercise 4 — ATM Simulation Start with a balance of R$1000.
In a while True loop, show a menu:

1. Check balance
2. Deposit
3. Withdraw
4. Exit
Use break to exit on option 4. Prevent withdrawals greater than the current balance.""")
print(50 * "-")

balance = 1000
while True:
    print("\nATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("Choose an option (1-4): "))
    
    if choice == 1:
        print(f"Your current balance is: R${balance:.2f}")
    elif choice == 2:
        deposit_amount = float(input("Enter the amount to deposit: R$"))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"Deposited R${deposit_amount:.2f}. New balance: R${balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    elif choice == 3:
        withdraw_amount = float(input("Enter the amount to withdraw: R$"))
        if withdraw_amount > balance:
            print("Insufficient funds for this withdrawal.")
        elif withdraw_amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            balance -= withdraw_amount
            print(f"Withdrew R${withdraw_amount:.2f}. New balance: R${balance:.2f}")
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 4.")

print(50 * "-")
print("""Exercise 5 — Grade Report with a Dictionary Given this dictionary:

grades = {
    "Alice": 92,
    "Bruno": 78,
    "Carla": 85,
    "Daniel": 59
}
Loop over it and print:

Each student's name and grade
Whether each student passed (grade >= 60)
The class average""")
print(50 * "-")

grades = {
    "Alice": 92,
    "Bruno": 78,
    "Carla": 85,
    "Daniel": 59
}
total_grade = 0
for student, grade in grades.items():
    total_grade += grade
    status = "Passed" if grade >= 60 else "Failed"
    print(f"{student}: {grade} - {status}")
class_average = total_grade / len(grades)
print(f"Class average: {class_average:.2f}")