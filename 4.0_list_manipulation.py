"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Eight monthly marketing campaign budgets.
# 2. Process: The program displays the full list, one budget of my choice,
# sorts the budgets, and calculates the average budget.
# 3. Out: The original list, one selected budget, the sorted list, and the average.
# 4. What my list is about, and what I computed from it:
# My list represents monthly budgets for different marketing campaigns.
# I computed the average budget because it helps compare the typical campaign spending.
# Check: For the first three budgets, (1200 + 2500 + 1800) / 3 = 1833.33.
# This confirms the average calculation method works correctly.

# Your code below
campaign_budgets = [1200, 2500, 1800, 3200, 1500, 2800, 2100, 3500]

print("All campaign budgets:", campaign_budgets)

print("One budget I chose:", campaign_budgets[2])

sorted_budgets = sorted(campaign_budgets)
print("Sorted budgets:", sorted_budgets)

average_budget = sum(campaign_budgets) / len(campaign_budgets)
print("Average budget:", average_budget)
