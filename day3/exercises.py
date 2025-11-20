age = 17
height = 1.75
complex_number = 3 + 5j

# script that prompts user to enter base and height of a triangle and calculates the area
base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
area_of_triangle = 0.5 * base * height
print("The area of the triangle is:", area_of_triangle)

# script that prompts user to enter side a, side b, and side c of a triangle and calculates the perimeter
side_a = float(input("Enter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))
perimeter_of_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter_of_triangle)

# script that prompts user to enter length and width of a rectangle and calculates the area and perimeter
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print("The area of the rectangle is:", area_of_rectangle)
print("The perimeter of the rectangle is:", perimeter_of_rectangle)

# script that prompts user to enter radius of a circle and calculates the area and circumference
radius = float(input("Enter radius of the circle: "))
pi = 3.14
area_of_circle = pi * radius ** 2
circumference_of_circle = 2 * pi * radius
print("The area of the circle is:", area_of_circle)
print("The circumference of the circle is:", circumference_of_circle)

# script that finds slope and Euclidean distance between two points (x1, y1) and (x2, y2)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("The slope between the points is:", slope)
print("The Euclidean distance between the points is:", euclidean_distance)


print(len('python') != len('dragon'))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'python' and 'on' not in 'dragon')
print(str(float(len('python'))))

num = int(input("Enter a number: "))
is_even = (num % 2) == 0
print("Is the number even?", is_even)

print((7 // 3) == int(2.7))
print(type('10') == type(10))
print(int(9.8) == 10)
print(math.floor(9.8) == 10)

# script that asks user to enter hours and rate per hour to calculate weekly earning
hours = float(input("Enter hours worked in a week: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is:", weekly_earning)

# script that converts your age in years to seconds
age_in_years = int(input("How old are you (in years): "))
age_in_seconds = age_in_years * 365 * 3600
print("You have lived ", age_in_seconds)


print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")
