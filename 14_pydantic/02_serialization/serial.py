from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    state: str
    country: str
    postal_code: str

class User(BaseModel):
    id: int
    name:  str
    email: str
    is_active: bool
    address: Address
    created_at: datetime
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")
        }
    )


user = User(
    id=1,
    name="John Doe",
    email="Q2Vj2@example.com",
    is_active=True,
    address=Address(
        street="123 Main Street",
        city="Anytown",
        state="CA",
        country="USA",
        postal_code="12345"
    ),
    created_at=datetime.now(),
    tags=["tag1", "tag2"]
    )

python_dict = user.model_dump()

print(user)
print("="*30)
print(python_dict)

json_str = user.model_dump_json()
print("#"*50)   
print(json_str)