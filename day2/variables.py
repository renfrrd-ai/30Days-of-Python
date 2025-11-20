""" Day2: 30 Days of Python - Variables """

first_name = "Renfred"
last_name = "Alonge"
full_name = first_name + " " + last_name
country, city = "Canada", "Missussauga"
age = 17
year = 2025
is_married = False
is_true, is_light_on = True, False

print(type(first_name))
print(type(age))
print(type(is_married))
print(len(first_name))
print(len(first_name) == len(last_name))
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two


radius = int(input("Enter radius: "))
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

print(help('keywords'))
