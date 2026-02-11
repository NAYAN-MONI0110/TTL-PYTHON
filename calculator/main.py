while True:
    first_number = int(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /, ^): ")
    second_number = int(input("Enter the second number: "))

    if operator == "+":
        print("The result is:", first_number + second_number)
    elif operator == "-":
        print("The result is:", first_number - second_number)
    elif operator == "*":
        print("The result is:", first_number * second_number)
    elif operator == "/":
        if second_number == 0:
            print("Error: Cannot divide by zero")
        else:
            print("The result is:", first_number / second_number)
    elif operator == "^":
        print("The result is:", first_number ** second_number)
    else:
        print("Invalid operator")

    say_again = input("Do you want to play again? (y/n): ").lower()
    if say_again != "y":
        break
