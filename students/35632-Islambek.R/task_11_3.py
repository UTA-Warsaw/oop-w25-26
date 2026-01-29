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
        print(f"{self.name} has a population of {self.population}, capital city is {self.capital_city.name}")
        print("Biggest cities:")
        for city in self.biggest_cities:
            print("-", city.name, city.population)
        print()


# Kyrgyzstan
bishkek = City("Bishkek", "1.1mln")
osh = City("Osh", "0.3mln")
jalalabad = City("Jalalabad", "0.1mln")
kyrgyzstan = Country("Kyrgyzstan", "7mln", bishkek, [bishkek, osh, jalalabad])
kyrgyzstan.display_info()

# Kazakhstan
astana = City("Astana", "1.3mln")
almaty = City("Almaty", "2.0mln")
shymkent = City("Shymkent", "1.0mln")
kazakhstan = Country("Kazakhstan", "20mln", astana, [astana, almaty, shymkent])
kazakhstan.display_info()

# Uzbekistan
tashkent = City("Tashkent", "3.0mln")
samarkand = City("Samarkand", "0.5mln")
bukhara = City("Bukhara", "0.3mln")
uzbekistan = Country("Uzbekistan", "36mln", tashkent, [tashkent, samarkand, bukhara])
uzbekistan.display_info()
