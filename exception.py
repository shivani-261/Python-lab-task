print("start code")

try:
    a=int(input("enter A:"))
    b=int(input("enter b:"))
    c=a/b
    print("division:",c)
except zerodivisioerror as e:
    print("exception caught:",e)
print("end code")
                
