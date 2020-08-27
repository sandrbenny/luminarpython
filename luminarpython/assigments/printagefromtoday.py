bday=int(input("enter your birth date"))
bmonth=int(input("enter your birth month"))
byear=int(input("enter your birth year"))
tday=int(input("enter current date"))
tmonth=int(input("enter current month"))
tyear=int(input("enter current year"))
print("your age is:")
if (bmonth>=tmonth):
   age=tyear-byear-1
   print(age)
if (bmonth==tmonth):
    if (bdate>=tdate):
    age=tyear-byear - 1
    print(age)
else:
    age=tyear-byear
    print(age)

