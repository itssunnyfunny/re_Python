from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="The name of the employee",
        examples=["John Doe", "Jane Doe"]
    )

    department: Optional[str] = "general"
    salary: float = Field(
        ...,
        ge=10000
    )

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$",
    )
    phone: str = Field(
        ...,
        regex=r"^\+?1?\d{9,15}$"
    )
    age: int = Field(
        ...,
        ge=18,
        le=100,
        description="age in years"
    )
    descount: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description= "Discount in percentage"
    )


