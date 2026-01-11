def create_character(name, level, character_class, distance):
    return name, level, character_class, distance

name, level, character_class, distance_level = create_character("Legolas", 10, "Archer", 25)
total_exp = 100
movement_speed = 100


print(f"Welcome {name}, you're a level {level} {character_class} with Distance level {distance_level}")