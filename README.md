# 📊 Predictive Modeling for Country-Wise Deployment and Sustainability using Mobile Connectivity Index (MCI) for PreTUPS

**Repository:** `MCI_for_Pretups`  
**Author:** Mudit Gupta  
**Organization:** Comviva – PreTUPS Engineering  
**Internship Duration:** June 2025 – July 2025

---

## 🌍 Project Overview

This project delivers an end-to-end AI/ML solution to assess **country-wise readiness** and **sustainability** for PreTUPS deployment using GSMA's **Mobile Connectivity Index (MCI)** data. PreTUPS, Comviva's flagship recharge and distribution platform, aims to expand globally — and this model helps **strategically identify which countries are viable for new deployments** based on MCI indicators.

The model uses **clustering and scoring algorithms** to analyze infrastructure, affordability, digital skills, and services across countries and years. The final output flags countries with **high deployment feasibility**, enabling **data-driven business expansion strategies**.

---

## 🚀 AIML Use Cases

- 📈 **Predictive Deployment Readiness**: Identify countries most suitable for new PreTUPS deployments based on cluster-based scoring.
- 🧮 **Sustainability Indexing**: Estimate long-term viability using social, economic, and infrastructure readiness scores.
- 📊 **Country Profiling via ML Clustering**: Use unsupervised learning (KMeans) to group countries into meaningful deployment categories.
- 🧠 **Data-Driven Decision Support**: Equip product and strategy teams with a dashboard to make intelligent, MCI-based deployment calls.

---

## 🗂️ Folder Structure

```plaintext
MCI_for_Pretups/
│
├── data/
│   └── raw/                        # Raw MCI CSV data
│   └── processed/                 # Processed, clustered, and scored datasets
│
├── preprocess/
│   └── preprocess_mci.py         # Cleans and prepares raw MCI data
│
├── models/
│   └── model_mci.py              # Applies KMeans clustering to MCI features
│
├── scoring/
│   └── score_mci.py              # Assigns readiness/sustainability scores based on clusters
│
├── reports/
│   └── generate_report.py        # (Optional) Generates summary reports
│
├── dashboard/
│   └── dashboard.py              # Streamlit-based interactive dashboard
│
├── notebooks/
│   └── eda_mci.ipynb             # EDA and cluster visualization
│
├── pipeline/
│   └── run_pipeline.py           # Full automation script for end-to-end execution
│
└── README.md                     # This file
```
## 🧠 Modeling Approach

### ✅ Feature Selection
- Dropped irrelevant columns like `Country`, `ISO Code`, `Year`
- Used numerical MCI indicators like:
  - Infrastructure
  - Affordability
  - Consumer Readiness
  - Content and Services
  - Internet speed, literacy, penetration metrics

---

### 🌀 Clustering Logic (Unsupervised Learning)
- **Model:** KMeans
- **Clusters:** 4 (based on elbow method/intuition)
- **Preprocessing:** Scaled features using `StandardScaler`

#### 📊 Cluster output example:

| Cluster | Readiness Score | Sustainability Score |
|---------|------------------|-----------------------|
| 0       | 90               | 85                    |
| 1       | 70               | 75                    |
| 2       | 60               | 65                    |
| 3       | 45               | 50                    |

---

### 🏁 Scoring Logic
- Readiness and sustainability scores mapped directly from cluster label
- Countries with **Readiness Score ≥ 70** are flagged as **Potential Deployment = Yes**
- Final output saved as: `scored_mci.csv`

---

## 📊 Streamlit Dashboard Highlights

📍 **File:** `dashboard/dashboard.py`  
An intuitive, interactive dashboard for strategic decision-makers.

### ✅ Key Features:
- Year-wise filtering
- Region-wise breakdown
- Country-wise readiness and sustainability heatmaps
- Cluster distribution and insights
- Deployment feasibility flag (`Yes/No`)

> 🔎 Visualize which countries are ready, which are emerging, and which are not currently feasible.

---

## 🔁 End-to-End Pipeline

All steps are fully automated via a single command:

```bash
python pipeline/run_pipeline.py
```
---

### ⚙️ Steps executed:
1. Clean old outputs  
2. Preprocess MCI data  
3. Cluster countries using ML  
4. Score readiness & sustainability  
5. *(Optional)* Generate analytical reports  
6. *(Optional)* Launch interactive Streamlit dashboard  

---

## 📌 Example Output (`scored_mci.csv`)

| Country | Year | Cluster | Readiness Score | Sustainability Score | Potential Deployment |
|---------|------|---------|------------------|-----------------------|-----------------------|
| India   | 2020 | 0       | 90               | 85                    | Yes                   |
| Nepal   | 2020 | 3       | 45               | 50                    | No                    |
| Kenya   | 2021 | 1       | 70               | 75                    | Yes                   |
| Chad    | 2019 | 2       | 60               | 65                    | No                    |

---

## 🧪 Exploratory Data Analysis

**Notebook:** `notebooks/eda_mci.ipynb`

### Visualizations include:
- Count plots of cluster assignments
- Heatmaps and pairplots of MCI indicators
- Year-over-year feature comparisons
- Country-level insights and filtering

---

## 📦 Dependencies

- `pandas`, `numpy`
- `scikit-learn`
- `matplotlib`, `seaborn`
- `streamlit`
- Python ≥ 3.8

**Install with:**

```bash
pip install -r requirements.txt
```

---

## 📍 Use Cases for Comviva

- Strategic expansion of PreTUPS to viable countries
- Long-term investment planning using sustainability analysis
- Dashboard insights for leadership to make MCI-aligned decisions
- Foundation for future supervised ML models (e.g., predictive classification)

---

## ✍️ Author & Acknowledgements

👨‍💻 **Author:** Mudit Gupta  
🎓 **Internship Project at:** Comviva – PreTUPS Engineering  
🗓️ **Duration:** June 2025 – July 2025


---

## 📎 License

This repository is intended for academic, research, and internal evaluation purposes. For commercial use or redistribution, please contact the author or Comviva.

---
