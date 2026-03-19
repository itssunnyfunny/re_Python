class Chaicup:
    size = 150 # ml
    def describe(self):
        return f"A {self.size}"
    

cup = Chaicup()

print(cup.describe())
print(Chaicup.describe(cup))