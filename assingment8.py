# Assignment 8: Function Polymorphism

import math

def calculate_area(shape, a, b=0):

    if shape == "circle":
        area = math.pi * a * a

    elif shape == "rectangle":
        area = a * b

    elif shape == "triangle":
        area = 0.5 * a * b

    else:
        area = 0

    return area


print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:

    r = float(input("Enter radius: "))
    print("Area =", calculate_area("circle", r))

elif choice == 2:

    l = float(input("Enter length: "))
    w = float(input("Enter breadth: "))
    print("Area =", calculate_area("rectangle", l, w))

elif choice == 3:

    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area =", calculate_area("triangle", base, height))

else:
    print("Invalid choice")
