# Exercises Day 5

# 1 - Declare an empty list
list = []
# 2 - Declare a list with more than 5 items
cities = ['new york','los angeles','chicago','seattle','miami']
# 3 - Find the length of your list
print(len(cities))
# 4 - Get the first item, the middle item and the last item of the list
print(cities[0::2])
# 5 - Declare a list called mixed_data_types, put your(name,age,height,marital,status, address)
mixed_data = ['Mike Myers',54, '6 ft 3 in',{'married': 'single'},{'address':'534 Main street, Chicago,IL 21442'}]
# 6 - Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
# 7 - print the list  using print()
print(it_companies)
# 8 - Print the number of companies in the list
print(len(it_companies))
# 9 - Print the first, middle and last company
print(it_companies[0::3])
# 10 - Print the list after modifying one of the companies
it_companies[0]='Samsung'
print(it_companies)
# 11 - Add an IT company to it_companies
it_companies.append('HP')
print(it_companies)
# 12 - Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2,'OpenAI')
print(it_companies)
# 13 - Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1]=it_companies[1].upper()
print(it_companies)
# 14 - Join the it_companies with a string '#;  '
print(", ".join(it_companies))
# 15 - Check if a certain company exists in the it_companies list.
does_exist='Apple' in it_companies
print(does_exist)
# 16 - Sort the list using sort() method
it_companies.sort()
print(it_companies)
# 17 - Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
# 18 - Slice out the first 3 companies from the list
modified_it= it_companies[3::]
print(modified_it)
# 19 - Slice out the last 3 companies from the list
print(it_companies[:-3])
# 20 - Slice out the middle IT company or companies from the list
print(it_companies[0:(len(it_companies)//2)]+ it_companies[len(it_companies) // 2 + 1:])
# 21 - Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)
# 22 - Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies)//2)
# 23 - Remove the last IT company from the list
it_companies.pop()
# 24 - Remove all IT companies from the list
it_companies.clear()
# 25 - Destroy the IT companies list
del it_companies
# 26 - Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
# 27 - After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack=front_end.copy()
full_stack.insert(full_stack.index('Redux')+1,'Python')
full_stack.insert(full_stack.index('Python')+1,'SQL')
print(full_stack)
# Level 2 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
min_age, max_age = ages[0], ages[-1]
# Add the min age and the max age again to the list
ages.extend([min_age,max_age])
# Find the median age (one middle item or two middle items divided by two)
ages.sort()
if len(ages) % 2 == 0:
    print(f'The median is {(ages[len(ages)//2]+ages[len(ages)//2-1])/2}')
else:
    print(f'Odd, the median is {ages(len(ages)//2)}')
# Find the average age (sum of all items divided by their number )
avg_age = sum(ages)/len(ages)
print(f"Average age: {avg_age}")
# Find the range of the ages (max minus min)
ages.sort()
print(f'Range of ages is {(ages[-1]-ages[0])}')
# Compare the value of (min - average) and (max - average), use abs() method
print(abs(min_age - avg_age) == abs(max_age - avg_age))
# Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
middle_country= len(countries)//2
if len(countries) % 2== 0:
    print(f'The middle countries are {countries[middle_country-1],countries[middle_country]}')
else:
    print(f'The middle country is {countries[middle_country]}')
# This is where I findally realized that a list followed immediately by brackets and the index number was calling the value at that index. That had been tripping me up. This makes things considerably easier.
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(countries) % 2 == 0:
    print("Even")
    countries1 = countries[:len(countries)//2]
    countries2 = countries[len(countries)//2:]
else:
    print("Odd")
    countries1 = countries[:len(countries)//2 + 1]
    countries2 = countries[len(countries)//2 + 1:]
print(f"\nNumber in Countries1: {len(countries1)}\n Number in Countries2: {len(countries2)}")
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_list=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
asia, Russo, America, *scandic = countries_list
print(scandic)