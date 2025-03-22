import os
import json
import re
import datetime

# Paths for the difficulty folders
difficulty_paths = ["easy", "medium", "hard"]

# Regex to match filenames like '0001-two-sum.py'
filename_pattern = re.compile(r"(\d{4})-([a-z0-9-]+)\.py")

# Metadata structure to hold all problem information
metadata = {}

def extract_tags_from_file(file_path):
    """Extracts tags from the solution file's docstring."""
    tags = []
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        # Improved regex to capture tags from multiline docstring
        tag_match = re.search(r"Tags:\s*(.*?)\n", content, re.IGNORECASE)
        if tag_match:
            tags = [tag.strip() for tag in tag_match.group(1).split(',') if tag.strip()]
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
    return tags

def extract_metadata(difficulty, path):
    for filename in os.listdir(path):
        match = filename_pattern.match(filename)
        if match:
            problem_number, problem_title = match.groups()

            # Normalize title
            display_title = problem_title.replace("-", " ").title()

            # Capture modification date
            file_path = os.path.join(path, filename)
            modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d")

            # Extract tags from file
            tags = extract_tags_from_file(file_path)

            if problem_number not in metadata:
                metadata[problem_number] = {
                    "title": display_title,
                    "tags": tags,
                    "difficulty": difficulty,
                    "last_updated": modified_time
                }

            # Keep metadata updated if file changes
            else:
                metadata[problem_number]["tags"] = list(set(metadata[problem_number]["tags"] + tags))
                metadata[problem_number]["last_updated"] = modified_time

def update_metadata():
    for difficulty in difficulty_paths:
        path = os.path.join(os.getcwd(), difficulty)
        if os.path.exists(path):
            extract_metadata(difficulty, path)

    # Write updated metadata to each folder
    for difficulty in difficulty_paths:
        metadata_file = os.path.join(difficulty, ".metadata.json")
        with open(metadata_file, "w") as f:
            json.dump(metadata, f, indent=4, sort_keys=True)

    print("✅ Metadata updated successfully with tags and timestamps!")

if __name__ == "__main__":
    update_metadata()
