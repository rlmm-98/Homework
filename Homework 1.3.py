first_number = int(input("Insert a number: "))
second_number = int(input("Insert another number: "))
operation = input("Choose an operation (+ , - , / , * ): ")
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)
else:
    print("I don't recognize the operation")
