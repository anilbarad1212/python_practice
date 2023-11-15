class Factorial:
    def __init__(self, number):
        self.number = number

    def count(self):
        if self.number == 0 or self.number == 1:
            return 1
        else:
            return self.number * Factorial(self.number - 1).count()

obj = Factorial(6)
result = obj.count()
print(result)


class ArmstrongNumber:
    def __init__(self, number):
        self.number = number

    def is_armstrong(self):
        # Calculate the number of digits in the given number
        num = self.number
        num_of_digits = len(str(num))

        # Calculate the sum of digits raised to the power of num_of_digits
        digit_sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            digit_sum += digit ** num_of_digits
            temp //= 10
            

        # Check if the number is an Armstrong number
        if self.number == digit_sum:
            return True
        else:
            return False

# Input from the user
number = int(input("Enter a number: "))

# Create an ArmstrongNumber object
armstrong_checker = ArmstrongNumber(number)

# Check if the number is an Armstrong number
if armstrong_checker.is_armstrong():
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

