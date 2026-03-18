def pure_cahi(cups):
    return cups *10

total_chai =0 
#not recommended
def impure_cahi(cups):
    global total_chai
    total_chai += cups *10

def pour_chai(n):
    print(f"Pouring {n} cups of chai")
    if n==0:
        return "All cups poured"
    return  pour_chai(n-1)

print(pour_chai(5))


chai_types = ["light", "kadak", "ginger", "black", "kulsi"]

strong_chai = list(filter(lambda chai: chai.startswith("k"), chai_types))
print(strong_chai)