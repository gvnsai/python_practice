# to Calculate the Average of Numbers in a Given List

n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))

"""
#output:--
Enter the number of elements to be inserted: 3
Enter element: 5
Enter element: 4
Enter element: 9
Average of elements in the list 6.0
"""
