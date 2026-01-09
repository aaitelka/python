def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    print(f"{seed_type.title()} seeds:", end=' ')
    match unit:
        case "packets":
            print(f"{quantity} {unit} available")
        case "grams":
            print(f"{quantity} {unit} total")
        case "area":
            print(f"covers {quantity} square meters")
        case _:
            print("Unknown unit type")
