class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

class Country:
    def __init__(self, name, population, capital_city, biggest_cities):
        self.name = name
        self.population = population
        self.capital_city = capital_city
        self.biggest_cities = biggest_cities

    def display_info(self):
        cities_names = ", ".join(city.name for city in self.biggest_cities)
        print(f"{self.name} has population {self.population}, "
              f"capital city is {self.capital_city.name}, "
              f"biggest cities: {cities_names}")



warsaw = City("Warsaw", "1.8mln")
lodz = City("Lodz", "0.5mln")
krakow = City("Krakow", "0.6mln")

poland = Country("Poland", "38mln", warsaw, [warsaw, lodz, krakow])

poland.display_info()
