#BUBBLESORT
lst=[]
n=int(input("enter the limit oflist:"))
print("enter the numbers:")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
len=len(lst)
for i in range(len):
    for j in range(len-1):
        if(lst[j]>lst[j+1]):
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
print(lst)

