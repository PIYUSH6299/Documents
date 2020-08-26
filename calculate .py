# # calculate the duration of the year on planets 
# from math import pi

# r = input("radius of the orbit(million km): ")
# v = input("orbit speed(km/s): ")
# r = float(r)
# v = float(v)
# r = r*1000000
# year = (2 * pi * r )/ v
# year = year / (60 * 60 * 24)
# print(round(year))


# # calculate the sum of digits of a random three digit number

# from random import random

# n = random() *  900 + 100
# n = int(n)
# print(n)

# a = n // 100
# b = (n // 10) % 10
# c = n % 10
# print(a + b + c)




# # total surface area of the cylinder

# from math import pi

# h = float(input('h = '))
# r = float(input('r = '))

# circles = 2 * (pi * r ** 2)
# side = 2 * pi * r * h
# area = circles + side

# print('A =',round(area,2))





# # length of circumference and area of a circle

# r = float(input('Radius = '))
# ln = 2 * 3.14 * r
# area = 3.14 * (r ** 2)

# print("Length = %.2f"%ln)
# print("Area = %.2f"%area)

# # find the equation of the line (y = kx + b )passing through known points

# print("A(x1; y1):")
# x1 = float(input("\tx1 = "))
# y1 = float(input("\ty1 = "))

# print("A(x2; y2):")
# x2 = float(input("\tx2 = "))
# y2 = float(input("\ty2 = "))

# print("Equation:")
# k = (y1-y2) / (x1-x2)
# b = y2 - k * x2
# print("\ty = %.2f * x + %.2f" % (k.b)) 








































