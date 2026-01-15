class Country:
    def __init__(self, name, population, flag, capital_city):
        self.name = name
        self.population = population
        self.flag = flag
        self.capital_city = capital_city
    def show_details(self):
        print(f"{self.name} has population {self.population}, "
              f"capital city is {self.capital_city}, "
              f"flag is {self.flag}")
poland = Country("Poland", "38 mln", "white and red", "Warsaw")

poland.show_details()
