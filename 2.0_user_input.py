"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A product name and the quantity ordered.
# 2. Process:The program asks the user for both pieces of information and uses them in a sentence.
# 3. Out:A sentence showing the product name and the quantity ordered.
# 4. My two fields, and what I would do with them:I chose a product name and quantity ordered
# because they could be used in a form to record and describe a customer order.
# Check: When I entered an empty line for the quantity, the program gave a ValueError
# because an empty input cannot be converted to an integer.
# Check: When I entered a space for the quantity, the program gave a ValueError
# because a space cannot be converted to an integer.
# Check: When I entered text instead of a number, the program gave a ValueError
# because the text could not be converted to an integer.
# Your code below
product_name = input("Enter the product name: ")
quantity = int(input("Enter the quantity ordered: "))

print(f"The customer ordered {quantity} {product_name}.")
print(f"If one more is ordered, the quantity will be {quantity + 1}.")
