class Country:
    def __init__(self, name, population, capital_city):
        self.name = name
        self.population = population
        self.capital_city = capital_city

    def __str__(self):
        return f"Country: {self.name}, Population: {self.population}, Capital: {self.capital_city}"
