#inheritance

class a:
    def fun1(self):
        print("Hello Java")

class b:
    def fun2(self):
        print("Hello Python")

# obj1 = a()
# obj2 = b()
# obj1.fun1()
# obj2.fun2()

#single
class account:
    def bank(self):
        print("Bank Name : Axis Bank")

class saving_acc(account):
    def holder(self):
        print("Account Holder : Yokesh")

# sa = saving_acc()
# sa.holder()
# sa.bank()


class battery:
    def power(self):
        print("Power Source")

class mobile(battery):
    def call(self):
        print("Network is ON..")

class Smartphone(mobile):
    def wifi(self):
        print("Internet Connected")

# sm = Smartphone()
# sm.power()
# sm.call()
# sm.wifi()



class vehicle:
    def name(self):
        print("Indian Vehicle")

class car(vehicle):
    def fun1(self):
        print("4 Wheller")

class bike(vehicle):
    def fun2(self):
        print("2 Wheller")

# c = car()
# c.fun1()
# c.name()
# b = bike()
# b.fun2()
# b.name()


class MusicPlayer:
    def player(self):
        print("Play the Music")

class Camera:
    def pic(self):
        print("Ready to take Picture")

class Mobile(MusicPlayer,Camera):
    def app(self):
        print("Ready to talk")


# m1 = Mobile()
# m1.app()
# m1.player()
# m1.pic()




#method overloading

class cal:
    def add(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            print("4 Arg Add Value :",a+b+c+d)
        elif a!=None and b!=None and c!=None:
            print("3 Arg Add Value :", a + b + c)
        elif a != None and b != None:
            print("2 Arg Add Value :", a + b)
        else:
            print("1 Arg Value :", a)
# c = cal()
# c.add(20,40)
# c.add(20,40,50)
# c.add(20,40,50,70)
# c.add(10)


#method overriding

class ide:
    def run(self):
        print("Run Programs")
class pycharam(ide):
    def run(self):
        super().run()
        print("Run the Python Programs")
class vscode(pycharam):
    def run(self):
        super().run()#pycharam
        print("Run the All Programs")

vs = vscode()
# vs.run()

#Operator Overloading

a = 30
b = "10"

# print(a+b)
print(a.__add__(b))
print(a.__sub__(b))





