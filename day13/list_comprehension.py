# Day 13 List Comprehension
# Exercises Level  1
# Filter only negative and zero in the list using list comprehension, numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print(negative_and_zero)
# 2. Flatten the following list of lists using list comprehension: [[1, 2, 3], [4, 5], [6, 7, 8]]
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = [num for row in list_of_lists for num in row]
print(flattened_list)
# 3. Using list comprehension create the following list of tuples: 
list_of_tuples = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
def print_tuples(tuples):
    for tup in tuples:
        print(tup)
print_tuples(list_of_tuples)
# 4. Flatten the following list to a new list: countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [('Finland', 'Helsinki'), ('Sweden', 'Stockholm'), ('Norway', 'Oslo')]
def flattened_abriv_list(countries: list[tuple]) -> list[tuple]:
    return [(country[0].upper(), country[0][:3].upper(), country[1].upper()) for country in countries]
flattened_countries = flattened_abriv_list(countries)
print(flattened_countries)
# 5.Change the following list to a list of dictionaries:
countries = [('Finland', 'Helsinki'), ('Sweden', 'Stockholm'), ('Norway', 'Oslo')]
dict_countries = [{'country': country[0], 'city': country[1]} for country in countries]
print(dict_countries)
# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
def concat_names(names: list[tuple]) -> list[str]:
    return [f"{name[0][0]} {name[0][1]}" for name in names]
print(concat_names(names))
# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x, y, m: y - m * x
print(slope(1, 2, 3, 4))  # Output: 1.0