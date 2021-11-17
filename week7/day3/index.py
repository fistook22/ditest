# def calculation(x, y):
#     return x + y, x - y

# result = calculation(30, 40)
# print(result)

import random
def hit_or_miss(user_num):
    comp_num = random.randint(1, 100)
    if comp_num == user_num:
        print('good guess')
    else:
        print(f'you gueesed {user_num} and the number is {comp_num}')
    
hit_or_miss(45)
hit_or_miss(16)
