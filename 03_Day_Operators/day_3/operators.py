import math

# Variable declaration (1-3)
print("\n1-3. VARIABLE DECLARATION")

age = int(19)
height = float(1.63)
complex_number = complex(1j)

print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Complex number: {complex_number}, Type: {type(complex_number)}")

# Area of a triangle (4)
print("\n4. AREA OF A TRIANGLE")

base_triangle = float(input("Enter base: "))
height_triangle = float(input("Enter height: "))
area_triangle = float(0.5*base_triangle*height_triangle)

print(f"The area of the triangle is {area_triangle}")

# Perimeter of a triangle (5)
print("\n5. PERIMETER OF A TRIANGLE")

side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_triangle = side_a + side_b + side_c

print(f"The perimeter of the triangle is {perimeter_triangle}")

# Area and Perimeter of a rectangle (6)
print("\n6. AREA AND PERIMETER OF A RECTANGLE")

length_rectangle = float(input("Enter length: "))
width_rectangle = float(input("Enter width: "))
area_rectangle = length_rectangle*width_rectangle
perimeter_rectangle = 2*(length_rectangle+width_rectangle)

print(f"The area of the rectangle is {area_rectangle} and the perimeter is {perimeter_rectangle}")

# Area and circumference of a circle (7)
print("\n7. AREA AND CIRCUMFERENCE OF A CIRCLE")

radius = float(input("Enter radius: "))
pi = 3.14
area_circle = pi*radius**2
circumference = 2*pi*radius

print(f"The area of the circle is {area_circle} and the circumference is {circumference}")

# Slope, x-intercept, y-intercept (8)
print("\n8. SLOPE, X-INTERCEPT, Y-INTERCEPT \nFORMAT: y = mx + b")

m = float(input("Enter m (slope): "))
b = float(input("Enter b: "))
x_intercept = -b / m
print(f"Slope (m): {m}")
print(f"Y-intercept: {b} (0, {b})")
print(f"X-intercept: {x_intercept} ({x_intercept}, 0)")

# Slope and distance between two points
print("\n9. SLOPE AND DISTANCE BETWEEN TWO POINTS")

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2-y1) / (x2-x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Slope: {slope_points}")
print(f"Euclidean distance: {distance}")

# Slope, x-intercept, y-intercept (8)
print("\n8. SLOPE, X-INTERCEPT, Y-INTERCEPT \nFORMAT: y = mx + b")

m = float(input("Enter m (slope): "))
b = float(input("Enter b: "))
x_intercept = -b / m
print(f"Slope (m): {m}")
print(f"Y-intercept: {b} (0, {b})")
print(f"X-intercept: {x_intercept} ({x_intercept}, 0)")

# Slope and distance between two points (9)
print("\n9. SLOPE AND DISTANCE BETWEEN TWO POINTS")

x1, y1 = [float(x) for x in input("Enter point 1 coordinates here: ").split()]
x2, y2 = [float(x) for x in input("Enter point 2 coordinates here: ").split()]
slope_points = (y2-y1) / (x2-x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Slope: {slope_points}")
print(f"Euclidean distance: {distance}")

# Compare slopes from task 8 and 9 (10)
print("\n10. COMPARE SLOPES FROM TASK 8 AND 9")

print(f"Slope from task 9 (y=2x-2): {m}")
print(f"Slope from task 10 (points): {slope_points}")
if m == slope_points:
    print("The slopes are equal or parallel")
elif m*slope_points == -1:
    print("The slopes are negative reciprocals (perpendicular lines)")
else:
    print("The slopes are neither parallel nor perpendicular")

# Quadratic equation
print("\n11. QUADRATIC EQUATION CALCULATION")

def quadratic(x):
    return x**2 + 6x + 9

# Quadratic equation (11)
print("\n11. QUADRATIC EQUATION CALCULATION")

def quadratic(x):
    return x**2 + 6*x + 9

print("Trying different x values:")
for x in range(-6, 1):
    y = quadratic(x)
    marker = "   -> zero" if y == 0 else ""
    print(f"x = {x:2d}, y = {y:3d}{marker}")
print(f"\n y = 0 when x = -3")
