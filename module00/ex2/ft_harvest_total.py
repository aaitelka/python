def ft_harvest_total():
    weight = 0
    for i in range(3):
        weight += int(input(f"Day {i + 1} harvest: "))
    print(f"Total harvest: {weight}")
