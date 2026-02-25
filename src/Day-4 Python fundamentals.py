"""
a={"usn":123}
print(a)

student={
    "name":"Thrisha",
    "age":22,
    "course":"MCA"

}
print(student["name"])
student["age"]=22
student["city"]="Mangalore"
print(student)


marks={"math":80,"science":75,"english":85}
print(marks.get("math"))
print(marks.get("history",0))
for subject,score in marks.items():
    print(subject,score)
marks.update({"bio":90})
print(marks)

purchases={
    "Alice":200,
    "Bob":300,
    "Charlie":450
}
for name, amount in purchases.items():
    print(f"{name} spent {amount}")


print("Total purchases",len(purchases))

print("customer names:",purchases.keys())

print("customer names:",purchases.values())


n=int(input("Enter number of customers:"))
user_purchases={}
for i in range(n):
    name=input("Enter customer name:")
    amount=int(input(f"Enter purchase amount for {name}:"))
    user_purchases[name]=amount
print("Customer Purchases Data:",user_purchases)

top_customer=max(purchases,key=purchases.get)
print("Top Spending Customer:",top_customer)

Low_customer=min(purchases,key=purchases.get)
print("Top Spending Customer:",Low_customer)
"""

A={1,2,3}
B={3,4,5}
print(A|B)
print(A & B)
print(3 in A)