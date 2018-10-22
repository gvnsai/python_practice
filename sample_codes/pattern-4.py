#Python Program to Print an Inverted Star Pattern


n=int(input("Enter number of rows: "))
for i in range (n,0,-1):
    print((n-i) * ' ' + i * '*')




"""
#output:--
Enter number of rows: 5
*****
 ****
  ***
   **
    *

"""
