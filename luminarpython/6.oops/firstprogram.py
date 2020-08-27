#class
#object
#reference


class ClassName:

class Person:
    def setValues(self,age,name,gender):
        self.age=age
        self.name=name
        self.gender=gender
    def PrintValues(self):
        print(self.age)
        print(self.name)
        print(self.gender)

obj=Person()
obj.setValues(27,"rahul","male")
obj.PrintValues()

obj2=Person()
obj2.setValues(23,"meera","female")
obj2.PrintValues()


