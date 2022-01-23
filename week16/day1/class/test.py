from datetime import date

from babel import numbers, dates

num = 12345

us_num = numbers.format_decimal(num, locale='en_US')
se_num = numbers.format_decimal(num, locale='sv_SE')

current_date = date(2022, 1, 23)
us_date = dates.format_date(current_date, locale='en_US')
se_date = dates.format_date(current_date, locale='sv_SE')

print(f'the us num is {us_num}')
print(f'the us num is {se_num}')

print(f'The current date is {current_date}')
print(f'The current date is {us_date}')
print(f'The current date is {se_date}')