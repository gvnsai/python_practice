# To Reverse a Given Number.

n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)


#output:--
Enter number: 23456
Reverse of the number: 65432