l=[1,2,3,4,5,6,7,8,9,10]
even=[]

for i in l:
    if i%2==0:
        even.append(i)

print(even)

l1=filter(lambda x:x%2==0,l)
print(list(l1))
