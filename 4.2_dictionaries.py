"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a marketing campaign stored in a dictionary.
# 2. Process: The program reads one field, changes one field, removes one field,
# checks for a field that does not exist, and displays all remaining fields.
# 3. Out: The updated campaign information and all remaining fields with their values.
# 4. My object, my five fields, and why those:
# My object is a marketing campaign. I chose campaign name, budget, channel,
# target audience, and duration because these are useful details for planning
# and managing a real marketing campaign.


# Your code below
campaign = {
    "name": "Summer Fashion Campaign",
    "budget": 2500,
    "channel": "Instagram",
    "target_audience": "Young adults",
    "duration": "4 weeks"
}

# Read one field
print("Campaign name:", campaign["name"])

# Change one field
campaign["budget"] = 3000
print("Updated budget:", campaign["budget"])

# Remove one field
del campaign["duration"]

# Check a field that does not exist
print("Campaign location:", campaign.get("location", "Location not available"))

# Display every remaining field and its value
print("Final campaign details:")
for field, value in campaign.items():
    print(field, ":", value)

# Check: When I asked for the "location" field, it did not exist.
# The program displayed "Location not available" instead of stopping with an error.