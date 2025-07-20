import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

print("📥 Loading dataset...")

# Step 1: Read raw CSV, skip top 2 header rows
df = pd.read_csv("data/processed/processed_mci_index_scores.csv", header=2)

# Step 2: Drop completely empty columns (optional cleanup)
df = df.dropna(axis=1, how='all')

# Step 3: Drop rows where country name is missing
df = df.dropna(subset=["Country"], how="any")

print(f"✅ Dataset shape: {df.shape}")
print("📊 Columns in dataset:", df.columns.tolist()[:10], "...")

# Step 4: Select numeric features for clustering (excluding non-numeric columns like ISO, Country)
exclude_cols = ["ISO Code", "Country", "Year"]
feature_cols = [col for col in df.columns if col not in exclude_cols and df[col].dtype in ['float64', 'int64']]

X = df[feature_cols].dropna()

# Step 5: Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 6: Apply KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

df = df.loc[X.index]  # align with rows used for clustering
df["Cluster"] = clusters

# Step 7: Save clustered data
df.to_csv("data/processed/clustered_mci.csv", index=False)
print("✅ Clustered dataset saved at: data/processed/clustered_mci.csv")
