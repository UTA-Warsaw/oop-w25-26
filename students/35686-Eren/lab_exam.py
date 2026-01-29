class Country:
    def __init__(self,name , population, capital_city):
        self.name = name
        self.population = population
        self.capital_city = capital_city

p1 = Country('Turkiye', 80 , 'Ankara')

print(p1.name , p1.population, p1.capital_city)
