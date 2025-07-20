# Descriptors
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