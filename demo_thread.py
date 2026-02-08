"""
1.Single level
2.multi-level
3.daemon thread
"""

#threading module
import threading as t

def fire(n):
    print("Fire mode actived to",n)

#fire("M17")

#t1 = t.Thread(target = fire, args = ("ak47",))
#windows(idle)->process -> ram
#process smallest part -> thread->(t1)
#t1.start()


#Multi level thread

def book(n):
    print("Book Name :",n)
def author(n):
    print("Author Name :",n)


t1 = t.Thread(target=book,args=("Learn Java",))
#t2 = t.Thread(target=author,args=("Pradeepa",))

#t1.start()
#t1.join()
#t2.start()

#daemon thread

def book(n):
    print("Book Name :",n)

t1 = t.Thread(target=book,args=("Learn Java",))
t1.setDaemon(True)
print(t1.isDaemon())
t1.start()




    






