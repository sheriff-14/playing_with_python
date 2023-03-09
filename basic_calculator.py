number_1 = int(input("Enter any Number: "))
operator = input("Enter an operator: ")
number_2 = int(input("Enter another Number: "))

if operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "/":
    print(number_1 / number_2)
elif operator == "%":
    print(number_1 % number_2)
else:
    print("Please enter a valid input/operator: ")
