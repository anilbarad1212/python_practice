# THREAD COMMINICATIONS 

# WHEN TWO OR MORE THREADS COMMUNICATES WITH EACH OTHER ITS CALLED THREAD COMMUNICATIONS .
# THERE ARE THREE METHODS FOR THREAD COMMUNICATIONS 

# EVENT,
# CONDITION
# QUEUE

# EVENT: in event method we need to create event object for share thread communications example e=Event() , it has some method like e.set()
# sets flag = True , e.clear() sets flag = False , e.wait() executes when e.is_set() == True. 

# below is example of event communications

# from threading import Thread,Event
# from time import sleep

# def light_switch():
#     sleep(3)
#     e.set()
#     print('Green light on')
#     sleep(5)
#     print('red light on')
#     e.clear()

# def traffic():
#     e.wait()
#     while e.is_set():
#         print('you can go...')
#         sleep(.5)
#     print('programme done.')   

# e=Event()
# t1=Thread(target=light_switch)
# t2=Thread(target=traffic)
# t1.start()
# t2.start()



# CONDITION :in condition method we need to create event object for share thread communications example cv=Condition() , it has some method like cv.notify()
# and cv.wait(timeout=0) method. 


# from threading import Thread, Condition
# from time import sleep

# lst=[]

# def produce():
#     cv.acquire()
#     for i in range(1,6):
#       lst.append(i)
#       sleep(1)
#       print('item produced')
#     cv.notify()   #this method will notify another thread to be process
#     cv.release()

# def consume():
#    cv.acquire()
#    cv.wait(timeout=0)
#    cv.release()
#    print(lst)
# cv=Condition()    
# t1=Thread(target=produce)
# t2=Thread(target=consume)
# t1.start()
# t2.start()





def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number-1)

number=int(input('enter the number : '))
print(factorial(number))



# for transfer data one database to another database 

# python manage.py dumpdata > data.json
# python manage.py loaddata data.json
