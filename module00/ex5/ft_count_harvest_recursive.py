def ft_count_harvest_recursive(days=0, harvest_day=None):
    if harvest_day is None:
        harvest_day = int(input("Days until harvest: "))

    if days == harvest_day:
        print("Harvest time!")
        return

    days += 1
    print(f"Day {days}")
    ft_count_harvest_recursive(days, harvest_day)
