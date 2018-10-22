#To Print Odd Numbers Within a Given Rangeself.

lower=int(input("Enter the lower limit for the range:"))
upper=int(input("Enter the upper limit for the range:"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)




"""
#output:--
Enter the lower limit for the range:2
Enter the upper limit for the range:4
3
"""
