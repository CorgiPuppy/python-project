# Comprehensions for lists
list = []
for i in range(50):
    if i % 5 == 0:
        list.append(i)
print(list)

list = [i for i in range(50) if i % 5 == 0]
print(list)

# Comprehensions for dictionaries
dict = {
    0: "item0",
    1: "item1",
    2: "item2"
}
print(dict)

dict = {i:f'item{i}' for i in range(3)}
print(dict)

# Generator comprehension
myGenerator = (i for i in range(2, 5))
print(next(myGenerator))
print(next(myGenerator))