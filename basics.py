'''
Basics
'''
'''
import random as rn

def conversation(yes, no):
    answers = [yes, no]
    print("Do you want to ask me?")
    for answer in answers:
        if answer != answers[-1]:
            print("{yes} or {y}, ".format(yes=answer, y=answer[0]), end='')
        else:
            print(f"{answer} or {answer[0]}")

    choice = input()
    while choice == "yes" or choice == "y" or choice == "Yes":
        print("How much money do you have?")
        money = int(input("Suggest: "))
        if money >= 1000:
            print("I can give you", money, "dollars")
        elif money >= 500 and money < 1000:
            print("I can give you only", money, "dollars")
        else:
            print(f"I can't give you {money} dollars")
        print("Do you want to ask me?")
        print("(", end='') 
        for i in range(len(answers)):
            if answers[i] != answers[-1]:
                print(f"{answers[i]}, ", end='')
            else:
                print("{0}".format(answers[i]), end='')
        print(")") 
        choice = answers[rn.randint(0, len(answers)-1)]
        print(choice)
    return choice
'''
'''
listOfAnswers = ['yes', 'no']
listOfAnswers.append(['Yes', 'No'])
listOfAnswers.insert(len(listOfAnswers), ['Yes', 'No'])
print(conversation(*listOfAnswers[2]))
'''
'''
dictOfAnswers = {
    'first answer': [
        'yes',
        'no'
    ],
    'second answer': [
        'no',
        'yes'
    ]
}
conversation(dictOfAnswers["first answer"][0], dictOfAnswers["second answer"][0])
'''

'''
OOP
'''
'''
class Worker:
    def __init__(self, name='Default', age='default'):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
 
    def setName(self, name):
        self.__name = name
    def setAge(self, age):
        self.__age = age

    def whatCanIDo(self, subject):
        pass

class Teacher(Worker):
    def whatCanIDo(self, subject=None):
        if subject is not None:
            print(f"I can teach {subject}!")
        else:
            print("I can't teach anything!")

class Student(Worker):
    def whatCanIDo(self, subject=None):
        if subject is not None:
            print(f"I can study {subject}!")
        else:
            print("I can't study anything!")



student = Student('John', 20)
print("John's name: {name}".format(name=student.getName()))
print("John's age: {age}".format(age=student.getAge()))
student.setAge(21)
print("John's name: {name}".format(name=student.getName()))
print("John's age: {age}".format(age=student.getAge()))
student.whatCanIDo('English')
teacher = Teacher('Luisa', 58)
print("Luisa's name: {name}".format(name=teacher.getName()))
print("Luisa's age: {age}".format(age=teacher.getAge()))
teacher.setAge(60)
print("Luisa's name: {name}".format(name=teacher.getName()))
print("Luisa's age: {age}".format(age=teacher.getAge()))
teacher.whatCanIDo()
'''

'''
Advanced concepts
'''
# Generators
'''
def fibonacci():
    fib1, fib2 = 0, 1
    while True:
        yield fib1
        fib1, fib2, = fib2, fib1 + fib2
fibGenerator = fibonacci()
for i in range(0, 5 + 1):
    print(f" F[{i}] = {next(fibGenerator)}", end='')
print()

def findLines(filename, keyWord):
    with open(filename, 'r') as file:
        for line in file:
            if keyWord in line:
                yield line
linesGen = findLines("file.txt", "ERROR")
print(next(linesGen).strip())
print(next(linesGen).strip())
print(next(linesGen).strip())
'''
# Descriptors
'''
class ReversedStringDescriptor:
    def __get__(self, instance, owner):
        print('get method invoked')
        return self.value[::-1]
    def __set__(self, instance, value):
        print('set method invoked')
        self.value = value
    def __delete__(self, instance):
        print('delete method invoked')
        del self.value

class MyClass:
    myAttribute = ReversedStringDescriptor()
    def __init__(self):
        self.__myAttribute = ReversedStringDescriptor()

    def setAttribute(self, myAttribute):
        self.__myAttribute = myAttribute

obj = MyClass()
obj.setAttribute('Hello')
obj.myAttribute = 'Hello'
print(obj.myAttribute)
del obj.myAttribute
print(obj.myAttribute)
'''
# Internal and private variables
'''
class Car:
    def __init__(self):
        self._color = "yellow"
        self.__model = "bmw"

car = Car()
print(car._color)
print(dir(car))
print(car._Car__model)
'''
# Decorators
'''
def decorator(func):
    def wrapFun():
        print('*$**$(#*$(#$*))')
        func()
        print('*$**$(#*$(#$*))')
    return wrapFun
def hello():
    print('Hello')
sayHello = decorator(hello)
sayHello()

def decorator(func):
    def wrapFun():
        print('*$**$(#*$(#$*))')
        func()
        print('*$**$(#*$(#$*))')
    return wrapFun
@decorator
def hello():
    print('Hello')
hello()

def decorator(func):
    def wrapFun(*args):
        print('*$**$(#*$(#$*))')
        func(*args)
        print('*$**$(#*$(#$*))')
    return wrapFun
@decorator
def hello(phrase):
    print(f"Say {phrase}")
hello('Hello')
'''
# Comprehensions for lists
'''
list = []
for i in range(50):
    if i % 5 == 0:
        list.append(i)
print(list)

list = [i for i in range(50) if i % 5 == 0]
print(list)
'''
# Comprehensions for dictionaries
'''
dict = {
    0: "item0",
    1: "item1",
    2: "item2"
}
print(dict)

dict = {i:f'item{i}' for i in range(3)}
print(dict)
'''
# Generator comprehension
'''
myGenerator = (i for i in range(2, 5))
print(next(myGenerator))
print(next(myGenerator))
'''
# Regular expressions
'''
import re
txt = "No#pain,#no#gain"
x = re.search("^No.*gain$", txt)
if x:
    print("x: YES! We have a match!")
else:
    print("x: No match")
y = re.findall('ai', txt)
if y:
    print("y: YES! We have a match:", y)
else:
    print("y: No match")
z = re.split("#", txt)
if z:
    print("z: YES! We have a match:", z)
else:
    print("z: No match")
w = re.sub("#", "*", txt)
if w:
    print("w: YES! We have a match:", w)
else:
    print("w: No match")
'''
# File handling
'''
print("FILE BEFORE ALTERING:")
file = open("file.txt", 'r')
contentOfFile = file.readlines()
print(*contentOfFile)
file.close()
file = open("file.txt", 'a')
file.write("Hi-Hi")
file.close()
print("FILE AFTER ALTERING:")
file = open("file.txt", 'r')
contentOfFile = file.readlines(1)
print(*contentOfFile)
file.close()
'''
# Lambda functions
'''
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
'''
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