# Day 6 - Tuples

# 1. Create an empty tuple
tpl = ()
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Mara', 'Leia')
brothers =('Anakin', 'Luke')
# 3. Join brothers and sisters tuples and assign it to siblings
siblings=sisters+brothers
# 4. How many siblings do you have?
total_siblings=len(siblings)
print(total_siblings)
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents=('Han','Padme')
Family_members=parents+siblings
print(f'The members of the family are {Family_members}.')

# Level 2
# 1. Unpack siblings and parents from family_members
father,mother,*siblings = Family_members
parents=(father,mother)
print(f"The parents are {parents} and the siblings are {siblings}")
# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('apple','orange','pear')
vegetables=('carrot','spinach','kale')
animal=('chicken','cow','pig')
food_stuff_tp=fruits + vegetables + animal
# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)
# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if len(food_stuff_tp) % 2 == 0:
    middle_food=print(f'Even,,{[len(food_stuff_tp)//2]} +{[len(food_stuff_tp)//2+1]}')
else:
    middle_food=print(f'Odd,{food_stuff_tp[len(food_stuff_tp)//2]}')
# 5. Slice out the first three items and the last three items from food_stuff_lt list
print(f'First three items:,{food_stuff_tp[0:3]}')
print(f'Last three itesm :{food_stuff_tp[-3:]}')
# 6 - Delete the food_staff_tp tuple completely
del food_stuff_tp
# 7 - Check if an item exists in tuple:
    # Check if 'Estonia' is a nordic country
    # Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"Is Estonia a nordic country? {"Estonia" in nordic_countries}\n"
      f"Is Iceland a nordic country? {"Iceland" in nordic_countries}"
)