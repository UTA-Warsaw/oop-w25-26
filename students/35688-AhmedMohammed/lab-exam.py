class Country:
    def __init__(self, name, population, capital_city):
        self.name = name
        self.population = population
        self.capital_city = capital_city

    def __str__(self):
        return f"{self.name} (Capital: {self.capital_city}, Population: {self.population})"

poland = Country("Poland", 40000000, "Warsaw")

