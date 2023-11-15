# class Pattern:
#     def __init__(self, number):
#         self.number = number

#     def create_pattern(self):
#         for i in range(1, self.number + 1):
#             for j in range(1, i + 1):
#                 print('*', end='')
#             print()

# obj = Pattern(5)
# obj.create_pattern()

class Pattern:
    def __init__(self, number):
        self.number = number

    def create_pattern(self):
        for i in range(self.number, 0, -1):
            for k in range(i,self.number):
                print(' ',end='')
            for j in range(0,i):
                print('*', end='')
                print(' ',end='')
            print()
        for i in range(1, self.number+1):
            for j in range(self.number - i):
                print(' ', end='')
            for k in range(1 * i - 1):
                print('*', end='')
                print(' ',end='')
            print()


obj = Pattern(10)    
obj.create_pattern()

