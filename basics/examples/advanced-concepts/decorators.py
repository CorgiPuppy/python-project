# Decorators
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