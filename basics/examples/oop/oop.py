'''
OOP
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