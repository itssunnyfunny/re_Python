chai_type = "Plain"

def front_desk():
    chai_type = "Ginger chai"
    def kitchen():
        global chai_type
        chai_type = "Irani chai"
    kitchen()
    print(f"Chai type: {chai_type}")

front_desk()
print(f"Chai type: {chai_type}")