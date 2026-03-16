l1=["anjali","priyanshi","om","ashvi"]

def findvowels(name):
    if name[0]in"aeiou":
        return name
l2=list(filter(findvowels,l1))
print(l2)
