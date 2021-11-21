# def check_arguments(*args):
#     for arg in args:
#         print(f"These are the arguments {arg}")


# my_list = ['Toby', 24, 1, 2, 'hey', 'hello', 'world']

# check_arguments(*my_list)

# print(*my_list, sep='-')
# def  check_keywordedarguments(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key, ':', value)
#     return kwargs

# my_kwargs = check_keywordedarguments(name="Sarah", age=24, profession='coder', favortie_food='burgers')

# check_keywordedarguments(**my_kwargs)
# print('hello you')
# def check_arguments_keywordedarguments(required_arg, *args, **kwargs):
#     print(required_arg)
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)

# check_arguments_keywordedarguments("hello world")
# check_arguments_keywordedarguments("hello world", 1, 2, 'hey')
# check_arguments_keywordedarguments("hello world", 1, 2, 'hey', name="Sarah", age=24)

# def divider(*args):
#     total = 1
#     for num in args:
#         # total = total / num
#         try:
#             total = total / num
#         except ZeroDivisionError:
#             total = total / 1
#         except TypeError:
#             print('you can\'t use strings with this function')
         
#     return total

# print(divider(1,2,3,4,5,6,7,0, 'hello world'))


# print('end of program')


# def my_sum(arg_list):
#     # your code here
#     result = 0
#     for num in arg_list:
#         if isinstance(num, bool):
#             raise Exception('value cannot be a boolean')
#         try:
#             result += num
#             print('im a number', num)
#         except TypeError:
#             print('NaN, skipping')

            
#     return result

# my_list = [2,3,1,2,"four",42, True,False ,1,5,3,"imanumber"]
# # print(my_sum(my_list))
# # 59

# def add_normal(num_1, num_2):
#     return num_1 + num_2

# add = lambda num_1, num_2: num_1 + num_2

# print((lambda num_1, num_2: num_1 + num_2)(5,6))

# def name_titled(first, last):
#     return f'{first.title()} {last.title()}'


# for x in ["Apple", "Banana", "Pear", "Apricot", "Orange"]:
#     print(x) 

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(lambda s:s.upper(), fruit)

# print(list(map_object))

# nums = list(range(5,30))

# def power_of_itself(n):
#     return n**n

# print(list(map(lambda n:n**n, nums)))   # SAME OUTPUT AS BELOW
# print(list(map(power_of_itself, nums))) # SAME OUTPUT AS ABOVE

# my_list = []
# for item in fruit:
#     my_list.append(item**item)



# def starts_with_A(s):
#     return s[0] == "A"

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange", 'anchovy']
# filtered_object = filter(starts_with_A, fruit)
# # filtered_object = filter(lambda s:s[0] == "A", fruit)
# filtered_object = filter(lambda s: "A" in s.upper() and 'e' in s.lower(), fruit)
# print(list(filtered_object))
# from functools import reduce


# numbers = list(range(1,13,2))
# # print(numbers)

# strings = ['hello', 'world', 'lalala', 'land']
# numbers_of_ls = list(map(lambda s:s.count('l'), strings))
# print(numbers_of_ls)
# reduced = reduce(lambda a,b:a+b, numbers_of_ls)
# print(reduced)

# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# # Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters

# def say_hello(username):
#     print(f'hello {username}')
    

# filtered_people = list(filter(lambda s:len(s)<= 4, people))

# list(map(say_hello, filtered_people))



# def get_age(day,month,year):
#     current_year = 2021
#     current_month = 11
#     current_day = 18
#     age = current_year - year
#     if current_month < month:
#         age -= 1
#     elif current_month == month:
#         if current_day < day:
#             age -= 1
#     return age

# def can_retire(gender, date_of_birth):
#     num_date_list = list(map(lambda s:int(s), date_of_birth.split('/')))
    
#     my_age = get_age(*num_date_list)
#     if gender == 'm' and my_age >= 67:
#         return True
#     elif gender == 'f' and my_age >= 62:
#         return True
#     else:
#         return False



# print(can_retire('m', '27/10/1952'))