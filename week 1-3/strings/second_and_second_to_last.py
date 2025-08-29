string = input("Please type in a string: ")
index_last_let = len(string) -2
last_let = string[index_last_let]
second_let = string[1]

if last_let != second_let:
    print("The second and the second to last characters are different")
else:
    print("The second and the second to last characters are " + second_let)
