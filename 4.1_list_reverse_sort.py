"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list of eight monthly marketing campaign budgets from exercise 4.0.
# 2. Process: The program displays the list in four different orders and checks
# whether the original list has been changed.
# 3. Out: The four different orders and the original list at the end.
# 4. My four orders are sorted ascending, sorted descending, reversed copy,
# and reverse in place. sorted() and reversed() create new results without
# modifying the original list. reverse() modifies the original list in place.

# Your code below
campaign_budgets = [1200, 2500, 1800, 3200, 1500, 2800, 2100, 3500]

print("Original list:", campaign_budgets)

# 1. Sorted ascending - creates a new list
ascending = sorted(campaign_budgets)
print("Sorted ascending:", ascending)

# 2. Sorted descending - creates a new list
descending = sorted(campaign_budgets, reverse=True)
print("Sorted descending:", descending)

# 3. Reversed copy - creates a new list
reversed_copy = list(reversed(campaign_budgets))
print("Reversed copy:", reversed_copy)

# 4. Reversed in place - modifies the original list
campaign_budgets.reverse()
print("Reversed in place:", campaign_budgets)

# Restore the original order so the list survives
campaign_budgets.reverse()

# Check: the original list is unchanged at the end
print("Original list at the end:", campaign_budgets)