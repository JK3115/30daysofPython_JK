# Day 2: 30 days of python programming
first_name = 'rob'
last_name = 'cosmonaut'
full_name = 'rob cosmonaut'
country = 'Russia'
city = 'LA'
age = 40
year = '1986'
is_married = True
is_true = True
is_light_on = False
baseball,hockey,football = 'dodgers','sharks','rams'

# Level 2
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
print(type(baseball))
print(type(hockey))
print(type(football))

print(len(first_name))

print(len(first_name) > len(last_name))

num_one = 5
num_two = 4

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

pi=3.14
radius=30

area_of_a_ciricle=pi*(radius**2)
print(area_of_a_ciricle)
circumcference_of_circle=2*pi*radius
print(circumcference_of_circle)
radius_input=input('enter radius ')
radius2=int(radius_input)
input_area=pi*(radius2**2)
print(input_area)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your Country of origin: ")
age = int(input("Enter your age (as a number:) "))

help ('keywords')