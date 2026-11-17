"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of monthly marketing campaign budgets.
# 2. Process: The function calculates the average budget in the list.
# 3. Out: The average campaign budget as a number.
# 4. My function name, and why return rather than print:
# My function is called calculate_average_budget because its name clearly explains
# what it calculates. I use return because the result can then be stored and used
# elsewhere, while print only displays it.


# Your code below
def calculate_average_budget(budgets):
    if len(budgets) == 0:
        return None

    return sum(budgets) / len(budgets)


campaign_budgets = [1200, 2500, 1800, 3200, 1500, 2800, 2100, 3500]

print(
    "Average of first three budgets:",
    calculate_average_budget(campaign_budgets[:3])
)

print(
    "Average of first five budgets:",
    calculate_average_budget(campaign_budgets[:5])
)

print(
    "Average of all budgets:",
    calculate_average_budget(campaign_budgets)
)

# Check: When the function was called with an empty list, it returned None.
# This is acceptable because there is no average when there are no budgets.
print("Average of empty list:", calculate_average_budget([]))
