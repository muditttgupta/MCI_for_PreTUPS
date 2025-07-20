# reports/generate_reports.py
import pandas as pd
import os

os.makedirs("data/reports", exist_ok=True)

df = pd.read_csv("data/processed/scored_mci.csv")

# Summary Stats
df.describe().to_csv("data/reports/summary_statistics.csv")

# Cluster Summary
cluster_summary = df.groupby("Cluster").agg({
    "Country": "count",
    "Index": "mean",
    "Infrastructure": "mean",
    "Affordability": "mean"
}).rename(columns={"Country": "Country_Count"})
cluster_summary.to_csv("data/reports/cluster_summary.csv")

# Feasibility Summary
feasibility_summary = df["Potential Deployment"].value_counts()
feasibility_summary.to_csv("data/reports/deployment_summary.csv")

# Top Countries
top_countries = df.sort_values(by="Index", ascending=False).head(10)
top_countries.to_csv("data/reports/top_countries.csv", index=False)

# Region-wise feasibility
region_summary = df.groupby(["Region", "Potential Deployment"]).size().unstack().fillna(0)
region_summary.to_csv("data/reports/region_feasibility.csv")
