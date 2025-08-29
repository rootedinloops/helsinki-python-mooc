shape = "-"

while True:
    string = input("Please type in a string: ")
    under = len(string) * shape

    if string == "":
        break
    else:
        print(string)
        print(under)
