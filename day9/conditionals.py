# Conditionals are used to make decisions in code. They allow us to execute different blocks of code based on certain conditions.
# syntax
#code if condition else code

# Exercise Day 9: Conditionals
# Level 1
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, print “You are old enough to drive”, else print “You need to wait {n} years to drive.”, where n is the number of years remaining to turn 18.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:    
    years_remaining = 18 - age
    print(f"You need to wait {years_remaining} years to drive.")
# 2.Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 30 
your_age = int(input("Enter your age: "))   
if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_diff} years older than you.")
elif your_age > my_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")
else:
    print("We are the same age.")
# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is smaller than {b}.")
else:
    print(f"{a} is equal to {b}.")

# Level 2:
# 1. Write a code which gives grade to students according to their scores:
score = float(input("Enter the score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
# 2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
months= {
    "autumn": ["september", "october", "november"],
    "winter": ["december", "january", "february"],
    "spring": ["march", "april", "may"],
    "summer": ["june", "july", "august"]
}
user_month = input("Enter the month: ").lower()
if user_month in months["autumn"]:
    print("The season is Autumn.")
elif user_month in months["winter"]:
    print("The season is Winter.")
elif user_month in months["spring"]:
    print("The season is Spring.")
elif user_month in months["summer"]:
    print("The season is Summer.")
else:
    print("Invalid month entered.")
# 3. The following list contains some fruits: fruits = ['banana', 'orange', 'mango', 'lemon']. If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists in the list print('That fruit already exists in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input("Enter a fruit: ").lower()
if user_fruit not in fruits:
    fruits.append(user_fruit)
    print("Modified list:", fruits)
else:
    print("That fruit already exists in the list.")
# Level 3:
# 1. Here we have a person dictionary. Feel free to modify it !
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# If the person is married and if he lives in Finland, print the information in the following format:
person = {
    'first_name': 'Alex',
    'last_name': 'Johnson',
    'age': 28,
    'country': 'Finland',
    'is_married': True,
    'skills': ['Python', 'Django', 'SQL', 'Machine Learning'],
    'address': {
        'street': 'Elm Avenue',
        'zipcode': 'M5V 1A1'
    }
}
if 'skills' in person:
    middle_index = len(person['skills']) // 2
    print("Middle skill:", person['skills'][middle_index])
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")
    if set(['JavaScript', 'React']).issubset(set(person['skills'])):
        print("He is a front end developer.")
    elif set(['Node', 'Python', 'MongoDB']).issubset(set(person['skills'])):
        print("He is a backend developer.")
    elif set(['React', 'Node', 'MongoDB']).issubset(set(person['skills'])):
        print("He is a fullstack developer.")
    if person.get('is_married') == True and person.get('country') == "Finland":
        print(f"{person['first_name']} {person['last_name']} lives in {person['country']} and is married.")
    else:
        print("Unknown title.")

