class Car:
    def __init__(self, model, brand,age):
        self.model = model
        self.brand = brand
        self.age = age
brands = "Toyota"

models = [
    "Corolla",
    "Camry",
    "RAV4",
    "Highlander",
    "Yaris",
    "Supra",
    "Prius",
    "Land Cruiser",
    "Hilux",
    "Avalon"
]

cars = []

for i in range(10):
    car = Car(
        brand=brands,
        model=models[i],
        age=1 + i
    )
    cars.append(car)

for car in cars:
    print("Brand:", car.brand, " Model:", car.model, " Age:", car.age)