import pandas as pd
import mysql.connector

# Load CSV file
csv_file = 'profiles.csv'
df = pd.read_csv(csv_file)

# Connect to MySQL without specifying a database first
conn = mysql.connector.connect(
    host="localhost",
    user="Kaifqureshi220",
    password="Mohd@7860"
)
cursor = conn.cursor()

# Step 1: Create Database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS Profile_Twitter;")
cursor.execute("USE Profile_Twitter;")

# Step 2: Create Table dynamically based on CSV structure
columns = ', '.join([f'`{col}`Text' for col in df.columns])
cursor.execute(f'CREATE TABLE IF NOT EXISTS profiles ({columns});')

# Step 3: Insert Data from CSV into the Table
for _, row in df.iterrows():
    values = tuple(row.astype(str))
    placeholders = ', '.join(['%s'] * len(row))
    cursor.execute(f'INSERT INTO profiles VALUES ({placeholders})', values)

# Commit changes
conn.commit()

# Step 4: Perform SQL queries to check inserted data
cursor.execute('SELECT * FROM profiles LIMIT 10;')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('SELECT Distinct Follower from Profiles;')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
