#method overriding/run time polymorphism
#we need two or more class with inhertance
#same function name in all class

class program:
    def idle(self):
        print("learn language with idle tool")

class vscode(program):
    def idle(self):
        super().idle()
        print("Write the python in vscode")

class pycharm(vscode):
    def idle(self):
        super().idle()
        print("Write the python in pycharm")

obj = pycharm()
# obj.idle()

#operator overloading
a = 10
b = 5
# print(a+b)
# print(a.__add__(b))
# print(a.__add__("Hi"))
# print(a.__sub__(b))
# print(a.__sub__("Hello"))


#abtraction
from abc import ABC, abstractmethod
class upi(ABC):
    @abstractmethod
    def pyment(self):
        print("UPI Pyment Logic")
    @abstractmethod
    def ac(self):
        print("UPI account details Logic")

    def data(self):
        print("Hello users")
class gpay(upi):
    def pyment(self):
        super().pyment()
        print("Gpay pyment excute with upi logic")
    def ac(self):
        print("Gpay account details Logic")
# g = gpay()
# g.pyment()
# g.ac()

#encapsulation
"""
1.private -> __variable
2.protected -> _variable
3.public -> variable
* its apply to both attribute and member function
"""


class ac:
    name = "Sankar"
    _ac = 123456
    __pin = None

    def set_pin(self,pin):
        self.__pin = pin
        # print(self.__pin)


class upi(ac):
    def pyment(self):
        print(super().name)
        print(super()._ac)
        # print(super().__pin)

a = ac()
# print(a.name)
#print(a._ac)
# print(a.__pin)

u = upi()
# u.pyment()
# u.set_pin(3344)


#distructor
class notes:
    def __del__(self):
        print("Complete the tasks")
    def __init__(self):
        print("Take the notes")
    def theory(self):
        print("Python ")


a = notes()
a.theory()
del a
# a.theory()
























