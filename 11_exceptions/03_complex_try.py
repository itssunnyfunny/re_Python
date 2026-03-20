def serve_chai(flavor):
    try:
        print(f"Chai type: {flavor}")
        if flavor == "unknown":
            raise ValueError(f"Unknown chai flavor: {flavor}")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Chai served")
    finally:
        print("Next customer please")

serve_chai("lemon")
serve_chai("unknown")