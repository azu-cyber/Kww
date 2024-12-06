from math import gcd
def find_1cm(a, b):
    return abs(a * b) // gcd(a, b)
count = int(input("Enter the number of values: "))
numbers = []
for i in range(count):
    number = int(input(f"Enter number fi + 1}: "))
    numbers .append(number)
print("LM of the numbers is:" find_1cm_multiple(numbers))