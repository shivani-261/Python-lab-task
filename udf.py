def oddeven(a):
    if a%2==0:
        print(a,"is even.")
    else:
        print(a,"is odd.")

def maxoftwo(a,b):
    if a>b:
        print(a,"Is max")
    else:
        print(b,"Is max")

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print(a,"Is max")
        else:
            print(c,"Is max")
    elif b>a:
        print(b,"Is max")
    else:
        print(c,"Is max")

def prime(a):
    if a%2==0:
        for i in range (3,int(a/2)+1,2):
            if a%i==0:
                print(a,"is not prime")
    else:
        print(a,"Is prime")

def fibonacci(n):
    a,b=0,1
    print(a,end="")
    while b<n:
        a,b=b,a+b
    print()
