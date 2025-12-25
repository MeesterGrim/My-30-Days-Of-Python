# Day 2: 30 Days of python programming'

# Exercises: Level 1
first_name = "First"
last_name = "Last"
full_name = str(first_name + last_name)
country = "country"
city = "city"
age = 250
year =2025
is_married = False
is_true = True
is_light_on = is_true
a, b, c = 0, 1, 2

# Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type([a, b, c]))
print(type(a))
print(type(b))
print(type(c))
print()
print(len(first_name))
if(len(first_name) > len(last_name)):
    print('First name is longer than Last name')
else:
    print('Last name is longer than First name')
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
area_of_circle = 3.14 * (30 ** 2)
circum_of_circle = 2 * 3.14 * 30
try:
    user_radius = input('Please enter a radius: ')
    user_area = 3.14 * (int(user_radius) ** 2)
    print('User area: ' + str(user_area))
except ValueError:
    print("Invalid radius provided")

print()
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
country = input("Please enter your country: ")
if(len(first_name) > len(last_name)):
    print(f'{first_name} is longer than {last_name}')
else:
    print(f'{last_name} is longer than {first_name}')