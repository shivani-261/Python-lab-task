import random

data1=open("data1.txt","w")
for i in range(10):
    data1.write(str(random.randint(1,100))+",")
data1.close()

data1=open("data1.txt","r")
prime=open("prime.txt","w")
l=data1.read().split(",")[:-1]
for i in l:
    num=int(i)
    count=0

    for j in range(1,num+1):
        if num%j==0:
            count+=1
            
    if count==2:
        prime.write(str(num)+",")
                    
data1.close()
prime.close()
    
print("Prime Numbers:")
prime=open("prime.txt","r")
print(prime.read())
prime.close()
