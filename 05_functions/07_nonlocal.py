def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "Lemon"
    kitchen()
    print(f"Chai type: {chai_type}")

update_order()
