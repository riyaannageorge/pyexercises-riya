
import csv
import matplotlib.pyplot as plt

# Read campaign data from the CSV file
campaigns = []

with open("campaigns_A.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter=";")

    for row in reader:
        if row["Impressions"].strip() == "":
            continue

        campaigns.append(row)

# Prepare campaign data for the charts
names = []
ctr_values = []
cpa_values = []
roas_values = []

for campaign in campaigns:
    impressions = float(campaign["Impressions"])
    clicks = float(campaign["Clicks"])
    cost = float(campaign["Cost (€)"].replace(",", "."))
    conversions = float(campaign["Conversions"])
    revenue = float(campaign["Revenue (€)"].replace(",", "."))

    names.append(campaign["Campaign"])
    ctr_values.append((clicks / impressions) * 100)
    cpa_values.append(cost / conversions if conversions != 0 else 0)
    roas_values.append(revenue / cost if cost != 0 else 0)

# Create three campaign performance charts
fig, axes = plt.subplots(3, 1, figsize=(12, 15))

axes[0].bar(names, roas_values)
axes[0].set_title("Campaign ROAS Comparison")
axes[0].set_ylabel("ROAS")
axes[0].tick_params(axis="x", rotation=45)

axes[1].bar(names, ctr_values)
axes[1].set_title("Campaign CTR Comparison")
axes[1].set_ylabel("CTR (%)")
axes[1].tick_params(axis="x", rotation=45)

axes[2].bar(names, cpa_values)
axes[2].set_title("Campaign CPA Comparison")
axes[2].set_ylabel("CPA (€)")
axes[2].tick_params(axis="x", rotation=45)

plt.tight_layout()

# Save the charts as an image
plt.savefig("campaign_performance.png", dpi=300)

plt.show()

print("Campaign visualizations created successfully!")
