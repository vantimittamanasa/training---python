def fact1(n):
    if n==0 or n==1:
        return n
    return n*fact1(n-1)
print(fact1(6))
        