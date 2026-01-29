class Country:
    def __init__(self, name, population, capital_city):
        self.name = name
        self.population = population
        self.capital_city = capital_city
    def show_details(self):
        print(f"{self.name} has population {self.population}, "
              f"capital city is {self.capital_city}")

poland = Country("Poland", "38 mln", "Warsaw")

poland.show_details()
