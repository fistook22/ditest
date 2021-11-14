#ex1
# my_fav_numbers = {22, 5, 7}
# nums_add = (1, 12)
# my_fav_numbers.update(nums_add)
# #theres no index to sets
# friend_fav_numbers = {4,15}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

#ex2
#we can never add anything to tuple

#ex3
# for num in range(1, 21):
#     print(num)

#ex4
# num_list = []

# for num in range(3,10):
#     new_num = num/2
    
#     if str(new_num)[-1] == '0':
#         new_num = num//2
 
#     num_list.append(new_num)
# print(num_list)

#ex5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# basket.pop(0)
# basket.pop()
# basket.insert(2, 'Kiwi')
# basket.insert(0, 'Apples')
# apples_num = basket.count('Apples')
# print(apples_num)
# basket.clear()
# print(basket)

#ex6

# name = input('What is your name?')
# my_name ='shai'
# while name != my_name:
#     name = input('I dont know you, are you sure this is your name?')
    

#ex7
# list = [2,4,4,3,2,7,9,6,0,98,6,43]

# for even in list:
#     if even % 2 == 0:
#         print(even)

#ex8
# for i in range(1500, 2500):
#     if i % 7 == 0:
#         print(i)
#     if i % 5 == 0:
#         print(i)

#ex9
# my_list = []
# user_list = input('give me a list of your fav fruits, plz seperate thm with a single space.')
# my_list.append(user_list.split())
# print(my_list)
# fruit_want = input('what fruit do u want?').split()
# if fruit_want in my_list:
#     print("thst's your fav fruit, enjoy")
# else:
#     print("you chose a new fruit i hope you'll enjoy it")

#ex10
# pizza_price = 10
# topping_price = 2.5
# pizza = []
# to_add = []
# while to_add != 'quit':
#     if to_add != []:
#         print('topping added')
#     to_add = input('what topping would you like on your pizza?')
#     pizza.append(to_add)
# else:
#         pizza.remove('quit')
#         print(f'your pizza toppings are: {pizza}')
        
#         pizza_sum = topping_price * len(pizza) + pizza_price - topping_price
#         print(f'and this is the price {pizza_sum}')
        
#ex11                      Help
# toddler = range(0,2)
# kid = range(3,11)
# adult = range(12,120)
# tod_price = 0
# kid_price = 10
# adult_price = 15
# family_ages = input("your ages please")

#ex12                                Help
# names_list = ['dan', 'david', 'adar']
# new_list = []
# for kick in names_list:
#     age = int(input(f'{names_list[0]} how old are u?'))
#     if age < 16:
#         names_list.remove('dan')
#     age = int(input(f'{names_list[0]} how old are u?'))
#     if age < 16:
#         names_list.remove('david')
#     age = int(input(f'{names_list[1]} how old are u?'))
#     if age < 16:
#         names_list.remove('adar')
# print(names_list)

#ex13 - 14                      Help
# sandwich_orders = ['sabich', 'panini', 'chala', 'hot dog']
# finished_sandwich = []
# for make in sandwich_orders:
#     finished_sandwich.append(make)
#     print(f'i made {finished_sandwich}')



