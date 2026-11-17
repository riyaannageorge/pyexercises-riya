"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of monthly marketing campaign budgets.
# 2. Process, function by function:
# calculate_total() calculates the total of all campaign budgets.
# find_highest_budget() finds the highest campaign budget.
# find_lowest_budget() finds the lowest campaign budget.
# budget_summary() uses the three functions to answer a question about the budgets.
# 3. Out: The total budget, highest budget, lowest budget, and a final summary.
# 4. The question my fourth function answers:
# What is the overall budget situation for my marketing campaigns?
# Splitting the work into three small functions makes each calculation easier
# to test and understand.


# Your code below
# Function 1: calculate the total budget
def calculate_total(budgets):
    return sum(budgets)


# Function 2: find the highest budget
def find_highest_budget(budgets):
    if len(budgets) == 0:
        return None
    return max(budgets)


# Function 3: find the lowest budget
def find_lowest_budget(budgets):
    if len(budgets) == 0:
        return None
    return min(budgets)


# Function 4: use the three functions together
def budget_summary(budgets):
    total = calculate_total(budgets)
    highest = find_highest_budget(budgets)
    lowest = find_lowest_budget(budgets)

    return (
        f"Total budget: {total} | "
        f"Highest budget: {highest} | "
        f"Lowest budget: {lowest}"
    )


# My marketing campaign budgets from exercise 4.0
campaign_budgets = [1200, 2500, 1800, 3200, 1500, 2800, 2100, 3500]


# Test 1: calculate_total()
# Expected result: 1200 + 2500 + 1800 = 5500
print("Test 1 - Total of first three budgets:", calculate_total(campaign_budgets[:3]))

# Test 2: find_highest_budget()
# Expected result: 3500
print("Test 2 - Highest budget:", find_highest_budget(campaign_budgets))

# Test 3: find_lowest_budget()
# Expected result: 1200
print("Test 3 - Lowest budget:", find_lowest_budget(campaign_budgets))


# Final test: budget_summary() uses the three functions together
print("Final summary:", budget_summary(campaign_budgets))


# Empty-list check
# The functions return 0 or None instead of crashing.
empty_budgets = []

print("Empty list - total:", calculate_total(empty_budgets))
print("Empty list - highest:", find_highest_budget(empty_budgets))
print("Empty list - lowest:", find_lowest_budget(empty_budgets))
print("Empty list - summary:", budget_summary(empty_budgets))

