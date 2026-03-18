# Functions are reusable pieces of code that perform a specific task. They allow us to break our code into smaller, more manageable chunks, and they can be called multiple times throughout our program.
# Exercises Day 11
# Level 1.
# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.'
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(5, 10))
# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area
print(area_of_circle(5))
# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for num in args:
        if type(num) in [int, float]:
            total += num
        else:
            return "All arguments must be numbers."
    return total
print(add_all_nums(1, 2, 3, 4, 5))
print(add_all_nums(1, 2, "3", 4, 5))
# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(25))
# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    else:
        return 'Summer'
print(check_season("December"))
# 6. Write a function called calculate_slope which return the slope of a linear equation.
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope    
print(calculate_slope(1, 2, 3, 4))
# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates the value of a quadratic equation, solve_quadratic_eqn
def solve_quadratic_eqn(a, b, c):
    discriminant = (b**2 - 4*a*c)**0.5
    x1 = (-b + discriminant) / (2*a)
    x2 = (-b - discriminant) / (2*a)
    return (x1, x2)
print(solve_quadratic_eqn(1, -3, 2))
# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)
print_list([1, 2, 3, 4, 5])
# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst    
print(reverse_list([1, 2, 3, 4, 5]))
def reverse_list(string):
    reversed_string = []
    for i in range(len(string)-1, -1, -1):
        reversed_string.append(string[i])
    return reversed_string 
print(reverse_list(["A","B","C"])) 
# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns the capitalized list of items.
def capitalize_list_items(lst):
    capitalized_lst = []
    for item in lst:
        capitalized_lst.append(item.capitalize())
    return capitalized_lst 
print(capitalize_list_items(["apple", "banana", "cherry"]))
# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(food_list, item):
    food_list.append(item)
    return food_list
print(add_item(["apple", "banana", "cherry"], "orange"))
# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(food_list, item):
    if item in food_list:
        food_list.remove(item)
    return food_list   
print(remove_item(["apple", "banana", "cherry"], "banana"))
# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total    
print(sum_of_numbers(5))
# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            total += i
    return total
print(sum_of_odds(5))
# 15. Declare a function named sum_of_evens. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_evens(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total += i
    return total    
print(sum_of_evens(5))
# Level 2.
# 1. Declare a function named evens_and_odds. It takes a positive integer as parameter and it counts the number of evens and odds in the number.
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of evens are {evens}. The number of odds are {odds}."
print(evens_and_odds(100))
# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not.
def is_empty(param):
    if param:
        return "The parameter is not empty."
    else:
        return "The parameter is empty."
print(is_empty([]))
print(is_empty([1, 2, 3]))
# 4. Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
def greet(name="Guest"):
    if name == "Guest":
        print("Hello, Guest!")
    else:   
        print(f"Hello, {name}!")
    return name
(greet("Alice"))
# 5. Create a function called show_args to take an arbitrary number of named arguments and print their names and values. 
def show_args(**args):
    # Print the prefix once at the start
    print("Received:", end="") 
    for key, value in args.items():
        # Print the pairs separated by a space
        print(f"{key}: {value}", end=" ")
show_args(name="Alice", age=30, city="New York")
# Level 3.
# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if type(n) != int or n <= 1:
        return f"{False} - A prime number is defined as a natural number greater than 1. Your number: {n} ({type(n)})"
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return f"{False} - For any number n > 1, if there is no whole number i (where 2 ≤ i ≤ √n) such that n ÷ i has no remainder, then n is a prime number."
        else:
            return f"{True} - {n} is prime"
# 2. Write a functions which checks if all items are unique in the list.
def are_all_items_unique(lst):
    unique_items = set()
    for item in lst:
        if item in unique_items:
            return False
        unique_items.add(item)
    return True
print(are_all_items_unique([1, 2, 3, 4, 5]))
# 3 - Write a function which checks if all the items of the list are of the same data type.
def is_type(lst):
    _type = set()
    for i in lst:
        _type.add(type(i))
    if len(_type) == 1:
        return f"{True} - All items in the list are of the same data type ({type(lst[0])})"
    else:
        return f"{False} - There are {len(_type)} different data types in the list ({_type})"
# 4. Write a function which check if provided variable is a valid python variable
def is_valid_variable(variable):
    if variable.isidentifier(): # The isidentifier() method checks if the string is a valid identifier in Python. An identifier is a name used to identify a variable, function, class, module, or other object in Python. It must follow certain rules:
        return f"{True} - '{variable}' is a valid Python variable name."
    else:
        return f"{False} - '{variable}' is not a valid Python variable name." 
print(is_valid_variable("my_variable"))
# As the last two exercises were answered in the previous day in a similar fashion, I have decided to skip them.