# class First_Pattern:
#     def __init__(self,number):
#         self.number=number
    
#     def print_star(self):
#         for i in range(1,self.number+1):
#             for j in range(i):
#                 print('*',end='')
#             print()


# number=int(input('enter the number :'))
# obj=First_Pattern(number)
# print(obj.print_star())


# class First_Pattern:
#     def __init__(self,number):
#         self.number=number
    
#     def print_star(self):
#         for i in range(self.number,0,-1):
#             for j in range(i):
#                 print('*',end='')
#             print()


# number=int(input('enter the number :'))
# obj=First_Pattern(number)
# print(obj.print_star())

# from colorama import Fore
# import random

# class First_Pattern:
#     def __init__(self,number):
#         self.number=number
    
#     def print_star(self):
#         for i in range(self.number,0,-1):
#             color_choices=random.choice([Fore.BLUE,Fore.GREEN,Fore.RED,Fore.YELLOW])
#             for k in range(i,self.number):
#                 print(' ',end='')
#             for j in range(i):
#                 print(color_choices + '*',end=' ')
#             print()


# number=int(input('enter the number :'))
# obj=First_Pattern(number)
# print(obj.print_star())


from colorama import Fore
import random

class First_Pattern:
    def __init__(self,number):
        self.number=number
    
    def print_star(self):
        for i in range(self.number,0,-1):
            color_choices=random.choice([Fore.BLUE,Fore.GREEN,Fore.RED,Fore.YELLOW])
            for k in range(i,self.number):
                print(' ',end='')
            for j in range(i):
                print(color_choices + '*',end=' ')
            print()
            if i <= 1:
                for i in range(0,self.number+1):
                    color_choices=random.choice([Fore.BLUE,Fore.GREEN,Fore.RED,Fore.YELLOW])
                    for k in range(self.number-i):
                        print(' ',end='')
                    for j in range(i):
                        print(color_choices+'*',end=' ')
                    print()
                    

number=int(input('enter the number :'))
obj=First_Pattern(number)
print(obj.print_star())

