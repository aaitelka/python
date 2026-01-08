def ft_plant_age():
    plante_age = int(input("Enter plant age in days: "))
    if plante_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
