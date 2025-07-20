import pandas as pd

print("📥 Loading clustered dataset...")
df = pd.read_csv("data/processed/clustered_mci.csv")

# OPTIONAL: Print cluster distribution
print("\n📊 Cluster distribution:")
print(df["Cluster"].value_counts())

# Example scoring logic: Assume cluster 0 is most ready, cluster 3 least
cluster_scores = {
    0: {"readiness_score": 90, "sustainability_score": 85},
    1: {"readiness_score": 70, "sustainability_score": 75},
    2: {"readiness_score": 60, "sustainability_score": 65},
    3: {"readiness_score": 45, "sustainability_score": 50},
}

# Assign scores
df["Readiness Score"] = df["Cluster"].map(lambda x: cluster_scores[x]["readiness_score"])
df["Sustainability Score"] = df["Cluster"].map(lambda x: cluster_scores[x]["sustainability_score"])

# Flag deployment-worthy countries (custom rule)
df["Potential Deployment"] = df["Readiness Score"].apply(lambda x: "Yes" if x >= 70 else "No")

# Save
output_path = "data/processed/scored_mci.csv"
df.to_csv(output_path, index=False)
print(f"\n✅ Scored dataset saved at: {output_path}")
