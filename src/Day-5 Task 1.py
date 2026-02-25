def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter   

length = float(input("Enter length: "))
width = float(input("Enter width: "))


area, perimeter = calc_rectangle(length, width)


<<<<<<< HEAD
print("Area:", area, ", Perimeter:", perimeter)
=======
print("Area:", area, ", Perimeter:", perimeter)
>>>>>>> f49fd9c9f786cd21697a7a890c46cae5bcfc5ce6
