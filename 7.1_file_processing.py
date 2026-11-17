"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Some first names are lowercase instead of starting with a capital letter.
# - Some last names are all uppercase instead of normal capitalization.
# - There are blank lines between some names.
# - Some names have inconsistent capitalization, such as "GUIDO van rossum".

# 1. In: The names stored in names.txt, including blank lines and inconsistent capitalization.
# 2. Process, problem by problem:
# Blank lines are ignored.
# Names are cleaned by removing extra spaces and using consistent capitalization.
# The cleaned names are sorted alphabetically by last name.
# The original names.txt file is not changed.
# 3. Out: A new file containing the cleaned names sorted by last name.
# 4. How I decide which word is the last name:
# For a name with two words, the second word is the last name.
# For "Guido van rossum", the final word "rossum" is treated as the last name.


# Your code below
# Read the original names.txt file without changing it
with open("names.txt", "r") as file:
    lines = file.readlines()

# Remove blank lines and clean the names
cleaned_names = []

for line in lines:
    name = line.strip()

    if name:
        words = name.split()
        cleaned_name = " ".join(word.capitalize() for word in words)
        cleaned_names.append(cleaned_name)

# Sort the names by the last word in each name
cleaned_names.sort(key=lambda name: name.split()[-1])

# Write the cleaned and sorted names to a new file
with open("names_cleaned_sorted.txt", "w") as file:
    for name in cleaned_names:
        file.write(name + "\n")

# Check: the original names.txt file was not modified
# The output contains only non-empty, cleaned names sorted by last name.

print("Cleaned and sorted names saved successfully.")
