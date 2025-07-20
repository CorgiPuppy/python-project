# Exception handling
try:
    num1 = 8
    num2 = 0
    print(num1/num2)
    print("Done calculation")
except ZeroDivisionError:
    print("Error! Don't divide by zero")
except (ValueError, TypeError):
    print("Error")

try:
    number = 10
    string = "hello"
    print(number + string)
    print("Done operation")
except ZeroDivisionError:
    print("Error! Don't divide by zero")
except (ValueError, TypeError):
    print("Error")

try:
    string = "hello"
    zero = 0
    print(string/zero)
    print("Done operation")
except:
    print("Just error")
finally:
    print("This will run anyways: ", 5, "+", 5, "=", 5+5)