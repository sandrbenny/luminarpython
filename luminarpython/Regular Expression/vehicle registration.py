#validate vehicle registration number#used for pattern matching
#step 1 to import re module
from re import *
#kl08bn4970
rule='[Kk][Ll][0-9]{2}[a-z]{1,2}\d{4}'
regno=input("enter reg no:")
matcher=fullmatch(rule,regno)
if(matcher!=None):
    print("valid reg number")
else:
    print("invalid regnumber")
