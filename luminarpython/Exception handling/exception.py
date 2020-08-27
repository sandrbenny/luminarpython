num1=int(input("enter a num:"))
num2=int(input("enter a num:"))
try:
    res=num1/num2
    print("result:",res)
    print("process complterd successfully...")
except Exception as e:
    print("exception occured")
    print(e.args)


    

