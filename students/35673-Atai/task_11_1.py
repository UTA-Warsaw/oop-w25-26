class Country:
    def __init__(self, name, population, flag, capital_city):
        self.name = name
        self.population = population
        self.flag = flag
        self.capital_city = capital_city
    
    def show_details(self):
        print(f"{self.name} has population {self.population}, capital city is {self.capital_city}, flag is {self.flag}")


poland = Country("Poland", "38mln", "white and red", "Warsaw")
poland.show_details()

france = Country("France", "68mln", "blue, white, and red", "Paris")
france.show_details()