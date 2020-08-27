#validate mobile  number#using pattern matching
#step 1 to import re module
from re import *
#9388463566
rule='\d{10}'
mobno=input("enter mob no:")
matcher=fullmatch(rule,mobno)
if(matcher!=None):
    print("valid mob number")
else:
    print("invalid mob number")
