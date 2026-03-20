print("start code")

try:
    a=int(input("enter A:"))
    b=int(input("enter b:"))
    c=a/b
    print("division:",c)
    l=[10,20,30,40,50]
    index=int(input("Enter index number to fetch element:"))
    print("Element:",l[index])
except Zerodivisionerror as e:
    print("exception caught:",e)
    
except Valueerror as e:
    print("exception caught:",e)
    
except Indexerror as e:
    print("exception caught:",e)    
print("end code")
                
