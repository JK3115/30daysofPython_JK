# Exercises Day 8: Dictionaries
# 1. Create an empty dictionary called "dog"
dog = {}
# 2. Add name, color, breed, legs, and age to the dog dictionary
dog["name"] = "Buddy"
dog["color"] = "Golden"
dog["breed"] = "Golden Retriever"
dog["legs"] = "long"
dog["age"] = 3
# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, and address
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Python", "JavaScript"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main Street"
}
# 4. Get the length of the student dictionary
print(len(student))
# 5. Get the value of skills and check the data type, it should be a list
print(student["skills"])
print(type(student["skills"]))
# 6. Modify the skills values by adding one or two skills
student["skills"]=("HTML","CSS","ClaudeCode")
print(student["skills"])
# 7. Get the dictionary keys as a list
print(list(student.keys()))
# 8. Get the dictionary values as a list
print(list(student.values()))
# 9. Change the dictionary to a list of tuples using items() method
print(list(student.items()))
# 10. Delete one of the items in the dictionary
del student["age"]
print(student)
