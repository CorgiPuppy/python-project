# Lambda functions
number = 5
def square(num):
    return num * num
print(f"square function: {square(number)}")
squareLambda = lambda num: num * num
print(f"square lambda fun: {squareLambda(number)}")

numbers = [3, 1]
def greatestNumber(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print("greatest number function of", *numbers, ":", greatestNumber(*numbers))
greatestNumberLambda = lambda num1, num2: num1 if num1 > num2 else num2
print("greatest number lambda function of", *numbers, ":", greatestNumber(*numbers))