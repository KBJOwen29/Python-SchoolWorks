def Add(num1, num2):
    return num1 + num2

def Subtract(num1, num2):
    return num1 - num2

def Multiply(num1, num2):
    return num1 * num2

def Divide(num1, num2):
    return num1 / num2

def Retry():
    if input("Retry? (y/n)") == "y":
        main()
    else:
        print("Goodbye")
        exit()


def main():
    print("Provide a number: ", end="")
    num1 = int(input())
    print("Add(+), Subtract(-), Multiply(*), or Divide(/)? ", end="")
    operation = input()
    print("Provide another number: ", end="")
    num2 = int(input())
    if operation == "Add" or operation == "+":
        print(Add(num1, num2))
        Retry()
    elif operation == "Subtract" or operation == "-":
        print(Subtract(num1, num2))
        Retry()
    elif operation == "Multiply" or operation == "*":
        print(Multiply(num1, num2))
        Retry()
    elif operation == "Divide" or operation == "/":
        print(Divide(num1, num2))
        Retry()
    else:
        print("Invalid operation")
        Retry()

main()


