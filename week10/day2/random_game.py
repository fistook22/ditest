import random
import string
from random import randint
from string import ascii_letters


# def str_generator(size=5, chars=ascii_letters):
#     return "".join(random.choice(chars) for _ in range(size))
#
#
# print(str_generator())

answer = randint(1, 100)

while True:
    try:
        guess = int(input("guess a number between 1-100:  "))
        if 0 < guess < 101:
            if guess == answer:
                print("your a genius!")
                break
        else:
            print("yo lady! i said 1-100!")
    except ValueError:
        print('please enter a number')
        continue
