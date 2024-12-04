import sqlite3

# Define database name and keywords
database_name = "contracts_merged_index.db"
keywords = ["lastTimeRewardApplicable", "rewardPerTokenStored"]

# Connect to the SQLite database
conn = sqlite3.connect(database_name)
cursor = conn.cursor()

# Build the query dynamically for multiple keywords
placeholders = " OR ".join(["content LIKE ?" for _ in keywords])
query = f"SELECT name, path FROM file_index WHERE {placeholders}"

# Execute the query with the keywords
cursor.execute(query, [f"%{kw}%" for kw in keywords])

# Fetch all matching results
results = cursor.fetchall()

# Print the name and path if matches are found
if results:
    print(f"Entries containing keywords {', '.join(keywords)}:")
    for name, path in results:
        print(f"Name: {name}, Path: {path}")
else:
    print(f"No entries found for keywords: {', '.join(keywords)}")

# Close the connection
conn.close()
