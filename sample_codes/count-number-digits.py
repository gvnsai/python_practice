#To Count the Number of Digits in a Number.

n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)




"""
output:--
Enter number:6
The number of digits in the number are: 1
"""
