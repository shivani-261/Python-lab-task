d={1:"jigar",2:"Ajay",3:"Vijay",4:"Kamal",5:"Ketan"}
key=int (input("Enter existing key:"))
value=input("Enter New value:")

if key in d:
    d[key]=value
else:
    print("key is not presented in dictionary")
print(d)
