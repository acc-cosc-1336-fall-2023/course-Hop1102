#homework 2

import decisions

option = int(input('Enter a numerical option for ratio:'))

total = int(input('Enter a numerical total for ratio:'))

result = decisions.get_options_ratio(option, total) 

print(result)

value = decisions.get_faculty_rating(result)

print(value)





