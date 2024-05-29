#recursion - Defining something in terms of itself

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

def fibonnaci(n):
    if(n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)

print(fibonnaci(6))