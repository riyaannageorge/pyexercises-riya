"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A number N entered by the user.
# 2. Process: The program checks each number from 1 to N and determines whether it is odd or even.
# 3. Out: A message for each number saying whether it is odd or even.
# 4. What happens on 0, on a negative number, on a very large number:
# 0: The program displays a message and stops.
# Negative number: The program displays a message and stops.
# 5000: The program displays a message that the number is too large and stops.

# Your code below
number = int(input("Enter a number: "))

if number == 0:
    print("The number must be positive. The program will stop.")
elif number < 0:
    print("The number must be positive. The program will stop.")
elif number >= 5000:
    print("The number is too large. The program will stop.")
else:
    for i in range(1, number + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
