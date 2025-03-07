import sqlite3
import pandas as pd

# Load CSV file
csv_file = 'profile.csv'
df = pd.read_csv(csv_file)

# Connect to SQLite database
conn = sqlite3.connect('profiles.db')
cursor = conn.cursor()

# Create table dynamically based on CSV structure
columns = ', '.join([f'"{col}" TEXT' for col in df.columns])
cursor.execute(f'CREATE TABLE IF NOT EXISTS profiles ({columns});')

# Insert data into the table
df.to_sql('profiles', conn, if_exists='replace', index=False)

# Fetch and display the data
cursor.execute('SELECT * FROM profiles LIMIT 10;')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()