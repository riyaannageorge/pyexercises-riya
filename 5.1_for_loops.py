"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The eight monthly marketing campaign budgets from exercise 4.0.
# 2. Process: The program loops through each budget, records its position,
# and calculates its percentage share of the total budget.
# 3. Out: One line for each campaign budget showing its position,
# budget amount, and percentage share of the total.
# 4. What I compute for each item, and why it is worth showing:
# I compute each budget's share of the total because it shows how much
# of the overall marketing budget is allocated to each campaign.


# Your code below
campaign_budgets = [1200, 2500, 1800, 3200, 1500, 2800, 2100, 3500]

total_budget = sum(campaign_budgets)

for position, budget in enumerate(campaign_budgets, start=1):
    share = (budget / total_budget) * 100
    print("Position", position, "- Budget:", budget, "- Share:", round(share, 2), "%")

# Check: The program printed exactly 8 lines, one for each budget in the list.
# This confirms there was no extra or missing iteration in the loop.