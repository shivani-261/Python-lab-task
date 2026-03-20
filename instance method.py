class Student:
    def sample(self,name,age):
        self.name=name
        self.age=age

    def describe(self):
         return f"{self.name} is {self.age} years old."
Student=Student()
Student.sample("Shivani",22)
print(Student.describe())
