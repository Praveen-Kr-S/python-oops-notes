#abstraction
from abc import ABC,abstractmethod
class paypal(ABC):
    @abstractmethod
    def payment(self):
        print("Payment logic")

    @abstractmethod
    def tranfer(self):
        print("tranfer logic")

class gpay(paypal):
    def payment(self):
        print("Gpay payment Excecuted!")
    def tranfer(self):
        print("Gpay money tranfer ")
class pytem(paypal):
    def payment(self):
        print("pytem payment Excecuted!")

    def tranfer(self):
        print("pytem money tranfer ")

# gp = gpay()
# gp.payment()
# gp.tranfer()
#
# pt = pytem()
# pt.payment()
# pt.tranfer()



#decorator

def greething(n):
    def content():
        print("Hello Madava Raj !!")
        n()
        print("Welcome to Livewire")
    content()
# @greething
def data():
    print("I am Kumar")




    












