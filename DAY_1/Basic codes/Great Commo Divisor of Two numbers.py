print("$$$ GCD OF TWO NUMBERS $$$")
m=int(input(" Enter the value of m: "))
n=int(input("Enter the value of n: "))
while n!=0:
    r=m%n
    m=n
    n=r
print(" GCD is= ",m)
