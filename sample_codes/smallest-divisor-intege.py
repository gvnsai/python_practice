#To Find the Smallest Divisor of an Integer.

n=int(input("Enter an integer:"))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("Smallest divisor is:",a[0])


"""
output:--
Enter an integer:66
Smallest divisor is: 2
"""
