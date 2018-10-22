#Python Program to Read Print Prime Numbers in a Range using Sieve of Eratosthenes.

n=int(input("Enter upper limit of range: "))
sieve=set(range(2,n+1))
while sieve:
    prime=min(sieve)
    print(prime,end="\t")
    sieve-=set(range(prime,n+1,prime))
 
print()


"""
#output:--
Enter upper limit of range: 5
2	3	5
"""
