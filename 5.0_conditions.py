"""Exercise 5.0 — Making the program decide

WHAT THE PROGRAM MUST DO
    Ask the user for a number, then display a different message depending on which
    range that number falls into. At least four ranges.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your four ranges, what are their exact boundaries, and what does each
       message say? Write the boundaries down before you code them.

WHAT THE AI CANNOT KNOW
    Your ranges and your boundaries. It can be an age, a budget, a satisfaction score,
    a delivery time. Choose something with a real meaning and defend the cut-off points.

    Boundaries are where programs go wrong. Decide explicitly whether a value exactly
    on the boundary belongs to the range above or the one below.

CHECK IT YOURSELF
    Test each of your boundary values exactly: if one range ends at 25, run it with 25.
    Then with 24 and 26. Write in a comment whether each landed where you intended.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A campaign satisfaction score entered by the user.
# 2. Process: The program checks which score range the number belongs to.
# 3. Out: A message describing the campaign performance.
# 4. My ranges, my boundaries, my messages:
# 0-49: "Needs improvement"
# 50-69: "Below expectations"
# 70-84: "Good performance"
# 85-100: "Excellent performance"


# Your code below
satisfaction_score = int(input("Enter the campaign satisfaction score (0-100): "))

if satisfaction_score < 0 or satisfaction_score > 100:
    print("Please enter a score between 0 and 100.")
elif satisfaction_score <= 49:
    print("Needs improvement")
elif satisfaction_score <= 69:
    print("Below expectations")
elif satisfaction_score <= 84:
    print("Good performance")
else:
    print("Excellent performance")

# Check: The boundary values worked as intended.
# 49 was "Needs improvement" and 50 was "Below expectations".
# 69 was "Below expectations" and 70 was "Good performance".
# 84 was "Good performance" and 85 was "Excellent performance".
# Values below 0 or above 100 displayed the invalid-score message.