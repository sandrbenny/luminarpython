#method Overriding
#same methods in different class.
class parent:
    def phone(self):
        print("samsung galaxy")
class child:
    def phone(self):
        print("iphone")
c=child()
c.phone()

#both classhave same method but chldhasits own definition.