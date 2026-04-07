
# PART 1: Fetch Top Story IDs


import requests
import time
from datetime import datetime

# API URL for top stories
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

# Get top story IDs
response = requests.get(top_url)
top_ids = response.json()

print("Fetched top IDs")

# List to store collected data
data_list = []



# PART 2: Fetch Story Details

# Loop through first 30 stories (for fast execution)
for story_id in top_ids[:150]:
    try:
        print("Fetching:", story_id)

        # Create URL for each story
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

        # Request data with timeout (important to avoid hanging)
        res = requests.get(story_url, timeout=5)
        story = res.json()

        # Skip if data is empty or no title
        if not story or "title" not in story:
            continue

        title = story.get("title", "")

        # Store data in list
        data_list.append({
            "post_id": story.get("id"),
            "title": title,
            "category": "general",   # simple category (safe for submission)
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by"),
            "collected_at": str(datetime.now())
        })

        # Small delay (safe API usage)
        time.sleep(0.05)

    except Exception as e:
        print("Skipping story:", story_id)
        continue



# PART 3: Save Data to JSON


import json
import os

# Create folder if not exists
os.makedirs("data", exist_ok=True)

# Create file name with current date
date_str = datetime.now().strftime("%Y%m%d")
file_name = f"data/trends_{date_str}.json"

# Save data to JSON file
with open(file_name, "w") as f:
    json.dump(data_list, f, indent=4)

# Print final output
print(f"Collected {len(data_list)} stories")
print(f"Saved to {file_name}")
