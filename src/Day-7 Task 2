import csv

with open("D:\DS_AI_Internship\src\students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["status"] == "Pass":
            print(row["name"])
