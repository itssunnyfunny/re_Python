from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=1, name="Coffee", price=5.99, in_stock=True)

product_two = Product(id=2, name="Tea", price=4.99, in_stock=False)

product_tree = Product(name="keyboard")