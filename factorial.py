def facto(n):
    if n==0 or n==1 :
        return 1
    else:
        return n*facto(n-1)

num = int(input("Enter a number"))

if num<0:
    print("no factorial for engative nunmbers")

else:
    print(" the factorial of given number is", facto(num))