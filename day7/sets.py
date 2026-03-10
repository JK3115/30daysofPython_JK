# Exercises Day 7 Sets

# Level 1 
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# 1. Find the length of the set it_companies
print(len(it_companies))
# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Anthropic','OpenAI','Discord'])
print(it_companies)
# 4. Remove one of the companies from the set it_companies
it_companies.remove('Discord')
print(it_companies)
# 5. What is the difference between remove and discard
# Remove and discard both remove items from the set, however remove will raise errors if the item is not found in the list, discard will not

# Level 2 
# 1. Join A and B
C=A.union(B)
# 2. Find A intersection B
print(A.intersection(B))
# 3. Is A subset of B
print(A.issubset(B))
# 4. Are A and B disjoint sets
print(A.isdisjoint(B))
# 5. Join A with B and B with A
A.update(B) # creates new set
B.update(A) # modifies B in-place
# 6. What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# 7 - Delete the sets completely
del A, B, it_companies
# Level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages=set(age)
print(f"Age set bigger than age list: {len(ages) > len(age)}")
# 2. Explain the difference between the following data types: string, list, tuple and set
""" 
String: Immutable text. 
List: Mutable ordered collection. 
Tuple: Immutable ordered collection. 
Set: Mutable unordered unique elements.
 """
# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
teacher=("I am a teacher and I love to inspire and teach people.")
print(f'The number of unique words in the sentence are {len(set(teacher.split()))}')
