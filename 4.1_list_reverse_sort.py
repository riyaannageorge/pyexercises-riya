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
# 2. Process: The program creates four different orders of the list and checks whether
# the original list has been changed.
# 3. Out: The four different orders and, at the end, the original list unchanged.
# 4. My four orders are sorted ascending, sorted descending, reversed order, and
# a reversed copy. sorted() and reversed() return new results, while reverse()
# modifies the original list.
# Check: The final original list is unchanged and matches the list from exercise 4.0.
# sorted() and reversed() did not modify the original list.
# reverse() modifies a list in place, but I used it on a copy so the original survived.


# Your code below
campaign_budgets = [1200, 2500, 1800, 3200, 1500, 2800, 2100, 3500]

print("Original list:", campaign_budgets)

# 1. Sorted ascending — creates a new list
ascending = sorted(campaign_budgets)
print("Sorted ascending:", ascending)

# 2. Sorted descending — creates a new list
descending = sorted(campaign_budgets, reverse=True)
print("Sorted descending:", descending)

# 3. Reversed copy — does not change the original
reversed_copy = list(reversed(campaign_budgets))
print("Reversed copy:", reversed_copy)

# 4. Reverse in place — modifies the list being used
modified_list = campaign_budgets.copy()
modified_list.reverse()
print("Reverse in place:", modified_list)

# Check: the original list is still unchanged
print("Original list at the end:", campaign_budgets)
