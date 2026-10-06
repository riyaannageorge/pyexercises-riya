"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user's answer to whether they approve a marketing campaign.
# 2. Process: The program keeps asking for an answer until the user enters yes
# or the maximum number of attempts is reached.
# 3. Out: A summary showing the number of attempts and whether approval was received.
# 4. My stop condition, my attempt limit, my summary:
# The stop condition is entering "yes". The maximum is 3 attempts.
# The summary shows how many attempts were used and whether the campaign was approved.


# Your code below
attempts = 0
max_attempts = 3
approved = False

while attempts < max_attempts and not approved:
    answer = input("Do you approve the campaign? ").strip().lower()
    attempts += 1

    if answer == "yes":
        approved = True
        print("Campaign approved.")
    else:
        print("Approval not received.")

print("Summary:")
print("Attempts used:", attempts)

if approved:
    print("The campaign was approved.")
else:
    print("The maximum number of attempts was reached without approval.")
# Check: When I entered "YES" with extra spaces, the program recognized it as "yes".
# The campaign was approved after 1 attempt, as intended.
# When I entered "no" three times, the program stopped after the maximum of 3 attempts.
