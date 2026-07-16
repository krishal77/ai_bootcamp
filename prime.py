num = int(input("enter a number: "))
count=0

for i in range(1,num+1):
    if(num%i==0):
        count+=1

    
if count ==2 :
    print(" the entered number is prime number")
else:
    print("the entered number is not prime number")