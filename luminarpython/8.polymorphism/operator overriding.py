class book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return str(self.pages)
    def __add__(self,others):
        return book(self.pages+others.pages)#operator overriding
    def __sub__(self,others):
        return (self.pages-others.pages)
ob=book(100)
obb=book(200)
obbb=book(300)
print(ob+obb+obbb)#h
# ere ob and obb are book type.addition only perform on string or integer.to make it possible override + operator,using__add__