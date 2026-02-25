

"""
file=open("sample.txt","w")
file.write("Hello,this is a file handling example.")
file.close()
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

with open("sample.txt","r") as file:
    content=file.read()
    print(content)

try:
    with open("missing.txt","r")as file:
        print(file.read())
except FileNotFoundError:
    print("Filenot found.Please check the filename.")
"""

import csv

with open("D:\DS_AI_Internship\src\data1.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)