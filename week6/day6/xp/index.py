# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# output_dict = {}
# for key, value in zip(keys,values):
#     output_dict.update({key:value})

# print(output_dict)

# family = {}
# while True:
#     name = input('whats the party memebers name? if youre done type quit ')
#     if name == 'quit':
#         break
#     age = int(input(f'whats {name}\'s age? '))
#     family[name] = age
#     family.update({name:age})

# total = 0
# for name, age in family.items():
#     if age < 3:
#         continue
#     if 3 <= age <= 12:
#         total += 10
#     if age > 12:
#         total +=15

# print(f'the total for the family is {total}')

#ex3 - zara
# brand = {
#     'name' : 'Zara',
#     'creation_date' : '1975',
#     'creator_name' : 'Amancio Ortega Gaona', 
#     'type_of_clothes' : ['men', 'women', 'children', 'home'], 
#     'international_competitors' : ['Gap', 'H&M', 'Benetton'], 
#     'number_stores' : 7000,
#     'France' : 'blue', 
#     'Spain' : 'red', 
#     'US' : ['pink', 'green'] 
# }
# brand.update({'number_stores' : 2})
# print(f"Zara's clothes are for everyone, {brand['type_of_clothes']}")
# brand.update({'country_creation' : 'spain'})
# brand.pop('creation_date')
# if 'international_competitors' in brand:
#     brand.update({"international_competitors": ['Gap', 'H&M', 'Benetton', 'Desigual']})
# # print(brand['international_competitors'[-1]])
# print(brand['US']) #9
# print(len(brand))
# print(brand.keys())
# more_on_zara = {
#     'creation_date' : 1975,
#     'number_stores' : 10000
# }
# zara = {**more_on_zara, **brand}
# print(zara)
# print(zara['number_stores'])
# print(more_on_zara)
# print(brand)


#ex4 - disney . enumerate**

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# print(list(enumerate(users)))
# for user, num in enumerate(users):
#     print(num, user)
# users.sort()
# print(list(enumerate(users)))
for name in users:
    if 'i' in name:
        print(name)
    if name.startswith('P'):
        print(name)
