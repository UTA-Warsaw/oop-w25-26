class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

class Country:
    def __init__(self, name, population, flag, capital_city, biggest_cities):
        self.name = name
        self.population = population
        self.flag = flag
        self.capital_city = capital_city
        self.biggest_cities = biggest_cities 

    def show_details(self):
        print(f"{self.name} has population {self.population}, capital city is {self.capital_city.name}, flag is {self.flag}")
        
        print("Biggest cities are:")
        for city in self.biggest_cities:
            print(f"- {city.name} (Pop: {city.population})")


hometree = City("Hometree (Kelutral)", "7,000 Na'vi")
hells_gate = City("Hell's Gate (RDA Base)", "10,000 Humans")
awa_atlu = City("Awa'atlu (Metkayina Village)", "8,000 Na'vi")

pandora = Country(
    name = "Pandora", 
    population = "~3 Million Na'vi", 
    flag = "Bioluminescent Blue", 
    capital_city = hometree, 
    biggest_cities = [hometree, hells_gate, awa_atlu]
)

pandora.show_details()