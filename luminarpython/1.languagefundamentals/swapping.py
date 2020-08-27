num1=10
num2=20
print("value before swapping")
print("num1=",num1)
print("num2=",num2)
#method 1
a=num1
num1=num2
num2=a
print("value after swapping")
print("num1=",num1)
print("num2=",num2)
#method 2
num1=num1+num2#num1=10+20=30
num2=num1-num2
num1=num1-num2

print("value after swapping")
print("num1=",num1)
print("num2=",num2)