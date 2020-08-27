from re import *
#pattern='[a-zA-Z]'
#pattern='[^0-9]'
#pattern='[^a-zA-Z0-9]'

#predefined characters
#.............................
#pattern='\s'#check for spaces
#pattern='\d'#check for digit
#pattern='\D'#prints,except all digits
#pattern='\w'#check for all elements
pattern='\W'#special characters

matcher=finditer(pattern,"abc23#4AXv")

for match in matcher:
    print(match.start())
    print(match.group())