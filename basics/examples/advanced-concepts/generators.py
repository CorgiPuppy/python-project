# Generators
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