class Car:
    wheels=4
    def sample(self,brand,model):
        self.brand=brand
        self.model=model

Car1=Car()
Car2=Car()

Car1.sample("Toyota","Camry")
Car2.sample("Honda","Civic")

print(Car1.wheels)
print(Car2.wheels)

print("Brand with car1:",Car1.brand)
print("Brand with car2:",Car2.brand)

