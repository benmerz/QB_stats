import sqlite3
import csv

# File paths
csv_file = 'bills.csv'
db_file = 'bills.sqlite'
table_name = 'bills'

# Read CSV header
with open(csv_file, 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)

# Create table schema
columns = [f'"{col}" TEXT' for col in header]
schema = f'CREATE TABLE IF NOT EXISTS {table_name} ({", ".join(columns)});'

# Connect to SQLite and create table
conn = sqlite3.connect(db_file)
c = conn.cursor()
c.execute(schema)

# Insert CSV rows
with open(csv_file, 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    rows = [row for row in reader]

placeholders = ','.join(['?'] * len(header))
insert_sql = f'INSERT INTO {table_name} VALUES ({placeholders})'
c.executemany(insert_sql, rows)
conn.commit()
conn.close()

print(f"Imported {len(rows)} rows into {db_file} as table '{table_name}'.")
