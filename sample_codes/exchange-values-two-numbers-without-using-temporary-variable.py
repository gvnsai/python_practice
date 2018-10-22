#To Exchange the Values of Two Numbers Without Using a Temporary Variable.

a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is:",a," b is:",b)

"""
#output:--
Enter value of first variable: 1
Enter value of second variable: 2
a is: 2  b is: 1
"""
