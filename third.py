def add_suffix(number):
    if 10 <= number % 100 <= 20:
        suffix = "th"
    else:
        last_digit = number % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"
    return str(number) + suffix

try:
    user_input = int(input("Enter a number: "))
    result = add_suffix(user_input)
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
