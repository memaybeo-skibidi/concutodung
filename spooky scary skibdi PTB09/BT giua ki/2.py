# This program takes two numbers as input and performs addition, subtraction, multiplication, and division.
# Input: Two numbers entered by the user.
# Output: Results of addition, subtraction, multiplication, and division.

# Prompt the user to input two numbers.
a = float(input("Nhâp số đầu tiên (a): "))
b = float(input("Nhập số thứ 2 (b): "))

# Perform the calculations.
sum_result = a + b
difference = a - b
product = a * b

# Check for division by zero before performing division.
if b != 0:
    quotient = a / b
else:
    quotient = "undefined (division by zero)"

# Print the results.
print("\nResults:")
print(f"Cộng (a + b): {sum_result}")
print(f"Trừ (a - b): {difference}")
print(f"Nhân (a * b): {product}")
print(f"Chia (a / b): {quotient}")