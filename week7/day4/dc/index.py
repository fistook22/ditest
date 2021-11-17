
def divide_zero():
    try: print(5/0)
    except ZeroDivisionError: print('this doesn\'t make sense')
divide_zero()