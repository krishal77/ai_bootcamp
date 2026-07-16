num = int(input("Enter a number"))

original = num
reverse =0

while num> 0:
    digit = num% 10
    reverse = reverse*10+digit
    num = num //10

if original == reverse :
    print("the given number is palindrome")
else:
    print("the given number is not palindrome")