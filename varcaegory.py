x = 5  # global var


def fun():
    x = 10  # local var
    print(x)  # first


age = 25
fun()
print(type(age))  # third
print(x)  # second


class My:
    country = "USA"  # class var
    name = "Alice"  # instance var
    ocunt = 1  # static var


obj = My()
print(type(obj.country))  # fourth


class instanceVar:
    def __init__(self, name, age):
        self.name = name  # instance var
        self.age = age  # instance var

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
obj2 = instanceVar("Bob", 30)
obj2.display()        
