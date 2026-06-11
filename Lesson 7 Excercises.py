print(50 * "-")
print("Exercise 1 — Season Detector Ask the user for a month number (1-12) and print the " \
"season:" \
"Dec, Jan, Feb → Summer (Southern Hemisphere)" \
"Mar, Apr, May → Autumn" \
"Jun, Jul, Aug → Winter" \
"Sep, Oct, Nov → Spring" \
"Other → Invalid")
print(50 * "-")

month_number = int(input("Enter a month number (1-12): "))
if month_number in [12, 1, 2]:
    season = "Summer (Southern Hemisphere)"
elif month_number in [3, 4, 5]:
    season = "Autumn"
elif month_number in [6, 7, 8]:
    season = "Winter"
elif month_number in [9, 10, 11]:
    season = "Spring"
else:
    season = "Invalid"

print(f"The season for month {month_number} is: {season}")

print(50 * "-")
print("Exercise 2 — BMI Calculator Ask for weight (kg) and height (m). Calculate BMI = " \
"weight / height². Print the BMI and the category:" \
"Below 18.5 → Underweight" \
"18.5 – 24.9 → Normal" \
"25.0 – 29.9 → Overweight" \
"30.0 or above → Obese")
print(50 * "-")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25.0 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is: {bmi:.2f}")
print(f"Your category is: {category}")

print(50 * "-")
print("Exercise 3 — Electricity Bill Ask for kWh consumed. Apply the tiered rate:" \
"First 100 kWh: R$0.40/kWh" \
"Next 200 kWh (101–300): R$0.65/kWh" \
"Above 300 kWh: R$0.95/kWh" \
"Print the bill total.")
print(50 * "-")

kwh_consumed = float(input("Enter kWh consumed: "))
if kwh_consumed <= 100:
    bill = kwh_consumed * 0.40
elif kwh_consumed <= 300:
    bill = 100 * 0.40 + (kwh_consumed - 100) * 0.65
else:
    bill = 100 * 0.40 + 200 * 0.65 + (kwh_consumed - 300) * 0.95

print(f"Your electricity bill is: R${bill:.2f}")

print(50 * "-")
print("""Exercise 4 — Rock, Paper, Scissors (vs. Computer) Ask the player for their choice.
Hard-code the computer's choice as "rock".
Print who wins. (Hint: use and / or in your conditions.)""")
print(50 * "-")

player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = "rock"

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")