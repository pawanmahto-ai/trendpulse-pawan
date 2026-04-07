# TASK 3: Analysis with Pandas & NumPy

import pandas as pd
import numpy as np

# Step 1: Load cleaned CSV file
file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)

print(f"Loaded data shape: {df.shape}")

# Print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Print average values
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score: {avg_score:.2f}")
print(f"Average comments: {avg_comments:.2f}")


# Step 2: Basic analysis using NumPy

scores = df["score"].values

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

print("\n--- NumPy Stats ---")
print(f"Mean score: {mean_score:.2f}")
print(f"Median score: {median_score:.2f}")
print(f"Std deviation: {std_score:.2f}")

# Highest & lowest score
print(f"Max score: {np.max(scores)}")
print(f"Min score: {np.min(scores)}")

# Category with most stories
top_category = df["category"].value_counts().idxmax()
top_count = df["category"].value_counts().max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# Story with most comments
max_comment_row = df.loc[df["num_comments"].idxmax()]

print("\nMost commented story:")
print(f"{max_comment_row['title']} - {max_comment_row['num_comments']} comments")


# Step 3: Add new columns

# Engagement = comments per score
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular if score > average
df["is_popular"] = df["score"] > avg_score


# Step 4: Save result to CSV
output_path = "data/trends_analysed.csv"

df.to_csv(output_path, index=False)

print(f"\nSaved analysed data to {output_path}")