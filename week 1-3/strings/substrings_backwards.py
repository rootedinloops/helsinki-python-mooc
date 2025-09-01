string = input("Please type in a string: ")
start = len(string) -1

while start >= 0:
    print(string[start:len(string) + 1])
    start -= 1
