# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sample_dict['class']['student']['marks']['history'])
# sample_dict['class']['student']['marks']['history'] = 150
# print(sample_dict['class']['student']['marks']['history'])
# sample_dict['class']['student']['marks']['history']['chmistry'] = 6660
# print(sample_dict['class']['student']['marks']['history']['chemistry'])



#ex 4  - week 6 day 4 xp gold - fruit shop
items = [
    {"banana": 4},
    {"apple": 2},
    {"orange": 1.5},
    {"pear": 3}
]
print(items)
for fruit, price in items.items():
    items[fruit] = {'stock' : 1, 'price': price}
print(items)