def count_up_to(n):
    count=1
    while count<=n:
        yield count
        count+=1

counter=count_up_to(5)

for num in counter:
    print(num)
def simple_generator():
    num=1
    
    yield num
    num=num+10
    
gen=simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
