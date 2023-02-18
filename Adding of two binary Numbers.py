a = input("Enter the first binary number: ")
b = input("Enter the second binary number: ")
a_int = int(a, 2)
b_int = int(b, 2)
sum_int = a_int + b_int
sum_bin = bin(sum_int)[2:]
print("The sum of two binary numbers is:", sum_bin)
