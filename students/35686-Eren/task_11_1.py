class Country:
    def __init__(self, name, population, flag, capital_city):
      self.name = name
      self.population = population
      self.flag = flag
      self.capital_city = capital_city



p1 = Country("Turkiye" , "90m" , "red and white" , "Ankara")

print(p1.name, "has", p1.population, "Its flag is", p1.flag, "And Its capital city is", p1.capital_city)
