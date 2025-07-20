import streamlit as st
import pandas as pd
import plotly.express as px

# Load scored dataset
df = pd.read_csv("data/processed/scored_mci.csv")

# Title
st.set_page_config(page_title="Pretups Deployment Dashboard", layout="wide")
st.title("📊 Pretups Deployment Feasibility Dashboard")
st.markdown("Explore **Country Readiness** and **Sustainability** scores derived from Mobile Connectivity Index (MCI) data.")

# Sidebar Filters
st.sidebar.header("🔍 Filter Options")
selected_region = st.sidebar.selectbox("Select Region", options=["All"] + sorted(df["Region"].dropna().unique().tolist()))
if selected_region != "All":
    df = df[df["Region"] == selected_region]

selected_cluster = st.sidebar.multiselect("Select Cluster(s)", options=sorted(df["Cluster"].unique().tolist()), default=sorted(df["Cluster"].unique().tolist()))
df = df[df["Cluster"].isin(selected_cluster)]

# Country Selector
selected_country = st.selectbox("🌐 Select a Country", df["Country"].unique())

# ------------------------------
# 📌 Country-wise Detailed Table
# ------------------------------
st.subheader(f"📄 Detailed Scores for {selected_country}")
country_data = df[df["Country"] == selected_country]

# Apply .highlight_max() safely to only numeric columns
numeric_cols = country_data.select_dtypes(include='number').columns
styled_country_data = country_data.style.highlight_max(axis=1, subset=numeric_cols)
st.dataframe(styled_country_data)

# ------------------------------
# 📈 Scatter Plot: Readiness vs Sustainability
# ------------------------------
st.subheader("📈 Readiness vs Sustainability Score (All Countries)")
fig_scatter = px.scatter(
    df,
    x="Readiness Score",
    y="Sustainability Score",
    color="Cluster",
    hover_name="Country",
    size="Index",
    title="Readiness vs Sustainability by Country",
    template="plotly_white"
)
st.plotly_chart(fig_scatter, use_container_width=True)

# ------------------------------
# 📊 Top 10 Countries by Scores
# ------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top 10 Countries by Readiness Score")
    top_readiness = df.sort_values("Readiness Score", ascending=False).head(10)
    st.dataframe(top_readiness[["Country", "Readiness Score", "Cluster"]].reset_index(drop=True))

with col2:
    st.subheader("🌱 Top 10 Countries by Sustainability Score")
    top_sustainability = df.sort_values("Sustainability Score", ascending=False).head(10)
    st.dataframe(top_sustainability[["Country", "Sustainability Score", "Cluster"]].reset_index(drop=True))

# ------------------------------
# 📍 World Map (Optional)
# ------------------------------
st.subheader("🗺️ Global View of Scores")

fig_map = px.choropleth(
    df,
    locations="ISO Code",
    color="Readiness Score",
    hover_name="Country",
    title="Global Readiness Score Map",
    color_continuous_scale="Blues",
    template="plotly_white"
)
st.plotly_chart(fig_map, use_container_width=True)


# Footer
st.markdown("---")
st.markdown("Developed as part of the **Pretups Deployment Feasibility Project** | Data: Mobile Connectivity Index")
