tpl = tuple()
brothers = ('Esmond')
sisters = ('Ella')
siblings = brothers + sisters
print(len(siblings))
family_members = tuple(list(siblings) + ['******', '_____'])
siblings, parents = family_members[0:2], family_members[2:4]
fruits = ('apple', 'orange')
veggies = ('lettuce', 'broccoli')
animal_products = ('egg', 'fish')
food_stuff_tp = fruits + veggies + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[2:4])
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
