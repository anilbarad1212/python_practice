# class Sumclass_Parent:
#     def __init__(self, number_one, number_two):
#         self.number_three = number_one
#         self.number_four = number_two

#     def first_data(self):
#         return self.number_three + self.number_four



# class Sumclass_One(Sumclass_Parent):
#     def __init__(self, number_one, number_two):
#         self.number_three = number_one
#         self.number_four = number_two

#     def first_sum(self):
#         super().__init__(self.number_three,self.number_four)
#         return self.number_three + self.number_four


# class Sumclass(Sumclass_One):
#     def __init__(self, number_one, number_two):
#         self.number_one = number_one
#         self.number_two = number_two
    
#     def calculate(self):
#         super().__init__(self.number_one,self.number_two)
#         return self.number_one + self.number_two + self.first_sum() + self.first_data()
    


# number_one = int(input('Enter number one: '))
# number_two = int(input('Enter number two: '))


# obj = Sumclass(number_one, number_two)


