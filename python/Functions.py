def emtpyfunc():
    pass#avoids the error
    #afunction without a body produces an error

def mean(a,b):
    sum=a+b
    mean=sum/2
    print(mean)

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
mean(a,b)