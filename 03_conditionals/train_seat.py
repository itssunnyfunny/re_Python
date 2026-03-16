seat_type = input("Enter seat type (sleeper/AC/geenral/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioning, beds available")
    case "general":
        print("General - Cheapest option, no revervations")
    case "luxury":
        print("Luxury - Primium seats with meals")
    case _:
        print("Invalid seat type")