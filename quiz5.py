num = float(input("Enter the first number: "))
num1 = float(input("Enter the second number: "))
num2 = float(input("Enter the third number: "))
largest = num
if num1 > largest:
    largest = num1
if num2 > largest:
    largest = num2
answer= ("The largest value is:", largest)
print(answer)

