class FibonacciSeries:
    def __init__(self, number):
        self.number = number
    

    def count(self):
        temp=0  
        a=0      
        b=1
        for i in range(self.number):
              temp += a
              a,b=b,a+b
        return temp
  

# Get the input from the user and create an instance of the FibonacciSeries class.
number = int(input('Enter number: '))
obj = FibonacciSeries(number)

# Calculate and print the sum of the Fibonacci series.
print("Sum of the series is", obj.count())




