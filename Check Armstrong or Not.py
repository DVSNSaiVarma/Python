num = input("Enter a number: ")
order = len(num)
sum = 0
for digit in num:
    sum += int(digit) ** order
if sum == int(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
