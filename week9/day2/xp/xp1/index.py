#ex1

# x = abs(-1.456)
# print(x)

# y = int(3.5)
# z = int('5')
# print(y, z)

# print("Enter your name:")
# a = input()
# print("Hello, " + a)

# class MyFuncEX:
#     """x represents a num after the abs built in func turned it to an absolut num.
#      y represents a num after the int built in func turned it to an integer num.
#      z represents a string after the int built in func turned it to an integer num.
#      a represents a string to be entered by the user  then printed in addition.
#     """

#     def do_nothing(self):
#         pass


# print(MyFuncEX.__doc__)


#ex2

class Currency:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.name}s'
    
    def __int__(self):
        return int(f'{self.amount}')
    
    def __repr__(self):
        return f'{self.amount} {self.name}s'
        

    def add(self, other_name):
        self.other_name = other_name
        if self.name != self.other_name:
            raise TypeError(f"can't add two different currencies like {self.name} and {self.other_name}")
        else:
            print(self.amount + self.amount)      
        
        
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(int(c1) + 5)
print(c1.add(c2))
print(c1)
# print(c1 += 5)
print(int(c1)*2)
# print(c1 += c2)
print(int(c1)*4)
print(c1.add(c3))
