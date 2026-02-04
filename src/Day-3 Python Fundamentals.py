"""
numbers=[10,20,30,40]
coordinates=(5,10)
print(numbers)
print(coordinates)


a=[100,200,300,400,500,600,700,800,900]
print(a[-3:-1])

print(a[1:4:1])
print(a[-4:-1:2])
"""
a = [5, 2, 9, 1, 7]
a.sort()
print(a)

a = [5, 2, 9, 1, 7]
a.sort(reverse=True)
print(a)
a.append(4)        
a.insert(1, 10)   
a.extend([5, 6])   
a.pop()            

print(a)
