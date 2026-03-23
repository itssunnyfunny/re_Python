from pydantic import BaseModel, field_validator, model_validator
from time import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name")
    def name_must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError("Name must be capitalized")
        return v


class User(BaseModel):
    email: str

    @field_validator("email")
    def normalize_email(cls, v):
        return v.lower().strip()

class Product(BaseModel):
    price: str # 4.44
    
    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v).replace('$', '')
        return v

class DataRange(BaseModel):
    start_data: datetime
    end_data: datetime

    @model_validator(mode='after')
    def validate_dates(cls, values):
        if values['start_data'] >= values['end_data']:
            raise ValueError('Start date must be before end date')
        return values

