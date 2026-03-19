# Day 12 - Modules
# Level 1 
# 1. Write a function which generates a six digit/character random_user_id.
import random
import string
def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    random_user_id = ''.join(random.choice(characters) for _ in range(6))
    return random_user_id
print(generate_random_user_id())
# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_characters = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    characters = string.ascii_letters + string.digits
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_characters))
        user_ids.append(user_id)
    return user_ids
print("\n" + "\n".join(user_id_gen_by_user()))
# 3. Write a function named rgb_color_gen. It will generate rgb colors in the form of rgb(0,0,0) to rgb(255,255,255).
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())
# Level 2
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num_colors):
    hexa_colors = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        hexa_colors.append(color)
    return hexa_colors
print(list_of_hexa_colors(5))
# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f"rgb({r},{g},{b})")
    return rgb_colors
print(list_of_rgb_colors(5))    
# 3. Write a function generate_colors which can generate any number of hexa or rgb colors. It takes a string parameter which can be either hexa or rgb.
def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."
print(generate_colors('hexa', 5))
# Level 3
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list.
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print(shuffle_list([1, 2, 3, 4, 5]))
# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    numbers = random.sample(range(10), 7)
    return numbers
print(unique_random_numbers())