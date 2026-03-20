def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "lemon"]:
        raise ValueError(f"Unknown chai flavor: {flavor}")
    print(f"Brewing chai for {flavor}")


try:
    brew_chai("unknown")
except ValueError as e:
    print(f"Error: {e}")