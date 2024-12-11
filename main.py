def printito10(n):
    if(n>10):
        return
    print(n)
    printito10(n+1)
printito10(1)
#project 2
def fac(n):
    if(n==1 or n==0):
        return 1
    return n*fac(n-1)
n = int(input("Enter your number : "))
print("Factorial of", n, "is : ",fac(n))