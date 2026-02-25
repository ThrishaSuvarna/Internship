import sqlite3
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


cursor.execute("""
INSERT INTO interns (name, track, stipend) VALUES
('Aarav Sharma', 'Data Science', 15000),
('Priya Patel', 'Web Development', 12000),
('Rohan Mehta', 'Data Science', 18000),
('Sneha Iyer', 'UI/UX Design', 10000),
('Karan Verma', 'Cyber Security', 20000);
""")

conn.commit()

cursor.execute("SELECT name, track FROM interns;")
rows = cursor.fetchall()

print("Intern Name | Track")
print("--------------------")
for row in rows:
    print(row[0], "|", row[1])

conn.close()