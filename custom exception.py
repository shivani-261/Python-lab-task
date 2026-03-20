print("start code")

try:
    a=int(input("enter A:"))
    b=int(input("enter b:"))
    c=a/b
    print("division:",c)
    l=[10,20,30,40,50]
    index=int(input("Enter index number to fetch element:"))
    print("Element:",l[index])
except Exception as e:
    print("exception caught:",e)
print("End code")
    

                
