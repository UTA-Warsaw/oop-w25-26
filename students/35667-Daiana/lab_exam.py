# lab_exam.py

class Country:
    def __init__(self, name: str, population: int, capital_city: str):
        self.name = name
        self.population = population
        self.capital_city = capital_city

    def __str__(self):
        return f"{self.name} has a population of {self.population} and its capital city is {self.capital_city}."



if __name__ == "__main__":
    c = Country("Korea", 53771300, "Seoyl")
    print(c)
