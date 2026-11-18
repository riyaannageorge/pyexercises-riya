
import csv

from datetime import datetime

# This function reads campaign information from the CSV file
def read_campaigns(filename):
    campaigns = []

    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            campaigns.append(row)

    return campaigns

# This function calculates the performance of each campaign
def calculate_metrics(campaigns):
    results = []

    for campaign in campaigns:

        # Skip campaigns with empty impressions
        if campaign["Impressions"].strip() == "":
            continue

        # Convert the European decimal comma into a dot
        impressions = float(campaign["Impressions"])
        clicks = float(campaign["Clicks"])
        cost = float(campaign["Cost (€)"].replace(",", "."))
        conversions = float(campaign["Conversions"])
        revenue = float(campaign["Revenue (€)"].replace(",", "."))

        # Calculate CTR
        ctr = clicks / impressions

        # Calculate CPA only when conversions are not zero
        if conversions == 0:
            cpa = None
        else:
            cpa = cost / conversions

        # Calculate ROAS
        if cost == 0:
            roas = None
        else:
            roas = revenue / cost

        # Store the campaign results
        results.append({
            "Campaign": campaign["Campaign"],
            "Channel": campaign["Channel"],
            "CTR": ctr,
            "CPA": cpa,
            "ROAS": roas,
            "Conversions": conversions,
        })

    return results

# This function asks the player to enter their name
def get_player_name():
    name = input("Enter your name: ").strip()

    while name == "":
        print("Please enter a valid name.")
        name = input("Enter your name: ").strip()

    return name
# This function asks five questions about campaign performance
def run_quiz(results):
    score = 0

    # Find the correct answers using the campaign data
    best_ctr = max(results, key=lambda x: x["CTR"])

    campaigns_with_cpa = [c for c in results if c["CPA"] is not None]
    highest_cpa = max(campaigns_with_cpa, key=lambda x: x["CPA"])

    high_roas_count = sum(1 for c in results if c["ROAS"] is not None and c["ROAS"] > 3)

    channel_conversions = {}
    for campaign in results:
        channel = campaign["Channel"]
        channel_conversions[channel] = channel_conversions.get(channel, 0) + campaign["Conversions"]

    best_channel = max(channel_conversions, key=channel_conversions.get)

    average_ctr = round(sum(c["CTR"] * 100 for c in results) / len(results), 2)

    # Ask the five quiz questions
    print("\n===== CAMPAIGN AUDIT QUIZ =====")

    answer = input("1. Which campaign has the best CTR? ")
    if answer.strip().lower() == best_ctr["Campaign"].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", best_ctr["Campaign"])

    answer = input("2. Which campaign has the highest CPA? ")
    if answer.strip().lower() == highest_cpa["Campaign"].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", highest_cpa["Campaign"])

    answer = input("3. How many campaigns have a ROAS above 3? ")
    if answer.strip() == str(high_roas_count):
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", high_roas_count)

    answer = input("4. Which channel generated the most conversions? ")
    if answer.strip().lower() == best_channel.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", best_channel)

    answer = input("5. What is the average CTR (%) rounded to two decimals? ")
    try:
        if round(float(answer), 2) == average_ctr:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Correct answer:", average_ctr)
    except ValueError:
        print("Invalid answer. Correct answer:", average_ctr)

    print("\n===== QUIZ RESULTS =====")
    print("Your score:", score, "/ 5")

    return score

# This function saves the player's name, score and date
def save_result(name, score):
    with open("result.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Player Name", "Score", "Date"])
        writer.writerow([name, score, datetime.now().strftime("%Y-%m-%d")])

# Test the campaign calculations
if __name__ == "__main__":
    campaigns = read_campaigns("campaigns_A.csv")

    results = calculate_metrics(campaigns)

    print("Campaign calculations completed!")

for campaign in results:
    print("------------------------------")
    print("Campaign:", campaign["Campaign"])
    print("Channel:", campaign["Channel"])
    print("CTR:", round(campaign["CTR"] * 100, 2), "%")
    print("CPA:", round(campaign["CPA"], 2) if campaign["CPA"] is not None else "N/A")
    print("ROAS:", round(campaign["ROAS"], 2) if campaign["ROAS"] is not None else "N/A")


# Overall campaign performance summary
print("\n===== OVERALL PERFORMANCE SUMMARY =====")

valid_campaigns = [c for c in results if c["ROAS"] is not None]

if valid_campaigns:
    best_campaign = max(valid_campaigns, key=lambda x: x["ROAS"])

    print("Best Campaign:", best_campaign["Campaign"])
    print("Best ROAS:", round(best_campaign["ROAS"], 2))
    # Ask for the player's name
player_name = get_player_name()

# Start the quiz
score = run_quiz(results)

# Save the result
save_result(player_name, score)

print("Your result has been saved successfully!")