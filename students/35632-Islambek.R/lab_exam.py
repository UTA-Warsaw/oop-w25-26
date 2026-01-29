class Country:
    def __init__(self, name, population, capital_city):
        self.name = name
        self.population = population
        self.capital_city = capital_city

    def get_info(self):
        return {
            "name": self.name,
            "population": self.population,
            "capital_city": self.capital_city
        }
if __name__ == "__main__":
    country = Country("Kyrgyzstan", 7000000, "Bishkek")
    print(country.get_info())
