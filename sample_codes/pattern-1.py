#Python Program to Read a Number n And Print the Series “1+2+…..+n= “.

n=int(input("Enter a number: "))
a=[]
for i in range(1,n+1):
    print(i,sep=" ",end=" ")
    if(i<n):
        print("+",sep=" ",end=" ")
    a.append(i)
print("=",sum(a))
 
print()


"""
#output:--
Enter a number: 7
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
"""
