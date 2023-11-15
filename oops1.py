import random
class Random_Walk:
    def __init__(self,number):
         self.number=number

    
    def initailize_function(self):
        return self.count_steps(self.number)
    

    def count_steps(self,number):
        x,y=0,0
        total_steps=[]

        for _ in range (number):
            direction = random.choice(["up", "down", "left", "right"])

                
            if direction == "up":
                y += 1
            elif direction == "down":
                y -= 1
            elif direction == "left":
                x -= 1
            elif direction == "right":
                x += 1
            distance = abs(x) + abs(y)
            total_steps.append(distance)

        return sum(total_steps)/len(total_steps)

       
    
number=int(input('enter number of steps: '))
obj=Random_Walk(number)
print(obj.initailize_function())




class Test:
    def my_function_one (self,number):
        if number <= 1:
            return 1
        else:
            return number * self.my_function_one(number-1)
        

    
    def my_function_two(self,number):
        my_list=[]
        for i in range(number, 0, -1):
            my_list.append(self.my_function_one(i))
        return sum(my_list)    
number=int(input('Enter the number :'))
obj=Test()
print(obj.my_function_two(number))