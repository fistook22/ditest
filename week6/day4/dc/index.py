import datetime
birth_date = input('give me your birth date in this format dd/mm/yyyy')
birthdate = datetime.datetime.strptime(birth_date, '%d/%m/%y')
diff = datetime.now() - birthdate
age = diff.days/365

# day, month, year = int(day), int (month), int(year)
# current_date = [11,11,2021]

# age = current_date[2] - year
# if month < current_date[1]:
#     age -= 1
# elif month == current_date[1] and day > current_date[0]:
#     age -= 1

print(f'i am {age} old') 
candles = int(str(age)[-1]) * 'i'

cake = f'''
    {candles}
   |:H:a:p:p:y |
 __|___________|__
|^^^^^^^^^^^^^^^^^|
|:B:i:r:t:h:d:a:y |
~~~~~~~~~~~~~~~~~~~
'''