def calculate_average(number1, number2):
    """Calculate the average of two numbers."""
    average = (number1 + number2) / 2
    return average

# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculate_average(num1, num2)
print(f"The average of {num1} and {num2} is: {result}")

print("Done")