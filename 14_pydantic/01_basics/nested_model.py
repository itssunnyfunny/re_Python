from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    state: str
    country: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="123 Main Street",
    city="Anytown",
    state="CA",
    country="USA",
    postal_code="12345"
)

user = User(id=1, name="John Doe", address=address)
print(user)

user_data = {
    "id": 2,
    "name": "shani",
    "address": {
        "street": "123 Main Street",
        "city": "Anytown",
        "state": "CA",
        "country": "USA",
        "postal_code": "12345"
    }
}

user = User(**user_data)
print(user)