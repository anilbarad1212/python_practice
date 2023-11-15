# class PrimeNumber:
#     def __init__(self, number):
#         self.number = number

#     def is_prime(self):
#         if self.number <= 1:
#             return f'{self.number} is not a prime number'
#         for i in range(2, self.number):
#             print(i)
#             if self.number % i == 0:
#                 return f'{self.number} is not a prime number'
#         return f'{self.number} is a prime number'

# number = int(input('Enter the number: '))
# obj = PrimeNumber(number)
# print(obj.is_prime())


# def is_prime(number):
#     if number <= 1:
#         return False
#     print(int(number**0.5),'***********')
#     for i in range(2, int(number**0.5) + 1):
#         print(i,'iiiiiiiiiiiiiii')
#         print()
#         if number % i == 0:
#             return False
#     print()    
#     return True

# def generate_primes(limit):
#     prime_numbers = []
#     for num in range(2, limit + 1):
#         print(num,'-----')
#         if is_prime(num):
#             prime_numbers.append(num)
#     return prime_numbers

# # Get the limit from the user
# limit = int(input("Enter a limit to generate prime numbers up to: "))

# # Generate and print prime numbers up to the specified limit
# prime_numbers = generate_primes(limit)
# print("Prime numbers up to", limit, "are:")
# print(prime_numbers)



# class Factorial(object):
#     def __init__(self, number):
#         self.number = number
    
#     def calculate(self):
#         self.temp_variable = 1  # Initialize to 1, as the factorial of 0 is 1
#         while self.number > 0:
#             self.temp_variable *= self.number
#             self.number -= 1
#         return self.temp_variable

# obj = Factorial(5)
# print(obj.calculate())



class Factorial(object):
    def __init__(self, number):
        self.number = number
    
    def calculate(self):
       return int(self.number**0.5)

obj = Factorial(5)
print(obj.calculate())



