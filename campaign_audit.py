
import csv



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
            "ROAS": roas
        })

    return results



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