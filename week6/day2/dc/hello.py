user_str = input("please enter a string")
if len(user_str) < 10:
    print("string not long enough")
elif len(user_str) > 10:
    print("string too long")
else:
    print(user_str[0], user_str[-1])

letter = ''
for char in (user_str):
    letter+=char
    print(letter)

from random import shuffle

string = user_str
user_str = list(string)
shuffle(user_str)
string = ''.join(user_str)
print(string)
