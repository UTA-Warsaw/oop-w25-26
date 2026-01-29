class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population


class Country:
    def __init__(self, name, population, flag, capital_city):
        self.name = name
        self.population = population
        self.flag = flag
        self.capital_city = capital_city

    def show_details(self):
        print(f"{self.name} has population {self.population}, capital city is {self.capital_city.name}, flag is {self.flag}")


bishkek = City("Bishkek", "1.1mln")
kyrgyzstan = Country("Kyrgyzstan", "7mln", "red and yellow", bishkek)
kyrgyzstan.show_details()
