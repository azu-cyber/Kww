import math
def printPowerSet(set,SetSize):
    PowerSetSize= (int) (math.pow(2, SetSize))
    inner = 0
    outer = 0
    for outer in range(0,PowerSetSize):
        for inner in range(0,SetSize):
            if((outer & (1 << inner)) > 0):
                print(set[inner], end = " ")
        print("")
size = int(input("Enter array size : "))
set = []
for i in range(0,size):
    n = int(input("Enter element : "))
    set.append(n)
printPowerSet(set, size)
#no.2 project
def totalFlips(number1, number2) :
    flips = 0
    while(number1 > 0 or number2 > 0):
        t1 = (number1 & 1)
        t2 = (number2 & 1)
        if(t1 |= t2):
            flips += 1
        number1>>=1
        number2>>=1
    return False
number1 = int(input("Enter First number : "))
number2 = int(input("Enter Second number : "))
print("\nNumber of flips needed : ",totalFlips(number1, number2))
