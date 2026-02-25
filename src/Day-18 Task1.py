import sqlite3
import pandas as pd

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
);
""")
cursor.execute("DELETE FROM interns;")  

cursor.executemany("""
INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?);
""", [
    ('Aarav Sharma', 'Data Science', 15000),
    ('Priya Patel', 'Web Development', 12000),
    ('Rohan Mehta', 'Data Science', 18000),
    ('Sneha Iyer', 'UI/UX Design', 10000),
    ('Karan Verma', 'Cyber Security', 20000)
])

conn.commit()

filter_query = """
SELECT name, track, stipend
FROM interns
WHERE track = 'Data Science'
AND stipend > 5000;
"""

df_filter = pd.read_sql_query(filter_query, conn)

print("\n🔹 Data Science Interns with stipend > 5000:\n")
print(df_filter)

avg_query = """
SELECT track, AVG(stipend) AS average_stipend
FROM interns
GROUP BY track;
"""

df_avg = pd.read_sql_query(avg_query, conn)

print("\n🔹 Average Stipend per Track:\n")
print(df_avg)

count_query = """
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track;
"""

df_count = pd.read_sql_query(count_query, conn)

print("\n🔹 Total Interns per Track:\n")
print(df_count)

conn.close()