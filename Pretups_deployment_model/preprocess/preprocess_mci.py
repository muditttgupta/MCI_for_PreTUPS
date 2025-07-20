# preprocess_mci.py (passthrough version)
import pandas as pd
import shutil
import os

input_path = 'data/raw/mci_index_scores.csv'

output_path = 'data/processed/processed_mci_index_scores.csv'

# Simply copy the file if no cleaning needed
df = pd.read_csv(input_path)
df.to_csv(output_path, index=False)
print(f"✅ No preprocessing needed. File copied to {output_path}")
