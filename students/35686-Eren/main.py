class Car:
    def __init__(self, brand, age):
     self.brand = brand
     self.age = age

c1 = Car('Audi', 5)
c2 = Car('BMW', 7)
print(c1.brand , "is better than", c2.brand, "and their ages are",c1.age, "and", c2.age)