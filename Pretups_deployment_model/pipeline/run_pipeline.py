import os
import glob
import subprocess

def delete_files_in_folder(folder_path):
    files = glob.glob(os.path.join(folder_path, '*.csv'))
    for file in files:
        os.remove(file)
        print(f"✅ Deleted: {file}")

def run_script(path):
    print(f"🚀 Running: {path}")
    subprocess.run(["python3", path], check=True)

if __name__ == "__main__":
    print("🔁 Running Full Pipeline...")

    # Step 1: Clean previous outputs
    print("🧹 Cleaning old outputs...")
    delete_files_in_folder("data/processed")

    # Step 2: Run preprocessing
    run_script("preprocess/preprocess_mci.py")

    # Step 3: Run clustering model
    run_script("models/model_mci.py")

    # Step 4: Run scoring module
    run_script("scoring/score_mci.py")

    # Step 5: Generate reports
    run_script("reports/generate_reports.py")

    print("✅ Full pipeline executed successfully.")
