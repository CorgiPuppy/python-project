# File handling
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