# TASK 2: Clean the Data & Save as CSV

import pandas as pd

# Step 1: Load JSON file
file_path = "data/trends_20260407.json"   # file name 

df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}")

# Step 2: Remove duplicates (same post_id)
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Step 3: Remove missing values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Step 4: Fix data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Step 5: Remove low quality data (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Step 6: Clean whitespace from title
df["title"] = df["title"].str.strip()

# Step 7: Save cleaned data to CSV
output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")

# Step 8: Print summary (stories per category)
print("\nStories per category:")
print(df["category"].value_counts())