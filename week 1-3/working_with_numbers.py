count = 0
sum1 = 0
pos = 0
neg = 0
print("Please type in integer numbers. Type in 0 to finish.")

while True:
    num = int(input("Number: "))
    if num != 0:
        sum1 += num 
    if num == 0:
        break
    count += 1
    mean = sum1 / count
    if num > 0:
        pos += 1
    if num < 0:
        neg += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum1}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")
