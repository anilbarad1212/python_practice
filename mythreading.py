# from threading import Thread, current_thread

# class Mythread:
#     def __init__(self):
#         self.name = "Thread-1"

#     def disp(self):
#         print(f"Thread name: {self.name}")

# obj = Mythread()
# t = Thread(target=obj.disp)
# print(t.name)
# t.start()
# t.join()  # Wait for the thread to complete

# # Main thread continues here
# main_thread = current_thread()
# print(f"Main thread name: {main_thread.name}")


from threading import Thread, current_thread

class Mythread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.name = "Thread-1"

    def disp(self):
        print(f"Thread name: {self.name}")

obj = Mythread()
t = Thread(target=obj.disp)
print(t.name)
t.start()
t.join()  # Wait for the thread to complete

# Main thread continues here
main_thread = current_thread()
print(f"Main thread name: {main_thread.name}")


# what is multi tasking :
# there are two part :
# proccess based multi tasking and thread based smulti tasking 

# in proceess based each task are seprates and do not depends on each , they all are executed at once without affecting others its called 
# proccess based multi tasking  example  we can use vs code , chrom , caculator , excel together they are run at same time without 
# affecting each other , it has multiple programme and each has thire own processs .


# while in threaad based multi tasking it has single programme but multi process , it can run without affecting each other and can run at the same 
# time , each pooccess know as thread , example , when we use gmail it can type text and check spell at same time , these are thread which do thire 
# own task at same time 


# what is single tasking  thread :
# when multiple tasks are executed by thread one by one , the its called single tasking thread 
# there is one join() method in thread , it use for run the tread in sequence or line by line.
    



# what is multi threading ?
# multitasking using multi thread 

# when multiple tasks are executed at a time , then its called multi tasking , for this purpose we need more than one thread and 
# when we use more than one thread , its called multi threading.



# what is race condition in thread ?

# race condition is a situation that occurs  when Thread are acting in unexpected sequence , this leading an unreliable output.
# we can solve  thread race conditon  using thread syncronization.


# now what is thread syncronization.

# many thread trying to access the same object can lead to problems like making inconsistant data or getting unexpectedthr output , 
# so when a thread is already accessing an object , stop any other thread to access the same object is called threqd syncronizations.


# the object where the threads are syncronized or access is called syncronized object or mutually exclusive lock(mutex).

# thread syncronized is recommended when multiple threads acting on same object simultaneously.

# there are following techniquest to do thread synchronization.
# -> using Lock
# -> using Rlock(re-entrant lock)
# -> using semaphores 

# lock has two states lock and unlock

# lock has two methods acquire(blockibg=True,timeout=-1) and relese()

# acquire(blocking=True,timeout=-1) means when you define aquire method it will block the code from thereand prevent to access it to another 
# threads , blocking=True is by default it means its block now and timeout=-1 menas it will be bloc forever

# relese() method is used to relese the lock , it can be called from any thread ,not only the thread which has acquired the lock. 



# Rlock(reentrant lock) this is used to lock thread multi ple times , thread which has lock this using acquired method only that thread can
# unlock this process.while in lock it can be lock and unlock(relese) by any thread , we can check information about which thread has lock and 
# relese process how many times using print statement to print Rlock and relese , it will display owner=thread id (every thread has unique id) and count=number means number of lock and 
# unlock 


# and the last one semaphore or bounded semaphore , it takes one argument boundedsemaphore(2) here two is number of thread you want to 
# allow to access the proess at same time , it will allow two threads at same time to process , if one of them is relese then third one will 
# allow to enter , we can check using print statement self.thread_name._value it will return number of threads alow at eachtime .

# syntax of lock,rlock and semaphore 

# syntax : in class based view define self.l=Semaphore , here l in variable name , self.l.acquire() and self.l.relese() same in 
# lock and rlock.


# DUCK TYPING AND STRONG TYPING IN PYTHON 

# duck typing meanssupose we have define class and methods , when we call that method python do not care about which class has been 
# called and which object it is , it just looking for method which you want to call , if it will not find that particular 
# method then it will genrate error , for this scenario we use strong typing , strongtyping has method call hasattr('obj','methodname')
# it will call the method if its exist.  


# METHOD OVERLOADING IN PYTHON 

# when we try to define multiple methods with same name in single calss , the accoerdig to python behaviour it will override 
# the first method , this is called method overloading.



# METHOD OVERRIDING 

# mathod overriding in python is when you define method in parent class and when you override this method in child class with same name 
# its called method overriding , however if you wish to overrdide the parent class method without affecting its own property then you can use
# super method to call parent class method.

# class Mul:
#     def defined(self,x,y):
#         print(x*y)

# class Add(Mul):
#     def defined(self,a,b):
#         super().defined(a,b)
#         print(a+b)
# obj=Add()
# obj.defined(5,5)


# OPERATOR OVERLOADING 


# Operator overloading is a feature in object-oriented programming languages that allows you to define and 
# customize the behavior of operators
# (such as +, -, *, /, ==, !=, etc.) for instances of user-defined classes. 
# It enables you to define how these operators should work with objects of your own classes. 


# class A:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         return self.x + other.x

# class B:
#     def __init__(self,x):
#         self.x=x

#     def __add__(self,other):
#         return self.x + other.x    
# a=A(100)
# b=B(200)
# print(a+b)