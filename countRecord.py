import sqlite3

# Connect to the SQLite database (replace 'database.db' with your database file)
conn = sqlite3.connect('contracts_merged_index.db')
cursor = conn.cursor()

# Execute the query
cursor.execute("SELECT COUNT(*) AS total_entries FROM file_index")
result = cursor.fetchone()

# Fetch and print the total number of entries
print(f"Total number of entries: {result[0]}")

# Close the connection
conn.close()
