class parent:
    def m1(self):
        print("inside parent1")
class child:
    def m2(self):
        print("inside parent2")
class subchild(parent,child):
    def m3(self):
        print("inside child")
s=subchild()
s.m1()
s.m2()
s.m3()
        