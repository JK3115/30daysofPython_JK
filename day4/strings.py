# Exercises - Day 4 Strings

# 1 - Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Number = 'Thirty '
Time = 'Days Of '
Coding = 'Python'
Title = Number + Time + Coding
print(Title)

# 2 - Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
First = "Coding "
Second = "For "
Who = "All"
Connect = First + Second + Who
print(Connect)

# 3 - Declare a variable named company and assign it to an initial value "Coding For All"
company = "Coding For All"

# 4 - Print the variable company using print().
print(company)

# 5 - Print the length of the company string using len() method and print().
print(len(company))

# 6 - Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7 - Change all the characters to lowercase letters using lower() method
print(company.lower())

# 8 - Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.capitalize(),"\n",company.title(),"\n",company.swapcase())

# 9 - Cut(slice) out the first word of Coding For All string.
cut_coding = company[7:]
print(cut_coding)

# 10 - Check if Coding For All string contains a word Coding using the method index, find or other methods
print(company.find('Coding'))

# 11 - Replace the word coding in the string 'Coding For All' to Python
print(company.replace('Coding','Python'))

# 12 - Change "Python for Everyone" to "Python for All" using the replace method or other methods.
python = "Python for Everyone"
print(python.replace('Everyone','All'))

# 13 - Split the string 'Coding For All' using space as the separator (split()) 
print(company.split())

# 14 - "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
big_tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(big_tech.split(', '))

# 15 - What is the character at index 0 in the string Coding For All
print(company[0])

# 16 - What is the last index of the string Coding For All.
print(len(company)-1)

# 17 - What character is at index 10 in "Coding For All" string
print(company[10])

# 18 - Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym="Python For Everyone".split()
print(f"{acronym[0][0]}{acronym[1][0]}{acronym[2][0]}")

# 19 - Create an acronym or an abbreviation for the name 'Coding For All'.
print(f"{company.split()[0][0]}",
      f"{company.split()[1][0]}",
      f"{company.split()[2][0]}")

# 20 - Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# 21 - Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# 22 - Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People".rfind("l"))

# 23 - Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
example= 'You cannot end a sentence with because because because is a conjunction'
print(example.find('because'))

# 24 - Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(example.rfind('because'))

# 25 - Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(example.replace('because because because',""))

# 26 - Duplicate of 23
# 27 - Duplicate of 25

# 28 - Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

# 29 - Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))

# 30 - '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())

# 31 - Which one of the following variables return True when we use the method isidentifier(): 
print(f"{"30DaysOfPython".isidentifier()}\n"
      f"{"thirty_days_of_python".isidentifier()}")

# 32 - The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lib_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(lib_list))

# 33 - Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge\nI just wonder what is next")

# 34 - Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity\n"
      "Asabeneh\t250\tFinland\tHelsinki")

# 35 - Use the string formatting method to display the following:
radius = 10
pi = 3.14
area = pi * radius ** 2
print(f'The radius is {radius} \nThe area = {pi} * radius ** 2 \nThe area of a circle with radius { radius} is {area}')

# 36 - Make the following using string formatting methods:
a=8
b=6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))