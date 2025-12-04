class Predator:
    x = "dangerous"

species_list = ["wolf", "tiger", "lion"]
predators = {species: Predator().x for species in species_list}

print(predators)




