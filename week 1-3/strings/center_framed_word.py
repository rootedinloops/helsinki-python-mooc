string = input("Please type in a string: ")
shape = "*"
left_pad = (28 - len(string)) //2
right_pad = 28 - len(string) - left_pad

print(shape * 30)
print (shape + (" " * left_pad) + string + ( " " * right_pad) + shape)
print(shape * 30)
