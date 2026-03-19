class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 1
    
    @age.setter
    def age(self, age):
        if 1<= age <=10:
          self._age = age
        else:
            raise ValueError("Age must be between 1 and 10")
        

leaf = TeaLeaf(5)
print(leaf.age)
leaf.age = 15
print(leaf.age)
