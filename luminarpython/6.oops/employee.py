class employee:
    def setEmployee(self,eid,ename,design):
        self.eid=eid
        self.ename=ename
        self.design=design
    def printValues(self):
        print(self.eid)
        print(self.ename)
        print(self.design)
obj=employee()
obj.setEmployee(101,"anusree","manager")
obj.printValues()

obj1=employee()
obj1.setEmployee(102,"deepak","assistant manager")
obj1.printValues()

obj3=employee()
obj3.setEmployee(103,"renu","clerk")
obj3.printValues()
