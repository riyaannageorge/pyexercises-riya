"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A sentence typed by the user.
# 2. Process: The program applies four different string transformations to the sentence.
# 3. Out: Four transformed versions of the sentence.
# 4. My four transformations, and when each is useful:
# strip() removes extra spaces at the beginning and end of text.
# upper() converts text to uppercase, which can be useful for headings.
# lower() converts text to lowercase, which can be useful for consistent text.
# replace() changes specific text, which can be useful for correcting or updating words.


# Your code below
sentence = input("Enter a sentence: ")

print("strip():", sentence.strip())
print("upper():", sentence.upper())
print("lower():", sentence.lower())
print("replace():", sentence.replace("a", "@"))
# Check: strip() worked as expected and removed the spaces at both ends.
# Check: upper() worked as expected and converted all letters to uppercase.
# Check: lower() worked as expected and converted all letters to lowercase.
# Check: replace() worked as expected and replaced each "a" with "@".
