# Exercise Day 3 - 1
age = int(19)

# Exercise Day 3 - 2
height = float(1.63)

# Exercise Day 3 - 3
complex_number = complex(1j)

# Exercise Day 3 - 4
print("Enter base: ")
base = input()
base = float(base)
print("Enter height: ")
height = input()
height = float(height)
area = 0.5 * base * height
area = int(area)
area = str(area)
print("The area of the triangle is " + area)23

# Exercise Day 3 - 5
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is " + str(perimeter))

# Exercise Day 3 - 6
length = int(input("Enter length: "))
width = int(input("Enter width: "))

area_rectangle = length * width
print("The area of the rectangle is " + str(area_rectangle))
perimeter_rectangle = 2 * (length + width)
print("The perimeter of the rectangle is " + str(perimeter_rectangle))

# Exercise Day 3 - 7
r = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * r**2
circumference = 2 * pi * r
area_circle = int(area_circle)
circumference = int(circumference)
print("The area of the circle is " + str(area_circle))
print("The circumference of the circle is " + str(circumference))

# Exercise Day 3 - 8 
m8 = 2
b = -2
x_intercept = int(-b / m8)

print(f"Equation: y = {m8}x + {b}")
print(f"Slope: m = {m8}")
print(f"Y-intercept: {b} (0, {b})")
print(f"X-intercept: {x_intercept} ({x_intercept}, 0)")

# Exercise Day 3 - 9
x1, y1 = 2, 2
x2, y2 = 6, 10

m9 = y2-y1 / x2-x1
distance = ((x2-x1)**2 + (y2-y1)**2) **0.5
print(f"Point 1: {x1}, {y1}")
print(f"Point 2: {x2}, {y2}")
print(f"Slope: m = {m9}")
print(f"Euclidean distance: {distance}")
