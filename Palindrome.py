def is_palindrome(input_string):
    return input_string == input_string[::-1]

input_string = input("Enter a word or phrase: ")

if is_palindrome(input_string):
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")
