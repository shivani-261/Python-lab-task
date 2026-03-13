import udf

while True:
    print("*"*40)
    print("1. OddEven")
    print("2. Max of Two")
    print("3. Max of Three")
    print("4. Prime")
    print("5. Fibonacci")
    print("6. Exit")
    print("*"*40)

    choice=int(int(input("Enter Your Choice : ")))
    print("*"*40)
    if choice==1:
        a=int(input("Enter Number : "))
        udf.oddeven(a)
    elif choice==2:
        a=int(input("Enter Number : "))
        b=int(input("Enter Number : "))
        udf.maxoftwo(a,b)
    elif choice==3:
        a=int(input("Enter Number : "))
        b=int(input("Enter Number : "))
        C=int(input("Enter Number : "))
        udf.maxofthree(a,b,c)
    elif choice==4:
        a=int(input("Enter Number : "))
        udf.prime(a)
    elif choice==5:
        a=int(input("Enter Number : "))
        udf.fibonacci(a)
    elif choice==6:
        print("Thank you for Using Our Services.")
        break
    else:
        print("Invalid Choice. Please Try Again")
    print("*"*40)
