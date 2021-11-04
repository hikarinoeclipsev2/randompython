# Hika's Multi Purpose Python Project - Vietnamese Edition
# made by Nam "Hika" Luong
# GNU GPLv3 license
# discord: Hika#5671
# facebook: facebook.com/hikarinoeclipse

import math

# backend
def intFunctionSum(x):
    f = x**10 + x**5 + 1
    print("Giá trị của f(x) là: ", f)

def floatSum(a, b):
    f = a**3 + b**3 + a*b
    print("Giá trị thực của hàm là: ", f)

def rectanglePerimeterSize(a, b):
    p = 2*(a + b)
    s = a*b
    print("Chu vi của hình chữ nhật là: ", p)
    print("Diện tích của hình chữ nhật là ", s)

def Velocity(h):
    v = (2*9.8*h)**1/2
    print("Vận tốc khi rơi tự do là: ", v)

def coordinateDistance(a, b):
    d = ((a - 0)**2 + (b - 0)**2)**1/2
    print("Khoảng cách từ gốc tọa độ tới tọa độ đã cho là: ", d)

def triangleSize(a, b, c):
    half_p = (a+b+c)/2
    s = (half_p*(half_p-a)*(half_p-b)*(half_p-c))**1/2
    print("Diện tích của tam giác đã cho là: ", s)

# submodules GUI
def UI(a):
    if (a == 1):
        print("1: Tính giá trị nguyên của f(x) = x^10 + x^5 + 1")
        x = int(input("Nhập giá trị nguyên của x: "))
        intFunctionSum(x)
    elif (a == 2):
        print("2: Tính giá trị thực của ")
        a = float(input("Enter float value of a: "))
        b = float(input("Enter float value of b: "))
        floatSum(a, b)
    elif (a == 3):
        print("3: Calculate perimeter and size of a rectangle")
        a = float(input("Enter width: "))
        b = float(input("Enter height: "))
        rectanglePerimeterSize(a, b)
    elif (a == 4):
        print("4: Free fall velocity calculator (added 4.11.21)")
        h = float(input("Enter height: "))
        Velocity(h)
    elif (a == 5):
        print("5: Distance to coordinate (added 4.11)")
        a = float(input("Enter x (horizontal) coordinate: "))
        b = float(input("Enter y (vertical) coordinate: "))
        coordinateDistance(a, b)
    elif (a == 6):
        print("6: Triangle size calculator (added 4.11)")
        a = float(input("Enter length of first side: "))
        b = float(input("Enter length of second side: "))
        c = float(input("Enter length of third side: "))
        triangleSize(a, b, c)
    elif (a == 0):
        print("Version 01A")
        print("- added modules")
        print("- github release")
        print("- source code update")
    else:
        print("404: Module not found")

# GUI
print("Welcome to Hika's Multi-Purpose Python Project") 
print("Module List:")
print("1: Calculate integer value of f(x) = x^10 + x^5 + 1")
print("2: Calculate float value of a^3 + b^3 + ab")
print("3: Calculate perimeter and size of a rectangle")
print("4: Free fall velocity calculator (added 4.11.21)")
print("5: Distance to coordinate (added 4.11)")
print("6: Triangle size calculator (added 4.11)")
print("0: Show version number and changelog")

# user input
a = int(input("Select your module: "))

# executes backend
UI(a)

# copyright Nam "Hika" Luong 2021