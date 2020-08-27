#METHOD OVERLOADING
#same method in with different parameters in single class
class Math:
    def add(self):
        num=10
        num2=20
        print(num+num2)
    def add(self,num1):
        num=20
        print(num1+num2)
    def add(self,num1,num2):
        print(num1+num2)
m=Math()
m.add(10,20)
#m.add(10)
#DIRECTLY NOT SUPPORTED IN PYTHON .ONLY LAST METHOD WILL WORK.