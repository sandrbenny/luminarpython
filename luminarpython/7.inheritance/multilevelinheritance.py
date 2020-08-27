class parent:
    def m1(self):
        print("inside parent")
class child(parent):
    def m2(self):
        print("inside child")
class subchild(child):
    def m3(self):
        print("inside subchild")
s=subchild()
s.m1()
s.m2()
s.m3()