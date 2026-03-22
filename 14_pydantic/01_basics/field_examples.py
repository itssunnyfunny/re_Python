from pydantic import BaseModel
from typing import List, Optional, Dict

class Cart(BaseModel):
    user_ic: int
    items: List[str]
    quantity: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    body: str
    tags: List[str]
    image_url: Optional[str]
    published: Optional[bool] = None

cart_data = {
    "user_ic": 123,
    "items": ["Laptop", "Mobile", "Tablet"],
    "quantity": {"Laptop": 1, "Mobile": 2, "Tablet": 1}
}

cart = Cart(**cart_data)
print(cart)


