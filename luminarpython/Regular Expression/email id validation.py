#abc@gmail.com
from re import *
rule='\w*@gmail.com'#\w *=\w ethra venelum
id=input("enter id no:")
matcher=fullmatch(rule,id)
if(matcher!=None):
    print("valid ")
else:
    print("invalid")
