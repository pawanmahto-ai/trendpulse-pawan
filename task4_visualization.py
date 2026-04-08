import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned CSV data
file_path = "data/trends_clean.csv"
df = pd.read_csv(file_path)
print(df.columns)

# Print shape of data (rows, columns)
print(f"Loaded data with shape: {df.shape}")

# Create outputs folder if it does not exist
if not os.path.exists("outputs"):
    os.makedirs("outputs")


# Chart 1: Top 10 stories by scor

# Sort data by score and take top 10
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles so they fit in chart
top10["title"] = top10["title"].apply(
    lambda x: x[:25] + "..." if len(x) > 25 else x
)

# Create horizontal bar chart
plt.figure(figsize=(20, 10))
plt.barh(top10["title"], top10["score"])

# Add labels and title
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")

# Show highest value on top
plt.gca().invert_yaxis()

# Increase left space so text is visible
plt.subplots_adjust(left=0.5)

# Save chart
plt.savefig("outputs/chart1_top_stories.png")
plt.close()


# Chart 2: Number of stories per category


# Count how many stories in each category
category_counts = df["category"].value_counts()

# Create bar chart
plt.figure(figsize=(8, 6))
plt.bar(category_counts.index, category_counts.values)

# Add labels and title
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

# Save chart
plt.savefig("outputs/chart2_categories.png")
plt.close()


# Chart 3: Score vs Comments


# Split data into popular and not popular
popular = df[df["score"] > 500]
not_popular = df[df["score"] <= 500]

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

# Add labels and title
plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")

# Show legend
plt.legend()

# Save chart
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# Dashboard: Combine all charts


# Create 3 subplots in one row
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Chart 1 inside dashboard
axs[0].barh(top10["title"], top10["score"])
axs[0].set_title("Top Stories")
axs[0].invert_yaxis()

# Chart 2 inside dashboard
axs[1].bar(category_counts.index, category_counts.values)
axs[1].set_title("Categories")

# Chart 3 inside dashboard
axs[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axs[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axs[2].set_title("Score vs Comments")
axs[2].legend()

# Add main title
plt.suptitle("TrendPulse Dashboard")

# Adjust spacing between charts
plt.subplots_adjust(left=0.3, wspace=0.4)

# Save dashboard
plt.savefig("outputs/dashboard.png")
plt.close()

# Final message
print("All charts saved in outputs folder")